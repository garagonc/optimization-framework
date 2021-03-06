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

    def __init__(self, ess_min_so_c: float=None, ess_max_so_c: float=None, ess_capacity: float=None, ess_max_charge_power: float=None, ess_max_discharge_power: float=None, ess_charging_eff: float=None, ess_discharging_eff: float=None):  # noqa: E501
        """MetaESS - a model defined in Swagger

        :param ess_min_so_c: The ess_min_so_c of this MetaESS.  # noqa: E501
        :type ess_min_so_c: float
        :param ess_max_so_c: The ess_max_so_c of this MetaESS.  # noqa: E501
        :type ess_max_so_c: float
        :param ess_capacity: The ess_capacity of this MetaESS.  # noqa: E501
        :type ess_capacity: float
        :param ess_max_charge_power: The ess_max_charge_power of this MetaESS.  # noqa: E501
        :type ess_max_charge_power: float
        :param ess_max_discharge_power: The ess_max_discharge_power of this MetaESS.  # noqa: E501
        :type ess_max_discharge_power: float
        :param ess_charging_eff: The ess_charging_eff of this MetaESS.  # noqa: E501
        :type ess_charging_eff: float
        :param ess_discharging_eff: The ess_discharging_eff of this MetaESS.  # noqa: E501
        :type ess_discharging_eff: float
        """
        self.swagger_types = {
            'ess_min_so_c': float,
            'ess_max_so_c': float,
            'ess_capacity': float,
            'ess_max_charge_power': float,
            'ess_max_discharge_power': float,
            'ess_charging_eff': float,
            'ess_discharging_eff': float
        }

        self.attribute_map = {
            'ess_min_so_c': 'ESS_Min_SoC',
            'ess_max_so_c': 'ESS_Max_SoC',
            'ess_capacity': 'ESS_Capacity',
            'ess_max_charge_power': 'ESS_Max_Charge_Power',
            'ess_max_discharge_power': 'ESS_Max_Discharge_Power',
            'ess_charging_eff': 'ESS_Charging_Eff',
            'ess_discharging_eff': 'ESS_Discharging_Eff'
        }

        self._ess_min_so_c = ess_min_so_c
        self._ess_max_so_c = ess_max_so_c
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
    def ess_min_so_c(self) -> float:
        """Gets the ess_min_so_c of this MetaESS.


        :return: The ess_min_so_c of this MetaESS.
        :rtype: float
        """
        return self._ess_min_so_c

    @ess_min_so_c.setter
    def ess_min_so_c(self, ess_min_so_c: float):
        """Sets the ess_min_so_c of this MetaESS.


        :param ess_min_so_c: The ess_min_so_c of this MetaESS.
        :type ess_min_so_c: float
        """
        if ess_min_so_c is not None and ess_min_so_c > 1:  # noqa: E501
            raise ValueError("Invalid value for `ess_min_so_c`, must be a value less than or equal to `1`")  # noqa: E501
        if ess_min_so_c is not None and ess_min_so_c < 0:  # noqa: E501
            raise ValueError("Invalid value for `ess_min_so_c`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ess_min_so_c = ess_min_so_c

    @property
    def ess_max_so_c(self) -> float:
        """Gets the ess_max_so_c of this MetaESS.


        :return: The ess_max_so_c of this MetaESS.
        :rtype: float
        """
        return self._ess_max_so_c

    @ess_max_so_c.setter
    def ess_max_so_c(self, ess_max_so_c: float):
        """Sets the ess_max_so_c of this MetaESS.


        :param ess_max_so_c: The ess_max_so_c of this MetaESS.
        :type ess_max_so_c: float
        """
        if ess_max_so_c is not None and ess_max_so_c > 1:  # noqa: E501
            raise ValueError("Invalid value for `ess_max_so_c`, must be a value less than or equal to `1`")  # noqa: E501
        if ess_max_so_c is not None and ess_max_so_c < 0:  # noqa: E501
            raise ValueError("Invalid value for `ess_max_so_c`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ess_max_so_c = ess_max_so_c

    @property
    def ess_capacity(self) -> float:
        """Gets the ess_capacity of this MetaESS.


        :return: The ess_capacity of this MetaESS.
        :rtype: float
        """
        return self._ess_capacity

    @ess_capacity.setter
    def ess_capacity(self, ess_capacity: float):
        """Sets the ess_capacity of this MetaESS.


        :param ess_capacity: The ess_capacity of this MetaESS.
        :type ess_capacity: float
        """

        self._ess_capacity = ess_capacity

    @property
    def ess_max_charge_power(self) -> float:
        """Gets the ess_max_charge_power of this MetaESS.


        :return: The ess_max_charge_power of this MetaESS.
        :rtype: float
        """
        return self._ess_max_charge_power

    @ess_max_charge_power.setter
    def ess_max_charge_power(self, ess_max_charge_power: float):
        """Sets the ess_max_charge_power of this MetaESS.


        :param ess_max_charge_power: The ess_max_charge_power of this MetaESS.
        :type ess_max_charge_power: float
        """

        self._ess_max_charge_power = ess_max_charge_power

    @property
    def ess_max_discharge_power(self) -> float:
        """Gets the ess_max_discharge_power of this MetaESS.


        :return: The ess_max_discharge_power of this MetaESS.
        :rtype: float
        """
        return self._ess_max_discharge_power

    @ess_max_discharge_power.setter
    def ess_max_discharge_power(self, ess_max_discharge_power: float):
        """Sets the ess_max_discharge_power of this MetaESS.


        :param ess_max_discharge_power: The ess_max_discharge_power of this MetaESS.
        :type ess_max_discharge_power: float
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
        if ess_charging_eff is not None and ess_charging_eff > 1:  # noqa: E501
            raise ValueError("Invalid value for `ess_charging_eff`, must be a value less than or equal to `1`")  # noqa: E501
        if ess_charging_eff is not None and ess_charging_eff < 0:  # noqa: E501
            raise ValueError("Invalid value for `ess_charging_eff`, must be a value greater than or equal to `0`")  # noqa: E501

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
        if ess_discharging_eff is not None and ess_discharging_eff > 1:  # noqa: E501
            raise ValueError("Invalid value for `ess_discharging_eff`, must be a value less than or equal to `1`")  # noqa: E501
        if ess_discharging_eff is not None and ess_discharging_eff < 0:  # noqa: E501
            raise ValueError("Invalid value for `ess_discharging_eff`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ess_discharging_eff = ess_discharging_eff
