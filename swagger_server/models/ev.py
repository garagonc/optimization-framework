# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Ev(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, battery_capacity_k_wh: float=None):  # noqa: E501
        """Ev - a model defined in Swagger

        :param battery_capacity_k_wh: The battery_capacity_k_wh of this Ev.  # noqa: E501
        :type battery_capacity_k_wh: float
        """
        self.swagger_types = {
            'battery_capacity_k_wh': float
        }

        self.attribute_map = {
            'battery_capacity_k_wh': 'Battery_Capacity_kWh'
        }

        self._battery_capacity_k_wh = battery_capacity_k_wh

    @classmethod
    def from_dict(cls, dikt) -> 'Ev':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ev of this Ev.  # noqa: E501
        :rtype: Ev
        """
        return util.deserialize_model(dikt, cls)

    @property
    def battery_capacity_k_wh(self) -> float:
        """Gets the battery_capacity_k_wh of this Ev.


        :return: The battery_capacity_k_wh of this Ev.
        :rtype: float
        """
        return self._battery_capacity_k_wh

    @battery_capacity_k_wh.setter
    def battery_capacity_k_wh(self, battery_capacity_k_wh: float):
        """Sets the battery_capacity_k_wh of this Ev.


        :param battery_capacity_k_wh: The battery_capacity_k_wh of this Ev.
        :type battery_capacity_k_wh: float
        """

        self._battery_capacity_k_wh = battery_capacity_k_wh
