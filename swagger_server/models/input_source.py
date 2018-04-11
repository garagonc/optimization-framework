# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ess import ESS  # noqa: F401,E501
from swagger_server.models.grid import Grid  # noqa: F401,E501
from swagger_server.models.load import Load  # noqa: F401,E501
from swagger_server.models.pv import PV  # noqa: F401,E501
from swagger_server.models.source import Source  # noqa: F401,E501
from swagger_server.models.weather import Weather  # noqa: F401,E501
from swagger_server import util


class InputSource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, load: Load=None, photovoltaic: PV=None, ess: ESS=None, grid: Grid=None, market: Source=None, weather: Weather=None):  # noqa: E501
        """InputSource - a model defined in Swagger

        :param load: The load of this InputSource.  # noqa: E501
        :type load: Load
        :param photovoltaic: The photovoltaic of this InputSource.  # noqa: E501
        :type photovoltaic: PV
        :param ess: The ess of this InputSource.  # noqa: E501
        :type ess: ESS
        :param grid: The grid of this InputSource.  # noqa: E501
        :type grid: Grid
        :param market: The market of this InputSource.  # noqa: E501
        :type market: Source
        :param weather: The weather of this InputSource.  # noqa: E501
        :type weather: Weather
        """
        self.swagger_types = {
            'load': Load,
            'photovoltaic': PV,
            'ess': ESS,
            'grid': Grid,
            'market': Source,
            'weather': Weather
        }

        self.attribute_map = {
            'load': 'load',
            'photovoltaic': 'photovoltaic',
            'ess': 'ESS',
            'grid': 'grid',
            'market': 'market',
            'weather': 'weather'
        }

        self._load = load
        self._photovoltaic = photovoltaic
        self._ess = ess
        self._grid = grid
        self._market = market
        self._weather = weather

    @classmethod
    def from_dict(cls, dikt) -> 'InputSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InputSource of this InputSource.  # noqa: E501
        :rtype: InputSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def load(self) -> Load:
        """Gets the load of this InputSource.


        :return: The load of this InputSource.
        :rtype: Load
        """
        return self._load

    @load.setter
    def load(self, load: Load):
        """Sets the load of this InputSource.


        :param load: The load of this InputSource.
        :type load: Load
        """

        self._load = load

    @property
    def photovoltaic(self) -> PV:
        """Gets the photovoltaic of this InputSource.


        :return: The photovoltaic of this InputSource.
        :rtype: PV
        """
        return self._photovoltaic

    @photovoltaic.setter
    def photovoltaic(self, photovoltaic: PV):
        """Sets the photovoltaic of this InputSource.


        :param photovoltaic: The photovoltaic of this InputSource.
        :type photovoltaic: PV
        """

        self._photovoltaic = photovoltaic

    @property
    def ess(self) -> ESS:
        """Gets the ess of this InputSource.


        :return: The ess of this InputSource.
        :rtype: ESS
        """
        return self._ess

    @ess.setter
    def ess(self, ess: ESS):
        """Sets the ess of this InputSource.


        :param ess: The ess of this InputSource.
        :type ess: ESS
        """

        self._ess = ess

    @property
    def grid(self) -> Grid:
        """Gets the grid of this InputSource.


        :return: The grid of this InputSource.
        :rtype: Grid
        """
        return self._grid

    @grid.setter
    def grid(self, grid: Grid):
        """Sets the grid of this InputSource.


        :param grid: The grid of this InputSource.
        :type grid: Grid
        """

        self._grid = grid

    @property
    def market(self) -> Source:
        """Gets the market of this InputSource.


        :return: The market of this InputSource.
        :rtype: Source
        """
        return self._market

    @market.setter
    def market(self, market: Source):
        """Sets the market of this InputSource.


        :param market: The market of this InputSource.
        :type market: Source
        """

        self._market = market

    @property
    def weather(self) -> Weather:
        """Gets the weather of this InputSource.


        :return: The weather of this InputSource.
        :rtype: Weather
        """
        return self._weather

    @weather.setter
    def weather(self, weather: Weather):
        """Sets the weather of this InputSource.


        :param weather: The weather of this InputSource.
        :type weather: Weather
        """

        self._weather = weather
