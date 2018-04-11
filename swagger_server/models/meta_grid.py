# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MetaGrid(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, p_grid_max_export_power: int=None, q_grid_max_export_power: int=None, max_voltage_drop: float=None, min_voltage_drop: float=None):  # noqa: E501
        """MetaGrid - a model defined in Swagger

        :param p_grid_max_export_power: The p_grid_max_export_power of this MetaGrid.  # noqa: E501
        :type p_grid_max_export_power: int
        :param q_grid_max_export_power: The q_grid_max_export_power of this MetaGrid.  # noqa: E501
        :type q_grid_max_export_power: int
        :param max_voltage_drop: The max_voltage_drop of this MetaGrid.  # noqa: E501
        :type max_voltage_drop: float
        :param min_voltage_drop: The min_voltage_drop of this MetaGrid.  # noqa: E501
        :type min_voltage_drop: float
        """
        self.swagger_types = {
            'p_grid_max_export_power': int,
            'q_grid_max_export_power': int,
            'max_voltage_drop': float,
            'min_voltage_drop': float
        }

        self.attribute_map = {
            'p_grid_max_export_power': 'P_Grid_Max_Export_Power',
            'q_grid_max_export_power': 'Q_Grid_Max_Export_Power',
            'max_voltage_drop': 'Max_Voltage_Drop',
            'min_voltage_drop': 'Min_Voltage_Drop'
        }

        self._p_grid_max_export_power = p_grid_max_export_power
        self._q_grid_max_export_power = q_grid_max_export_power
        self._max_voltage_drop = max_voltage_drop
        self._min_voltage_drop = min_voltage_drop

    @classmethod
    def from_dict(cls, dikt) -> 'MetaGrid':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The metaGrid of this MetaGrid.  # noqa: E501
        :rtype: MetaGrid
        """
        return util.deserialize_model(dikt, cls)

    @property
    def p_grid_max_export_power(self) -> int:
        """Gets the p_grid_max_export_power of this MetaGrid.


        :return: The p_grid_max_export_power of this MetaGrid.
        :rtype: int
        """
        return self._p_grid_max_export_power

    @p_grid_max_export_power.setter
    def p_grid_max_export_power(self, p_grid_max_export_power: int):
        """Sets the p_grid_max_export_power of this MetaGrid.


        :param p_grid_max_export_power: The p_grid_max_export_power of this MetaGrid.
        :type p_grid_max_export_power: int
        """

        self._p_grid_max_export_power = p_grid_max_export_power

    @property
    def q_grid_max_export_power(self) -> int:
        """Gets the q_grid_max_export_power of this MetaGrid.


        :return: The q_grid_max_export_power of this MetaGrid.
        :rtype: int
        """
        return self._q_grid_max_export_power

    @q_grid_max_export_power.setter
    def q_grid_max_export_power(self, q_grid_max_export_power: int):
        """Sets the q_grid_max_export_power of this MetaGrid.


        :param q_grid_max_export_power: The q_grid_max_export_power of this MetaGrid.
        :type q_grid_max_export_power: int
        """

        self._q_grid_max_export_power = q_grid_max_export_power

    @property
    def max_voltage_drop(self) -> float:
        """Gets the max_voltage_drop of this MetaGrid.


        :return: The max_voltage_drop of this MetaGrid.
        :rtype: float
        """
        return self._max_voltage_drop

    @max_voltage_drop.setter
    def max_voltage_drop(self, max_voltage_drop: float):
        """Sets the max_voltage_drop of this MetaGrid.


        :param max_voltage_drop: The max_voltage_drop of this MetaGrid.
        :type max_voltage_drop: float
        """

        self._max_voltage_drop = max_voltage_drop

    @property
    def min_voltage_drop(self) -> float:
        """Gets the min_voltage_drop of this MetaGrid.


        :return: The min_voltage_drop of this MetaGrid.
        :rtype: float
        """
        return self._min_voltage_drop

    @min_voltage_drop.setter
    def min_voltage_drop(self, min_voltage_drop: float):
        """Sets the min_voltage_drop of this MetaGrid.


        :param min_voltage_drop: The min_voltage_drop of this MetaGrid.
        :type min_voltage_drop: float
        """

        self._min_voltage_drop = min_voltage_drop
