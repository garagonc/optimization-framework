# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.meta_grid import MetaGrid  # noqa: F401,E501
from swagger_server import util


class Grid(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, meta: MetaGrid=None):  # noqa: E501
        """Grid - a model defined in Swagger

        :param meta: The meta of this Grid.  # noqa: E501
        :type meta: MetaGrid
        """
        self.swagger_types = {
            'meta': MetaGrid
        }

        self.attribute_map = {
            'meta': 'meta'
        }

        self._meta = meta

    @classmethod
    def from_dict(cls, dikt) -> 'Grid':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The grid of this Grid.  # noqa: E501
        :rtype: Grid
        """
        return util.deserialize_model(dikt, cls)

    @property
    def meta(self) -> MetaGrid:
        """Gets the meta of this Grid.


        :return: The meta of this Grid.
        :rtype: MetaGrid
        """
        return self._meta

    @meta.setter
    def meta(self, meta: MetaGrid):
        """Sets the meta of this Grid.


        :param meta: The meta of this Grid.
        :type meta: MetaGrid
        """

        self._meta = meta
