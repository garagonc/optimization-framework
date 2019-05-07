# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 15:05:36 2018

@author: garagon
"""

import importlib.util
import json
import threading

import os
from pyomo.environ import *
from pyomo.opt import SolverFactory
from pyomo.opt.parallel import SolverManagerFactory
from pyomo.opt import SolverStatus, TerminationCondition
import time

from IO.inputController import InputController
from IO.outputController import OutputController
from IO.redisDB import RedisDB
from optimization.ModelException import InvalidModelException

from utils_intern.messageLogger import MessageLogger

import pyutilib.subprocess.GlobalData
pyutilib.subprocess.GlobalData.DEFINE_SIGNAL_HANDLERS_DEFAULT = False

class OptControllerDiscrete(threading.Thread):

    def __init__(self, id, solver_name, model_path, control_frequency, repetition, output_config, input_config_parser,
                 config, horizon_in_steps, dT_in_seconds, optimization_type):
        # threading.Thread.__init__(self)
        super(OptControllerDiscrete, self).__init__()
        self.logger = MessageLogger.get_logger(__file__, id)
        self.logger.info("Initializing optimization controller " + id)
        # Loading variables
        self.id = id
        self.results = ""
        self.model_path = model_path
        self.solver_name = solver_name
        self.control_frequency = control_frequency
        self.repetition = repetition
        self.horizon_in_steps = horizon_in_steps
        self.dT_in_seconds = dT_in_seconds
        self.output_config = output_config
        self.input_config_parser = input_config_parser
        self.stopRequest = threading.Event()
        self.finish_status = False
        self.redisDB = RedisDB()
        self.lock_key = "id_lock"
        self.optimization_type = optimization_type

        try:
            # dynamic load of a class
            self.logger.info("This is the model path: " + self.model_path)
            module = self.path_import2(self.model_path)
            self.logger.info(getattr(module, 'Model'))
            self.my_class = getattr(module, 'Model')

        except Exception as e:
            self.logger.error(e)
            raise InvalidModelException("model is invalid/contains python syntax errors")

        if "False" in self.redisDB.get("Error mqtt" + self.id):
            self.output = OutputController(self.id, self.output_config)
        if "False" in self.redisDB.get("Error mqtt" + self.id):
            self.input = InputController(self.id, self.input_config_parser, config, self.control_frequency,
                                         self.horizon_in_steps, self.dT_in_seconds)

    # Importint a class dynamically
    def path_import2(self, absolute_path):
        spec = importlib.util.spec_from_file_location(absolute_path, absolute_path)
        module = spec.loader.load_module(spec.name)
        return module

    def join(self, timeout=None):
        self.stopRequest.set()
        super(OptControllerDiscrete, self).join(timeout)

    def Stop(self):
        try:
            self.input.Stop()
        except Exception as e:
            self.logger.error("error stopping input " + str(e))
        try:
            self.output.Stop()
        except Exception as e:
            self.logger.error("error stopping output " + str(e))
        if self.isAlive():
            self.join(1)

    def update_count(self):
        st = time.time()
        if self.repetition > 0:
            path = "/usr/src/app/optimization/resources/ids_status.txt"
            if os.path.exists(path):
                try:
                    if self.redisDB.get_lock(self.lock_key, self.id):
                        data = []
                        with open(path, "r") as f:
                            data = f.readlines()
                        if len(data) > 0:
                            line = None
                            for s in data:
                                if self.id in s and "repetition\": -1" not in s:
                                    line = s
                                    break
                            if line is not None:
                                i = data.index(line)
                                line = json.loads(line.replace("\n", ""))
                                line["repetition"] -= 1
                                data[i] = json.dumps(line, sort_keys=True, separators=(', ', ': ')) + "\n"
                                with open(path, "w") as f:
                                    f.writelines(data)
                except Exception as e:
                    self.logger.error("error updating count in file " + str(e))
                finally:
                    self.redisDB.release_lock(self.lock_key, self.id)
        st = int(time.time() - st)
        return st

    # Start the optimization process and gives back a result
    def run(self):
        self.logger.info("Starting optimization controller")
        solver_manager = None
        return_msg = "success"
        try:
            ###maps action handles to instances
            action_handle_map = {}

            #####create a solver
            optsolver = SolverFactory(self.solver_name)
            self.logger.debug("Solver factory: " + str(optsolver))
            # optsolver.options["max_iter"]=5000
            self.logger.info("solver instantiated with " + self.solver_name)

            ###create a solver manager
            solver_manager = SolverManagerFactory('pyro')

            if solver_manager is None:
                self.logger.error("Failed to create a solver manager")
            else:
                self.logger.debug("Solver manager created: " + str(solver_manager) + str(type(solver_manager)))

            # self.logger.info("Solvers ipopt = "+ str(SolverFactory('ipopt').available()))
            # self.logger.info("Solvers glpk = "+ str(SolverFactory('glpk').available()))
            # self.logger.info("Solvers gurobi = " + str(SolverFactory('gurobi').available()))

            count = 0
            self.logger.info("This is the id: " + self.id)
            while not self.stopRequest.isSet():
                self.logger.info("waiting for data")
                data_dict = self.input.get_data()  # blocking call
                self.logger.debug("Data is: " + json.dumps(data_dict, indent=4))
                if self.stopRequest.isSet():
                    break

                # Creating an optimization instance with the referenced model
                try:
                    self.logger.debug("Creating an optimization instance")
                    instance = self.my_class.model.create_instance(data_dict)
                except Exception as e:
                    self.logger.error(e)
                # instance = self.my_class.model.create_instance(self.data_path)
                self.logger.info("Instance created with pyomo")

                run_count = 0
                while True:
                    try:
                        # self.logger.info(instance.pprint())
                        action_handle = solver_manager.queue(instance, opt=optsolver)
                        self.logger.debug("Solver queue created " + str(action_handle))
                        self.logger.debug("solver queue actions = " + str(solver_manager.num_queued()))
                        action_handle_map[action_handle] = str(self.id)
                        self.logger.debug("Action handle map: " + str(action_handle_map))
                        start_time = time.time()
                        self.logger.debug("Optimization starting time: " + str(start_time))
                        break
                    except Exception as e:
                        self.logger.error("exception " + str(e))
                        if run_count == 5:
                            raise e
                        time.sleep(5)
                    run_count += 1

                ###retrieve the solutions
                for i in range(1):
                    this_action_handle = solver_manager.wait_any()
                    self.results = solver_manager.get_results(this_action_handle)
                    self.logger.debug("solver queue actions = " + str(solver_manager.num_queued()))
                    if this_action_handle in action_handle_map.keys():
                        self.solved_name = action_handle_map.pop(this_action_handle)
                    else:
                        self.solved_name = None

                start_time = time.time() - start_time
                self.logger.info("Time to run optimizer = " + str(start_time) + " sec.")
                if (self.results.solver.status == SolverStatus.ok) and (
                        self.results.solver.termination_condition == TerminationCondition.optimal):
                    # this is feasible and optimal
                    self.logger.info("Solver status and termination condition ok")
                    self.logger.debug("Results for " + self.solved_name + " with id: " + str(self.id))
                    self.logger.debug(self.results)
                    instance.solutions.load_from(self.results)
                    try:
                        my_dict = {}
                        for v in instance.component_objects(Var, active=True):
                            # self.logger.debug("Variable in the optimization: "+ str(v))
                            varobject = getattr(instance, str(v))
                            var_list = []
                            try:
                                # Try and add to the dictionary by key ref
                                for index in varobject:
                                    var_list.append(varobject[index].value)
                                my_dict[str(v)] = var_list
                            except Exception as e:
                                self.logger.error(e)
                                # Append new index to currently existing items
                                # my_dict = {**my_dict, **{v: list}}

                        self.output.publish_data(self.id, my_dict, self.dT_in_seconds)
                    except Exception as e:
                        self.logger.error(e)
                elif self.results.solver.termination_condition == TerminationCondition.infeasible:
                    # do something about it? or exit?
                    self.logger.info("Termination condition is infeasible")
                else:
                    self.logger.info("Nothing fits")

                count += 1
                if self.repetition > 0 and count >= self.repetition:
                    break

                self.logger.info("Optimization thread going to sleep for " + str(self.control_frequency) + " seconds")
                time_spent = self.update_count()
                for i in range(self.control_frequency - time_spent):
                    time.sleep(1)
                    if self.stopRequest.isSet():
                        break
        except Exception as e:
            self.logger.error(e)
            e = str(e)
            solver_error = "The SolverFactory was unable to create the solver"
            if solver_error in e:
                i = e.index(solver_error)
                i_start = e.index("\"", i)
                i_end = e.index("\"", i_start + 1)
                solver = e[i_start + 1: i_end]
                return_msg = "Incorrect solver " + str(solver) + " used"
            else:
                return_msg = e
        finally:
            # Closing the pyomo servers
            self.logger.debug("Deactivating pyro servers")
            # TODO : 'SolverManager_Pyro' object has no attribute 'deactivate'
            # this error was not present before pyomo update
            # solver_manager.deactivate()
            self.logger.debug("Pyro servers deactivated: " + str(solver_manager))

            # If Stop signal arrives it tries to disconnect all mqtt clients
            for key, object in self.output.mqtt.items():
                object.MQTTExit()
                self.logger.debug("Client " + key + " is being disconnected")

            self.logger.info(return_msg)
            self.finish_status = True
            return return_msg
