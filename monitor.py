"""
Created on Jan 28 16:28 2020

@author: nishit
"""

import configparser
from config.configUpdater import ConfigUpdater
from monitor.instanceMonitor import InstanceMonitor
import signal
import sys

from utils_intern.messageLogger import MessageLogger
#from IO.redisDB import RedisDB

def sigterm(x, y):
    print('SIGTERM received, time to leave.')
    #redisDB = RedisDB()
    monitor.Stop()
    #redisDB.set("End monitor", "True")



# Register the signal to the handler
signal.signal(signal.SIGTERM, sigterm)  # Used by this script

#redisDB = RedisDB()
#redisDB.set("End monitor", "False")
config = None
config_path = "/usr/src/app/monitor/resources/monitorConfig.properties"
config_path_default = "/usr/src/app/config/monitorConfig.properties"
ConfigUpdater.copy_config(config_path_default, config_path, True)

config = configparser.ConfigParser()
config.optionxform = str
config.read(config_path)
log_level = config.get("IO", "log.level", fallback="DEBUG")
logger = MessageLogger.set_and_get_logger_parent(id="", level=log_level)

monitor = InstanceMonitor(config)

if __name__ == '__main__':
    print("Monitor started")