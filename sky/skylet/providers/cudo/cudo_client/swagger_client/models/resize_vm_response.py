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


class ResizeVMResponse(object):
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
        'vm': 'VM'
    }

    attribute_map = {
        'vm': 'vm'
    }

    def __init__(self, vm=None, _configuration=None):  # noqa: E501
        """ResizeVMResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._vm = None
        self.discriminator = None

        self.vm = vm

    @property
    def vm(self):
        """Gets the vm of this ResizeVMResponse.  # noqa: E501


        :return: The vm of this ResizeVMResponse.  # noqa: E501
        :rtype: VM
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """Sets the vm of this ResizeVMResponse.


        :param vm: The vm of this ResizeVMResponse.  # noqa: E501
        :type: VM
        """
        if self._configuration.client_side_validation and vm is None:
            raise ValueError("Invalid value for `vm`, must not be `None`")  # noqa: E501

        self._vm = vm

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
        if issubclass(ResizeVMResponse, dict):
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
        if not isinstance(other, ResizeVMResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResizeVMResponse):
            return True

        return self.to_dict() != other.to_dict()
