# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MetaGloablControl(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, global_target_weight: float=None, local_target_weight: float=None):  # noqa: E501
        """MetaGloablControl - a model defined in Swagger

        :param global_target_weight: The global_target_weight of this MetaGloablControl.  # noqa: E501
        :type global_target_weight: float
        :param local_target_weight: The local_target_weight of this MetaGloablControl.  # noqa: E501
        :type local_target_weight: float
        """
        self.swagger_types = {
            'global_target_weight': float,
            'local_target_weight': float
        }

        self.attribute_map = {
            'global_target_weight': 'GlobalTargetWeight',
            'local_target_weight': 'LocalTargetWeight'
        }

        self._global_target_weight = global_target_weight
        self._local_target_weight = local_target_weight

    @classmethod
    def from_dict(cls, dikt) -> 'MetaGloablControl':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The metaGloablControl of this MetaGloablControl.  # noqa: E501
        :rtype: MetaGloablControl
        """
        return util.deserialize_model(dikt, cls)

    @property
    def global_target_weight(self) -> float:
        """Gets the global_target_weight of this MetaGloablControl.


        :return: The global_target_weight of this MetaGloablControl.
        :rtype: float
        """
        return self._global_target_weight

    @global_target_weight.setter
    def global_target_weight(self, global_target_weight: float):
        """Sets the global_target_weight of this MetaGloablControl.


        :param global_target_weight: The global_target_weight of this MetaGloablControl.
        :type global_target_weight: float
        """

        self._global_target_weight = global_target_weight

    @property
    def local_target_weight(self) -> float:
        """Gets the local_target_weight of this MetaGloablControl.


        :return: The local_target_weight of this MetaGloablControl.
        :rtype: float
        """
        return self._local_target_weight

    @local_target_weight.setter
    def local_target_weight(self, local_target_weight: float):
        """Sets the local_target_weight of this MetaGloablControl.


        :param local_target_weight: The local_target_weight of this MetaGloablControl.
        :type local_target_weight: float
        """

        self._local_target_weight = local_target_weight
