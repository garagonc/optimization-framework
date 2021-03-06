"""
Created on Jun 27 15:35 2018

@author: nishit
"""
import datetime
import json

from senml import senml

from IO.dataPublisher import DataPublisher
from IO.redisDB import RedisDB
from utils_intern.constants import Constants
from utils_intern.messageLogger import MessageLogger


class PVForecastPublisher(DataPublisher):

    def __init__(self, internal_topic_params, config, id, control_frequency, horizon_in_steps, dT_in_seconds, q):
        self.logger = MessageLogger.get_logger(__name__, id)
        self.pv_data = {}
        self.q = q
        self.control_frequency = control_frequency
        self.horizon_in_steps = horizon_in_steps
        self.dT_in_seconds = dT_in_seconds
        self.topic = "P_PV"
        self.redisDB = RedisDB()
        self.id = id
        try:
            super().__init__(True, internal_topic_params, config, control_frequency, id)
        except Exception as e:
            self.redisDB.set("Error mqtt" + self.id, True)
            self.logger.error(e)

    def get_data(self):
        #  check if new data is available
        if not self.redisDB.get_bool(Constants.get_data_flow_key(self.id)):
            return None
        self.logger.debug("Getting PV data from Queue")
        if not self.q.empty():
            try:
                new_data = self.q.get_nowait()
                self.logger.debug("new data "+str(new_data))
                self.q.task_done()
                self.pv_data = new_data
                self.logger.debug("extract pv data")
                data = self.convert_to_senml()
                return data
            except Exception:
                self.logger.error("Queue empty")
        else:
            self.logger.debug("PV Queue empty")
            return None

    def convert_to_senml(self):
        meas = []
        if len(self.pv_data) > 0:
            for row in self.pv_data:
                meas.append(self.get_senml_meas(float(row[1]), row[0]))
        doc = senml.SenMLDocument(meas)
        val = doc.to_json()
        return json.dumps(val)

    def get_senml_meas(self, value, time):
        if not isinstance(time, float):
            time = float(time.timestamp())
        meas = senml.SenMLMeasurement()
        meas.time = time
        meas.value = value
        meas.name = self.topic
        return meas

