# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ImageUrl(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, url: str=None):  # noqa: E501
        """ImageUrl - a model defined in Swagger

        :param url: The url of this ImageUrl.  # noqa: E501
        :type url: str
        """
        self.swagger_types = {
            'url': str
        }

        self.attribute_map = {
            'url': 'url'
        }

        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'ImageUrl':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ImageUrl of this ImageUrl.  # noqa: E501
        :rtype: ImageUrl
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self) -> str:
        """Gets the url of this ImageUrl.

        Publicly reachable URL of an image.  # noqa: E501

        :return: The url of this ImageUrl.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this ImageUrl.

        Publicly reachable URL of an image.  # noqa: E501

        :param url: The url of this ImageUrl.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url
