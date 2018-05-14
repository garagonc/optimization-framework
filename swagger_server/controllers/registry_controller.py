import connexion
import logging, os
from flask import json
import six

from swagger_server.models.input_source import InputSource  # noqa: E501
from swagger_server.models.output_source import OutputSource  # noqa: E501
from swagger_server import util


logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__file__)


def getFilePath(dir, file_name):
    # print(os.path.sep)
    # print(os.environ.get("HOME"))
    project_dir = os.path.dirname(os.path.realpath(__file__))
    data_file = os.path.join("/usr/src/app", dir, file_name)
    return data_file

def input_source(Input_Source):  # noqa: E501
    """Creates a new data source as input

     # noqa: E501

    :param InputSource: Data source to be created
    :type InputSource: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        logger.info("registry/input started")
        Input_Source = InputSource.from_dict(connexion.request.get_json())  # noqa: E501
        logger.info("This is the dictionary: " + Input_Source.to_str())
        # logger.info("This is the photovoltaic: "+Output_Source.photovoltaic.to_str())

        # ToDo Error checklist
        # if file is true then mqtt is false
        # limitation of qos
        # topic just base name
        # check with the model

        # Writes the registry/output to a txt file in ordner utils
        path = getFilePath("utils", "Input_registry.txt")
        with open(path, 'w') as outfile:
            json.dump(Input_Source, outfile, ensure_ascii=False)
        logger.info("registry/input saved into memory")

    return 'Operation succeded'



def output_source(Output_Source):  # noqa: E501
    """Creates a new data source as ouput

     # noqa: E501

    :param OutputSource: Output data source to be created
    :type OutputSource: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        logger.info("registry/output started")
        Output_Source = OutputSource.from_dict(connexion.request.get_json())  # noqa: E501

        logger.info("This is the dictionary: "+ Output_Source.to_str() )
        #logger.info("This is the photovoltaic: "+Output_Source.photovoltaic.to_str())

        #ToDo Error checklist
        # if file is true then mqtt is false
        # limitation of qos
        # topic just base name
        # check with the model

        #Writes the registry/output to a txt file in ordner utils
        path = getFilePath("utils", "Output_registry.txt")
        with open(path, 'w') as outfile:
            json.dump(Output_Source, outfile, ensure_ascii=False)
        logger.info("registry/output saved into memory")


    return 'Operation succeded'

def getDataJSON(object, key):
    data=json.dumps(object)
    data2=json.loads(data)
    return data2[key]