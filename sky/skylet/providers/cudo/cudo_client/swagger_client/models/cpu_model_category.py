# coding: utf-8

"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from sky.skylet.providers.cudo.cudo_client.swagger_client.configuration import Configuration


class CpuModelCategory(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'count_vm_available': 'int',
        'min_price_hr': 'Decimal',
        'name': 'str'
    }

    attribute_map = {
        'count_vm_available': 'countVmAvailable',
        'min_price_hr': 'minPriceHr',
        'name': 'name'
    }

    def __init__(self, count_vm_available=None, min_price_hr=None, name=None, _configuration=None):  # noqa: E501
        """CpuModelCategory - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count_vm_available = None
        self._min_price_hr = None
        self._name = None
        self.discriminator = None

        self.count_vm_available = count_vm_available
        self.min_price_hr = min_price_hr
        self.name = name

    @property
    def count_vm_available(self):
        """Gets the count_vm_available of this CpuModelCategory.  # noqa: E501


        :return: The count_vm_available of this CpuModelCategory.  # noqa: E501
        :rtype: int
        """
        return self._count_vm_available

    @count_vm_available.setter
    def count_vm_available(self, count_vm_available):
        """Sets the count_vm_available of this CpuModelCategory.


        :param count_vm_available: The count_vm_available of this CpuModelCategory.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and count_vm_available is None:
            raise ValueError("Invalid value for `count_vm_available`, must not be `None`")  # noqa: E501

        self._count_vm_available = count_vm_available

    @property
    def min_price_hr(self):
        """Gets the min_price_hr of this CpuModelCategory.  # noqa: E501


        :return: The min_price_hr of this CpuModelCategory.  # noqa: E501
        :rtype: Decimal
        """
        return self._min_price_hr

    @min_price_hr.setter
    def min_price_hr(self, min_price_hr):
        """Sets the min_price_hr of this CpuModelCategory.


        :param min_price_hr: The min_price_hr of this CpuModelCategory.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and min_price_hr is None:
            raise ValueError("Invalid value for `min_price_hr`, must not be `None`")  # noqa: E501

        self._min_price_hr = min_price_hr

    @property
    def name(self):
        """Gets the name of this CpuModelCategory.  # noqa: E501


        :return: The name of this CpuModelCategory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CpuModelCategory.


        :param name: The name of this CpuModelCategory.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CpuModelCategory, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CpuModelCategory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CpuModelCategory):
            return True

        return self.to_dict() != other.to_dict()
