"""
Created on Aug 17 13:36 2018

@author: nishit
"""
import configparser
import json
import logging

import os

import sys

from mock_data.mockGenericDataPublisher import MockGenericDataPublisher
from mock_data.mockPLoadDataPublisher import MockPLoadDataPublisher
from mock_data.mockSoCDataPublisher import MockSoCDataPublisher

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__file__)


class MockData:
    def __init__(self, config, load_forecast, soc_value, generic_topic_list):
        self.load_forecast = load_forecast
        self.soc_value = soc_value
        self.gereric_names = generic_topic_list
        self.config = config

    def startMockDataPublisherThreads(self):
        if self.config is not None:
            if self.load_forecast:
                raw_p_load_data_topic = self.config.get("IO", "raw.pload.data.topic")
                raw_p_load_data_topic = json.loads(raw_p_load_data_topic)
                self.mock_p_load_data = MockPLoadDataPublisher(raw_p_load_data_topic, self.config)
                self.mock_p_load_data.start()
            if self.soc_value:
                raw_soc_data_topic = self.config.get("IO", "raw.soc.data.topic")
                raw_soc_data_topic = json.loads(raw_soc_data_topic)
                self.mock_soc_data = MockSoCDataPublisher(raw_soc_data_topic, self.config)
                self.mock_soc_data.start()
            self.mock_generic_data = {}
            raw_generic_data_topic = self.config.get("IO", "raw.generic.data.topic", fallback=None)
            if raw_generic_data_topic is not None:
                raw_generic_data_topic = json.loads(raw_generic_data_topic)
                for generic_name in self.gereric_names:
                    generic_topic = raw_generic_data_topic.copy()
                    generic_topic["topic"] = generic_topic["topic"] + str(generic_name)
                    self.mock_generic_data[generic_name] = MockGenericDataPublisher(generic_topic, config, generic_name)
                    self.mock_generic_data[generic_name].start()

    def stopMockDataPublisherThreads(self):
        if self.load_forecast:
            logger.info("Stopping mock p load data thread")
            self.mock_p_load_data.Stop()
        if self.soc_value:
            logger.info("Stopping mock soc data thread")
            self.mock_soc_data.Stop()
        for generic_name, publisher in self.mock_generic_data.items():
            logger.info("Stopping mock " + generic_name + " data thread")
            publisher.Stop()


if __name__ == '__main__':
    logger.info("Starting mock data generation")
    # Creating an object of the configuration file (standard values)
    arglist = sys.argv
    logger.info("Arg list = " + str(arglist))
    load_forecast = False
    soc_value = False
    generic_topic_list = []
    for topic in arglist[1:]:
        if topic == "P_Load":
            load_forecast = True
        elif topic == "SoC_Value":
            soc_value = True
        else:
            generic_topic_list.append(topic)
    config = None
    try:
        config = configparser.RawConfigParser()
        data_file = os.path.join("/usr/src/app", "utils", "ConfigFile.properties")
        config.read(data_file)
    except Exception as e:
        logger.error(e)

    mockData = MockData(config, load_forecast, soc_value, generic_topic_list)
    mockData.startMockDataPublisherThreads()