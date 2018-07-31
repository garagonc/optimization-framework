import datetime
import json
import logging
import threading
from queue import Queue
import time

import os

from prediction.utils import Utils
from optimization.loadForecastPublisher import LoadForecastPublisher
from prediction.LSTMmodel import LSTMmodel
from prediction.modelPrediction import ModelPrediction
from prediction.processingData import ProcessingData
from prediction.rawDataReceiver import RawDataReceiver
from prediction.trainModel import TrainModel

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__file__)

class LoadPrediction(threading.Thread):

    def __init__(self, config, timesteps, horizon):
        super().__init__()
        self.stopRequest = threading.Event()

        self.length = timesteps
        self.length = 24
        self.horizon = horizon
        self.num_timesteps = 25
        self.hidden_size = 10
        self.batch_size = 1
        self.num_epochs = 1  # 10
        self.min_training_size = self.num_timesteps+10

        self.utils = Utils()
        self.raw_data_file_container = os.path.join("/usr/src/app", "prediction", "raw_data.csv")
        self.raw_data_file_host = os.path.join("/usr/src/app", "prediction/resources", "raw_data.csv")
        self.model_file_container = os.path.join("/usr/src/app", "prediction", "model.h5")
        self.model_file_host = os.path.join("/usr/src/app", "prediction/resources", "model.h5")
        self.utils.copy_files_from_host(self.raw_data_file_host, self.raw_data_file_container)
        self.utils.copy_files_from_host(self.model_file_host, self.model_file_container)

        raw_data_topic = config.get("IO", "raw.data.topic")
        raw_data_topic = json.loads(raw_data_topic)
        topics = [raw_data_topic]
        self.raw_data = RawDataReceiver(topics, config, self.num_timesteps, 24*10, self.raw_data_file_container)
        self.processingData = ProcessingData()

        self.q = Queue(maxsize=0)

        load_forecast_topic = config.get("IO", "load.forecast.topic")
        load_forecast_topic = json.loads(load_forecast_topic)
        self.load_forecast_pub = LoadForecastPublisher(load_forecast_topic, config, self.q, 60)
        self.load_forecast_pub.start()

        self.predicted_data = None

        self.lstmModel = LSTMmodel(self.num_timesteps, self.hidden_size, self.batch_size, self.model_file_container)
        self.trainModel = TrainModel(self.model_file_container)
        self.modelPrediction = ModelPrediction()

        self.train = False
        self.today = datetime.datetime.now().day
        self.copy_to_host_thread = threading.Thread()

    def run(self):
        while not self.stopRequest.is_set():
            model, created = self.lstmModel.model_setup()
            train = created or self.checktime()
            self.today = datetime.datetime.now()
            # get raw data from mqtt/zmq
            data = self.raw_data.get_raw_data(train)
            logger.debug("raw data ready " + str(len(data)))
            test_predictions = []
            if train:
                # preprocess data
                if len(data) > self.min_training_size:
                    Xtrain, Xtest, Ytrain, Ytest = self.processingData.preprocess_data(data, self.num_timesteps, True)

                    # train if required
                    self.trainModel.train(model, Xtrain, Ytrain, self.num_epochs, self.batch_size)
    
                    # evaluate if required
                    self.modelPrediction.evaluate(model, Xtest, Ytest, self.batch_size)
    
                    self.train = True

                    self.save_file_to_host()
            else:
                # preprocess data
                logger.info("len data = "+str(len(data)))
                Xtest = self.processingData.preprocess_data(data, self.num_timesteps, False)
                test_predictions = self.modelPrediction.predict_next_day(model, Xtest, self.batch_size, self.length)
                data = self.processingData.to_dict_with_datetime(test_predictions,
                                                                 datetime.datetime(datetime.datetime.now().year, 12, 11,
                                                                                   6, 0), 60)
                self.q.put(data)

            logger.debug("predictions "+str(test_predictions))

            time.sleep(1)
            # for testing

    def checktime(self):
        return (not self.train or datetime.datetime.now().day > self.today.day
        or datetime.datetime.now().month > self.today.month
        or datetime.datetime.now().year > self.today.year)

    def Stop(self):
        logger.info("start load controller thread exit")
        logger.info("Stopping load forecast thread")
        self.load_forecast_pub.Stop()
        self.stopRequest.set()
        if self.isAlive():
            self.join()
        logger.info("load controller thread exit")

    def save_file_to_host(self):
        self.utils.copy_files_to_host(self.raw_data_file_container, self.raw_data_file_host)
        pass