# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.meta_load import MetaLoad  # noqa: F401,E501
from swagger_server.models.source import Source  # noqa: F401,E501
from swagger_server import util


class Load(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, forecast: bool=None, p_load: Source=None, q_load: Source=None, meta: MetaLoad=None):  # noqa: E501
        """Load - a model defined in Swagger

        :param forecast: The forecast of this Load.  # noqa: E501
        :type forecast: bool
        :param p_load: The p_load of this Load.  # noqa: E501
        :type p_load: Source
        :param q_load: The q_load of this Load.  # noqa: E501
        :type q_load: Source
        :param meta: The meta of this Load.  # noqa: E501
        :type meta: MetaLoad
        """
        self.swagger_types = {
            'forecast': bool,
            'p_load': Source,
            'q_load': Source,
            'meta': MetaLoad
        }

        self.attribute_map = {
            'forecast': 'Forecast',
            'p_load': 'P_Load',
            'q_load': 'Q_Load',
            'meta': 'meta'
        }

        self._forecast = forecast
        self._p_load = p_load
        self._q_load = q_load
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt) -> 'Load':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Load of this Load.  # noqa: E501
        :rtype: Load
        """
        return util.deserialize_model(dikt, cls)

    @property
    def forecast(self) -> bool:
        """Gets the forecast of this Load.

        Is it forecasted data? Or row data  # noqa: E501

        :return: The forecast of this Load.
        :rtype: bool
        """
        return self._forecast

    @forecast.setter
    def forecast(self, forecast: bool):
        """Sets the forecast of this Load.

        Is it forecasted data? Or row data  # noqa: E501

        :param forecast: The forecast of this Load.
        :type forecast: bool
        """
        if forecast is None:
            raise ValueError("Invalid value for `forecast`, must not be `None`")  # noqa: E501

        self._forecast = forecast

    @property
    def p_load(self) -> Source:
        """Gets the p_load of this Load.


        :return: The p_load of this Load.
        :rtype: Source
        """
        return self._p_load

    @p_load.setter
    def p_load(self, p_load: Source):
        """Sets the p_load of this Load.


        :param p_load: The p_load of this Load.
        :type p_load: Source
        """
        if p_load is None:
            raise ValueError("Invalid value for `p_load`, must not be `None`")  # noqa: E501

        self._p_load = p_load

    @property
    def q_load(self) -> Source:
        """Gets the q_load of this Load.


        :return: The q_load of this Load.
        :rtype: Source
        """
        return self._q_load

    @q_load.setter
    def q_load(self, q_load: Source):
        """Sets the q_load of this Load.


        :param q_load: The q_load of this Load.
        :type q_load: Source
        """

        self._q_load = q_load

    @property
    def meta(self) -> MetaLoad:
        """Gets the meta of this Load.


        :return: The meta of this Load.
        :rtype: MetaLoad
        """
        return self._meta

    @meta.setter
    def meta(self, meta: MetaLoad):
        """Sets the meta of this Load.


        :param meta: The meta of this Load.
        :type meta: MetaLoad
        """

        self._meta = meta
