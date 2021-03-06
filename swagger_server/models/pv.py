# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.meta_pv import MetaPV  # noqa: F401,E501
from swagger_server.models.source import Source  # noqa: F401,E501
from swagger_server import util


class PV(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, p_pv: Source=None, p_pv_r: Source=None, p_pv_s: Source=None, p_pv_t: Source=None, q_pv: Source=None, q_pv_r: Source=None, q_pv_s: Source=None, q_pv_t: Source=None, meta: MetaPV=None):  # noqa: E501
        """PV - a model defined in Swagger

        :param p_pv: The p_pv of this PV.  # noqa: E501
        :type p_pv: Source
        :param p_pv_r: The p_pv_r of this PV.  # noqa: E501
        :type p_pv_r: Source
        :param p_pv_s: The p_pv_s of this PV.  # noqa: E501
        :type p_pv_s: Source
        :param p_pv_t: The p_pv_t of this PV.  # noqa: E501
        :type p_pv_t: Source
        :param q_pv: The q_pv of this PV.  # noqa: E501
        :type q_pv: Source
        :param q_pv_r: The q_pv_r of this PV.  # noqa: E501
        :type q_pv_r: Source
        :param q_pv_s: The q_pv_s of this PV.  # noqa: E501
        :type q_pv_s: Source
        :param q_pv_t: The q_pv_t of this PV.  # noqa: E501
        :type q_pv_t: Source
        :param meta: The meta of this PV.  # noqa: E501
        :type meta: MetaPV
        """
        self.swagger_types = {
            'p_pv': Source,
            'p_pv_r': Source,
            'p_pv_s': Source,
            'p_pv_t': Source,
            'q_pv': Source,
            'q_pv_r': Source,
            'q_pv_s': Source,
            'q_pv_t': Source,
            'meta': MetaPV
        }

        self.attribute_map = {
            'p_pv': 'P_PV',
            'p_pv_r': 'P_PV_R',
            'p_pv_s': 'P_PV_S',
            'p_pv_t': 'P_PV_T',
            'q_pv': 'Q_PV',
            'q_pv_r': 'Q_PV_R',
            'q_pv_s': 'Q_PV_S',
            'q_pv_t': 'Q_PV_T',
            'meta': 'meta'
        }

        self._p_pv = p_pv
        self._p_pv_r = p_pv_r
        self._p_pv_s = p_pv_s
        self._p_pv_t = p_pv_t
        self._q_pv = q_pv
        self._q_pv_r = q_pv_r
        self._q_pv_s = q_pv_s
        self._q_pv_t = q_pv_t
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt) -> 'PV':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PV of this PV.  # noqa: E501
        :rtype: PV
        """
        return util.deserialize_model(dikt, cls)

    @property
    def p_pv(self) -> Source:
        """Gets the p_pv of this PV.


        :return: The p_pv of this PV.
        :rtype: Source
        """
        return self._p_pv

    @p_pv.setter
    def p_pv(self, p_pv: Source):
        """Sets the p_pv of this PV.


        :param p_pv: The p_pv of this PV.
        :type p_pv: Source
        """

        self._p_pv = p_pv

    @property
    def p_pv_r(self) -> Source:
        """Gets the p_pv_r of this PV.


        :return: The p_pv_r of this PV.
        :rtype: Source
        """
        return self._p_pv_r

    @p_pv_r.setter
    def p_pv_r(self, p_pv_r: Source):
        """Sets the p_pv_r of this PV.


        :param p_pv_r: The p_pv_r of this PV.
        :type p_pv_r: Source
        """

        self._p_pv_r = p_pv_r

    @property
    def p_pv_s(self) -> Source:
        """Gets the p_pv_s of this PV.


        :return: The p_pv_s of this PV.
        :rtype: Source
        """
        return self._p_pv_s

    @p_pv_s.setter
    def p_pv_s(self, p_pv_s: Source):
        """Sets the p_pv_s of this PV.


        :param p_pv_s: The p_pv_s of this PV.
        :type p_pv_s: Source
        """

        self._p_pv_s = p_pv_s

    @property
    def p_pv_t(self) -> Source:
        """Gets the p_pv_t of this PV.


        :return: The p_pv_t of this PV.
        :rtype: Source
        """
        return self._p_pv_t

    @p_pv_t.setter
    def p_pv_t(self, p_pv_t: Source):
        """Sets the p_pv_t of this PV.


        :param p_pv_t: The p_pv_t of this PV.
        :type p_pv_t: Source
        """

        self._p_pv_t = p_pv_t

    @property
    def q_pv(self) -> Source:
        """Gets the q_pv of this PV.


        :return: The q_pv of this PV.
        :rtype: Source
        """
        return self._q_pv

    @q_pv.setter
    def q_pv(self, q_pv: Source):
        """Sets the q_pv of this PV.


        :param q_pv: The q_pv of this PV.
        :type q_pv: Source
        """

        self._q_pv = q_pv

    @property
    def q_pv_r(self) -> Source:
        """Gets the q_pv_r of this PV.


        :return: The q_pv_r of this PV.
        :rtype: Source
        """
        return self._q_pv_r

    @q_pv_r.setter
    def q_pv_r(self, q_pv_r: Source):
        """Sets the q_pv_r of this PV.


        :param q_pv_r: The q_pv_r of this PV.
        :type q_pv_r: Source
        """

        self._q_pv_r = q_pv_r

    @property
    def q_pv_s(self) -> Source:
        """Gets the q_pv_s of this PV.


        :return: The q_pv_s of this PV.
        :rtype: Source
        """
        return self._q_pv_s

    @q_pv_s.setter
    def q_pv_s(self, q_pv_s: Source):
        """Sets the q_pv_s of this PV.


        :param q_pv_s: The q_pv_s of this PV.
        :type q_pv_s: Source
        """

        self._q_pv_s = q_pv_s

    @property
    def q_pv_t(self) -> Source:
        """Gets the q_pv_t of this PV.


        :return: The q_pv_t of this PV.
        :rtype: Source
        """
        return self._q_pv_t

    @q_pv_t.setter
    def q_pv_t(self, q_pv_t: Source):
        """Sets the q_pv_t of this PV.


        :param q_pv_t: The q_pv_t of this PV.
        :type q_pv_t: Source
        """

        self._q_pv_t = q_pv_t

    @property
    def meta(self) -> MetaPV:
        """Gets the meta of this PV.


        :return: The meta of this PV.
        :rtype: MetaPV
        """
        return self._meta

    @meta.setter
    def meta(self, meta: MetaPV):
        """Sets the meta of this PV.


        :param meta: The meta of this PV.
        :type meta: MetaPV
        """

        self._meta = meta
