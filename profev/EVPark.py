import json
import os
import time
from utils_intern.messageLogger import MessageLogger

class EVPark:

    def __init__(self, id, path):
        self.logger = MessageLogger.get_logger(__name__, id)
        self.evs = {}
        self.chargers = {}
        self.total_charging_stations_power = 0
        self.persist_real_data_file = path


    def add_evs(self, evs_list):
        for ev in evs_list:
            if ev.ev_name in self.evs.keys():
                self.evs[ev.ev_name].update(ev.battery_capacity)
            else:
                self.evs[ev.ev_name] = ev
        self.logger.debug("EVs "+str(self.evs))


    def get_num_of_cars(self):
        return len(self.evs)

    # TODO: should it be calculated only for hosted evs?
    def get_vac_capacity(self):
        vac_capacity = 0
        for ev_name, ev in self.evs.items():
            vac_capacity += ev.battery_capacity
        return vac_capacity

    def add_chargers(self, chargers_list):
        for charger in chargers_list:
            self.validate_hosted_ev(charger)
            if charger.charger_id in self.chargers.keys():
                self.update_charger(charger, charger.charger_id)
            else:
                self.chargers[charger.charger_id] = charger
                self.total_charging_stations_power += charger.max_charging_power_kw

    def validate_hosted_ev(self, charger):
        if charger.hosted_ev is not None and charger.hosted_ev not in self.evs.keys():
            raise Exception("EV "+str(charger.hosted_ev)+" hosted on charger "+str(charger.charger_id)+" but not registered")

    def update_charger(self, charger, charger_id):
        if charger_id in self.chargers.keys():
            old_charger = self.chargers[charger_id]
            if charger.hosted_ev:
                old_charger.plug(charger.hosted_ev, charger.soc)
            elif old_charger.hosted_ev:
                old_charger.unplug()
            if charger.max_charging_power_kw:
                old_charger.max_charging_power_kw = charger.max_charging_power_kw

    def remove_ev(self, ev):
        pass

    def max_charge_power_calculator(self, charging_period):
        """
        Returns a dictionary "connections"
            keys: charger labels
            values: max charging power input to the connected car
        """

        connections = {}
        self.logger.info("evs : " + str(self.evs))
        self.logger.info("chargers : "+str(self.chargers))
        for key, charger in self.chargers.items():
            self.logger.debug(charger.get_dict())
            hosted_ev = charger.hosted_ev
            self.logger.info("ev "+str(hosted_ev) + " charger.soc "+str(charger.soc))
            if hosted_ev and not charger.soc == None:
                ev = self.evs[hosted_ev]
                battery_depth_of_discharge = (1 - charger.soc) * ev.battery_capacity * 3600 # max_charging_power_kw-sec

                charger_limit = charger.max_charging_power_kw
                car_limit = battery_depth_of_discharge / charging_period

                connections[key] = min(charger_limit, car_limit)

        return connections

    def get_hosted_ev(self, charger_id):
        if charger_id and charger_id in self.chargers.keys():
            return self.chargers[charger_id].hosted_ev

    def avg_battery_capacity(self):
        avg = 0
        for ev_id, ev in self.evs.items():
            avg += ev.battery_capacity
        avg = avg/len(self.evs)
        return avg

    def sum_battery_capacity(self):
        count = 0
        for key, charger in self.chargers.items():
            count = count + 1
        cap = 0
        count2=0
        for ev_id, ev in self.evs.items():
            cap += ev.battery_capacity
            count2 = count2 + 1
            #if count2 == count:
                #break
        return cap

    # TODO: include all evs for calculation
    def calculate_vac_soc_value(self, vac_soc_value_override=None):
        #default = 0.4
        vac_soc_value = 0
        all_soc_present = True
        sum_battery_cap = self.sum_battery_capacity()
        avg_battery_cap = self.avg_battery_capacity()
        self.logger.info(self.chargers.keys())
        self.logger.info(self.evs.keys())

        ev_data_from_file = None
        if os.path.exists(self.persist_real_data_file):
            ev_data_from_file = self.read_data(self.persist_real_data_file)

        # Poner aquí analsis de tiempo
        list_of_evs = []
        for ev_name in self.evs.keys():
            if not ev_data_from_file == None:
                self.evs[ev_name].set_soc(ev_data_from_file.get(ev_name))
            list_of_evs.append(ev_name)

        for key, charger in self.chargers.items():
            self.logger.info("charger "+str(key)+" hosting "+str(charger.hosted_ev))
            if charger.hosted_ev in self.evs.keys() and charger.plugged and charger.soc is not None:
                ev = self.evs[charger.hosted_ev]
                ev.set_soc(charger.soc)
                self.logger.info("inside "+str(ev.battery_capacity) + " charger.soc "+str(charger.soc))
                vac_soc_value += charger.soc * ev.battery_capacity
                if charger.hosted_ev in list_of_evs:
                    list_of_evs.remove(charger.hosted_ev)
                else:
                    self.logger.error("EV "+str(charger.hosted_ev)+" not existing or assigned to another charging station.")
            elif charger.hosted_ev in self.evs.keys() and not charger.plugged and charger.soc == None:
                self.logger.debug("Unplugging EV "+str(charger.hosted_ev))
                charger.unplug()
                ev = self.evs[charger.hosted_ev]
                vac_soc_value += ev.get_soc() * ev.battery_capacity
                if charger.hosted_ev in list_of_evs:
                    list_of_evs.remove(charger.hosted_ev)
                else:
                    self.logger.error("EV "+str(charger.hosted_ev)+" not existing or assigned to another charging station.")
            else:
                all_soc_present = False
                #vac_soc_value += default * avg_battery_cap
                #vac += avg_battery_cap
            """elif charger.soc is not None:
                            self.logger.debug("Charger.soc is not None: "+str(charger.soc))
                            vac_soc_value += charger.soc * avg_battery_cap
                            #vac += avg_battery_cap"""

        self.logger.debug("evs not connected "+str(list_of_evs))
        for ev_name in list_of_evs:
            vac_soc_value += self.evs[ev_name].get_soc() * self.evs[ev_name].battery_capacity
        vac_soc_value = vac_soc_value * 100 / sum_battery_cap
        self.logger.info("vac_soc_value " + str(vac_soc_value) + " " + str(sum_battery_cap))

        if not all_soc_present:
            #vac_soc_value = default
            self.logger.info("Not all soc values present so using default vac_soc_value of "+str(vac_soc_value))
        if vac_soc_value_override is not None:
            vac_soc_value = vac_soc_value_override
            self.logger.info("vac_soc_value_override to "+str(vac_soc_value_override))
        return vac_soc_value

    def charge_ev(self, p_ev, dT, single_ev):
        self.logger.debug("p_ev: "+str(p_ev) + " single_ev " + str(single_ev))
        socs = {}
        list_of_evs = []
        for ev_name in self.evs.keys():
            list_of_evs.append(ev_name)

        for key, charger in self.chargers.items():
            if key in p_ev.keys():
                self.logger.info("charging " + str(charger.__str__()))
                hosted_ev = charger.hosted_ev
                soc = charger.soc
                if hosted_ev in self.evs.keys() and charger.plugged:
                    new_soc = self.evs[hosted_ev].charge(soc, dT, p_ev[key])
                    if single_ev:
                        for ev, ev_value in self.evs.items():
                            ev_value.set_soc(new_soc)
                            if ev in list_of_evs:
                                list_of_evs.remove(ev)
                    self.logger.debug("new soc = "+str(new_soc))
                    charger.set_calculated_soc(new_soc)
                    self.logger.info("charged " + str(charger.__str__()))
                    socs[key] = new_soc
                    if not single_ev:
                        if hosted_ev in list_of_evs:
                            list_of_evs.remove(hosted_ev)
                elif hosted_ev in self.evs.keys() and not charger.plugged:
                    new_soc = self.evs[hosted_ev].discharge(soc, dT)
                    if single_ev:
                        for ev, ev_value in self.evs.items():
                            ev_value.set_soc(new_soc)
                            if ev in list_of_evs:
                                list_of_evs.remove(ev)
                    charger.set_calculated_soc(new_soc)
                    self.logger.info("Set new soc " + str(charger.__str__()))
                    if not single_ev:
                        if hosted_ev in list_of_evs:
                            list_of_evs.remove(hosted_ev)
                else:
                    self.logger.error("Charger "+str(charger.charger_id)+" does not have hosted ev")
            else:
                self.logger.info("discharging " + str(charger.__str__()))
                soc = charger.soc
                hosted_ev = charger.hosted_ev
                if hosted_ev in self.evs.keys():
                    self.logger.debug("soc before "+str(self.evs[hosted_ev].get_soc()))
                    if not charger.plugged:
                        new_soc = self.evs[hosted_ev].discharge(soc, dT)
                    else:
                        self.evs[hosted_ev].set_soc(soc)
                        new_soc = self.evs[hosted_ev].get_soc()
                    if single_ev:
                        for ev, ev_value in self.evs.items():
                            ev_value.set_soc(new_soc)
                            if ev in list_of_evs:
                                list_of_evs.remove(ev)
                    charger.set_calculated_soc(new_soc)
                    self.logger.info("discharged " + str(charger.__str__()))
                    socs[key] = new_soc
                    if not single_ev:
                        if hosted_ev in list_of_evs:
                            list_of_evs.remove(hosted_ev)
                else:
                    self.logger.error("Charger "+charger.charger_id+" does not have hosted ev")

        self.logger.debug("Reducing the soc for driving EVs")
        for ev_name in list_of_evs:
            self.logger.debug("Discharging "+str(ev_name))
            self.evs[ev_name].discharge(None, dT)
        dict_to_save = {}
        for ev_name in self.evs.keys():
            dict_to_save[ev_name] = self.evs[ev_name].get_soc()
            self.logger.debug("soc for "+str(ev_name)+" is "+str(self.evs[ev_name].get_soc()))
        dict_to_save["time"] = time.time()

        self.save_data(dict_to_save, self.persist_real_data_file)
        return socs

    def save_data(self, data, filepath):
        try:
            with open(filepath, "w") as f:
                f.write(json.dumps(data))
            self.logger.debug("EV data saved to: " + str(filepath))
        except Exception as e:
            self.logger.error("Read input file exception: " + str(e))


    def read_data(self, filepath):
        try:
            with open(filepath, "r") as file:
                data = file.read()
            return json.loads(data)
        except Exception as e:
            self.logger.error("Read input file exception: " + str(e))



    def single_ev_recharge(self):
        if len(self.chargers) == 1:
            for charger_id, charger in self.chargers.items():
                if charger.plugged:
                    return 1
        return 0

    def get_chargers_dict_list(self):
        charger_list = []
        for name, charger in self.chargers.items():
            charger_list.append(charger.get_dict())
        return charger_list