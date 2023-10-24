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


class ListProjectSshKeysResponse(object):
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
        'ssh_keys': 'list[SshKey]'
    }

    attribute_map = {
        'ssh_keys': 'sshKeys'
    }

    def __init__(self, ssh_keys=None, _configuration=None):  # noqa: E501
        """ListProjectSshKeysResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ssh_keys = None
        self.discriminator = None

        self.ssh_keys = ssh_keys

    @property
    def ssh_keys(self):
        """Gets the ssh_keys of this ListProjectSshKeysResponse.  # noqa: E501


        :return: The ssh_keys of this ListProjectSshKeysResponse.  # noqa: E501
        :rtype: list[SshKey]
        """
        return self._ssh_keys

    @ssh_keys.setter
    def ssh_keys(self, ssh_keys):
        """Sets the ssh_keys of this ListProjectSshKeysResponse.


        :param ssh_keys: The ssh_keys of this ListProjectSshKeysResponse.  # noqa: E501
        :type: list[SshKey]
        """
        if self._configuration.client_side_validation and ssh_keys is None:
            raise ValueError("Invalid value for `ssh_keys`, must not be `None`")  # noqa: E501

        self._ssh_keys = ssh_keys

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
        if issubclass(ListProjectSshKeysResponse, dict):
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
        if not isinstance(other, ListProjectSshKeysResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListProjectSshKeysResponse):
            return True

        return self.to_dict() != other.to_dict()