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


class Body5(object):
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
        'snapshot_id': 'str',
        'vm_id': 'str'
    }

    attribute_map = {
        'snapshot_id': 'snapshotId',
        'vm_id': 'vmId'
    }

    def __init__(self, snapshot_id=None, vm_id=None, _configuration=None):  # noqa: E501
        """Body5 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._snapshot_id = None
        self._vm_id = None
        self.discriminator = None

        self.snapshot_id = snapshot_id
        self.vm_id = vm_id

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this Body5.  # noqa: E501


        :return: The snapshot_id of this Body5.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this Body5.


        :param snapshot_id: The snapshot_id of this Body5.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and snapshot_id is None:
            raise ValueError("Invalid value for `snapshot_id`, must not be `None`")  # noqa: E501

        self._snapshot_id = snapshot_id

    @property
    def vm_id(self):
        """Gets the vm_id of this Body5.  # noqa: E501


        :return: The vm_id of this Body5.  # noqa: E501
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this Body5.


        :param vm_id: The vm_id of this Body5.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and vm_id is None:
            raise ValueError("Invalid value for `vm_id`, must not be `None`")  # noqa: E501

        self._vm_id = vm_id

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
        if issubclass(Body5, dict):
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
        if not isinstance(other, Body5):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Body5):
            return True

        return self.to_dict() != other.to_dict()
