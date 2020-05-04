# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.mqtt import MQTT  # noqa: F401,E501
from swagger_server import util


class Source(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, mqtt: MQTT=None, option: str=None):  # noqa: E501
        """Source - a model defined in Swagger

        :param mqtt: The mqtt of this Source.  # noqa: E501
        :type mqtt: MQTT
        :param option: The option of this Source.  # noqa: E501
        :type option: str
        """
        self.swagger_types = {
            'mqtt': MQTT,
            'option': str
        }

        self.attribute_map = {
            'mqtt': 'mqtt',
            'option': 'option'
        }

        self._mqtt = mqtt
        self._option = option

    @classmethod
    def from_dict(cls, dikt) -> 'Source':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Source of this Source.  # noqa: E501
        :rtype: Source
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mqtt(self) -> MQTT:
        """Gets the mqtt of this Source.


        :return: The mqtt of this Source.
        :rtype: MQTT
        """
        return self._mqtt

    @mqtt.setter
    def mqtt(self, mqtt: MQTT):
        """Sets the mqtt of this Source.


        :param mqtt: The mqtt of this Source.
        :type mqtt: MQTT
        """

        self._mqtt = mqtt

    @property
    def option(self) -> str:
        """Gets the option of this Source.

        option of the type of input  # noqa: E501

        :return: The option of this Source.
        :rtype: str
        """
        return self._option

    @option.setter
    def option(self, option: str):
        """Sets the option of this Source.

        option of the type of input  # noqa: E501

        :param option: The option of this Source.
        :type option: str
        """
        allowed_values = ["predict", "preprocess", "event", "sampling", "pv_predict"]  # noqa: E501
        if option not in allowed_values:
            raise ValueError(
                "Invalid value for `option` ({0}), must be one of {1}"
                .format(option, allowed_values)
            )

        self._option = option
