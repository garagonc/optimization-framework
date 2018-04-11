# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MetaESS(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, min_so_c: int=None, max_so_c: int=None, ess_capacity: int=None, ess_max_charge_power: int=None, ess_max_discharge_power: int=None, ess_charging_eff: float=None, ess_discharging_eff: float=None):  # noqa: E501
        """MetaESS - a model defined in Swagger

        :param min_so_c: The min_so_c of this MetaESS.  # noqa: E501
        :type min_so_c: int
        :param max_so_c: The max_so_c of this MetaESS.  # noqa: E501
        :type max_so_c: int
        :param ess_capacity: The ess_capacity of this MetaESS.  # noqa: E501
        :type ess_capacity: int
        :param ess_max_charge_power: The ess_max_charge_power of this MetaESS.  # noqa: E501
        :type ess_max_charge_power: int
        :param ess_max_discharge_power: The ess_max_discharge_power of this MetaESS.  # noqa: E501
        :type ess_max_discharge_power: int
        :param ess_charging_eff: The ess_charging_eff of this MetaESS.  # noqa: E501
        :type ess_charging_eff: float
        :param ess_discharging_eff: The ess_discharging_eff of this MetaESS.  # noqa: E501
        :type ess_discharging_eff: float
        """
        self.swagger_types = {
            'min_so_c': int,
            'max_so_c': int,
            'ess_capacity': int,
            'ess_max_charge_power': int,
            'ess_max_discharge_power': int,
            'ess_charging_eff': float,
            'ess_discharging_eff': float
        }

        self.attribute_map = {
            'min_so_c': 'Min_SoC',
            'max_so_c': 'Max_SoC',
            'ess_capacity': 'ESS_Capacity',
            'ess_max_charge_power': 'ESS_Max_Charge_Power',
            'ess_max_discharge_power': 'ESS_Max_Discharge_Power',
            'ess_charging_eff': 'ESS_Charging_Eff',
            'ess_discharging_eff': 'ESS_Discharging_Eff'
        }

        self._min_so_c = min_so_c
        self._max_so_c = max_so_c
        self._ess_capacity = ess_capacity
        self._ess_max_charge_power = ess_max_charge_power
        self._ess_max_discharge_power = ess_max_discharge_power
        self._ess_charging_eff = ess_charging_eff
        self._ess_discharging_eff = ess_discharging_eff

    @classmethod
    def from_dict(cls, dikt) -> 'MetaESS':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The metaESS of this MetaESS.  # noqa: E501
        :rtype: MetaESS
        """
        return util.deserialize_model(dikt, cls)

    @property
    def min_so_c(self) -> int:
        """Gets the min_so_c of this MetaESS.


        :return: The min_so_c of this MetaESS.
        :rtype: int
        """
        return self._min_so_c

    @min_so_c.setter
    def min_so_c(self, min_so_c: int):
        """Sets the min_so_c of this MetaESS.


        :param min_so_c: The min_so_c of this MetaESS.
        :type min_so_c: int
        """

        self._min_so_c = min_so_c

    @property
    def max_so_c(self) -> int:
        """Gets the max_so_c of this MetaESS.


        :return: The max_so_c of this MetaESS.
        :rtype: int
        """
        return self._max_so_c

    @max_so_c.setter
    def max_so_c(self, max_so_c: int):
        """Sets the max_so_c of this MetaESS.


        :param max_so_c: The max_so_c of this MetaESS.
        :type max_so_c: int
        """

        self._max_so_c = max_so_c

    @property
    def ess_capacity(self) -> int:
        """Gets the ess_capacity of this MetaESS.


        :return: The ess_capacity of this MetaESS.
        :rtype: int
        """
        return self._ess_capacity

    @ess_capacity.setter
    def ess_capacity(self, ess_capacity: int):
        """Sets the ess_capacity of this MetaESS.


        :param ess_capacity: The ess_capacity of this MetaESS.
        :type ess_capacity: int
        """

        self._ess_capacity = ess_capacity

    @property
    def ess_max_charge_power(self) -> int:
        """Gets the ess_max_charge_power of this MetaESS.


        :return: The ess_max_charge_power of this MetaESS.
        :rtype: int
        """
        return self._ess_max_charge_power

    @ess_max_charge_power.setter
    def ess_max_charge_power(self, ess_max_charge_power: int):
        """Sets the ess_max_charge_power of this MetaESS.


        :param ess_max_charge_power: The ess_max_charge_power of this MetaESS.
        :type ess_max_charge_power: int
        """

        self._ess_max_charge_power = ess_max_charge_power

    @property
    def ess_max_discharge_power(self) -> int:
        """Gets the ess_max_discharge_power of this MetaESS.


        :return: The ess_max_discharge_power of this MetaESS.
        :rtype: int
        """
        return self._ess_max_discharge_power

    @ess_max_discharge_power.setter
    def ess_max_discharge_power(self, ess_max_discharge_power: int):
        """Sets the ess_max_discharge_power of this MetaESS.


        :param ess_max_discharge_power: The ess_max_discharge_power of this MetaESS.
        :type ess_max_discharge_power: int
        """

        self._ess_max_discharge_power = ess_max_discharge_power

    @property
    def ess_charging_eff(self) -> float:
        """Gets the ess_charging_eff of this MetaESS.


        :return: The ess_charging_eff of this MetaESS.
        :rtype: float
        """
        return self._ess_charging_eff

    @ess_charging_eff.setter
    def ess_charging_eff(self, ess_charging_eff: float):
        """Sets the ess_charging_eff of this MetaESS.


        :param ess_charging_eff: The ess_charging_eff of this MetaESS.
        :type ess_charging_eff: float
        """

        self._ess_charging_eff = ess_charging_eff

    @property
    def ess_discharging_eff(self) -> float:
        """Gets the ess_discharging_eff of this MetaESS.


        :return: The ess_discharging_eff of this MetaESS.
        :rtype: float
        """
        return self._ess_discharging_eff

    @ess_discharging_eff.setter
    def ess_discharging_eff(self, ess_discharging_eff: float):
        """Sets the ess_discharging_eff of this MetaESS.


        :param ess_discharging_eff: The ess_discharging_eff of this MetaESS.
        :type ess_discharging_eff: float
        """

        self._ess_discharging_eff = ess_discharging_eff
