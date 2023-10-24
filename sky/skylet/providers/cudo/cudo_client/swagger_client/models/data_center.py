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


class DataCenter(object):
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
        'id': 'str',
        'region_id': 'str',
        'renewable_energy': 'bool',
        'supplier_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'region_id': 'regionId',
        'renewable_energy': 'renewableEnergy',
        'supplier_name': 'supplierName'
    }

    def __init__(self, id=None, region_id=None, renewable_energy=None, supplier_name=None, _configuration=None):  # noqa: E501
        """DataCenter - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._region_id = None
        self._renewable_energy = None
        self._supplier_name = None
        self.discriminator = None

        self.id = id
        self.region_id = region_id
        self.renewable_energy = renewable_energy
        self.supplier_name = supplier_name

    @property
    def id(self):
        """Gets the id of this DataCenter.  # noqa: E501


        :return: The id of this DataCenter.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataCenter.


        :param id: The id of this DataCenter.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def region_id(self):
        """Gets the region_id of this DataCenter.  # noqa: E501


        :return: The region_id of this DataCenter.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this DataCenter.


        :param region_id: The region_id of this DataCenter.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

    @property
    def renewable_energy(self):
        """Gets the renewable_energy of this DataCenter.  # noqa: E501


        :return: The renewable_energy of this DataCenter.  # noqa: E501
        :rtype: bool
        """
        return self._renewable_energy

    @renewable_energy.setter
    def renewable_energy(self, renewable_energy):
        """Sets the renewable_energy of this DataCenter.


        :param renewable_energy: The renewable_energy of this DataCenter.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and renewable_energy is None:
            raise ValueError("Invalid value for `renewable_energy`, must not be `None`")  # noqa: E501

        self._renewable_energy = renewable_energy

    @property
    def supplier_name(self):
        """Gets the supplier_name of this DataCenter.  # noqa: E501


        :return: The supplier_name of this DataCenter.  # noqa: E501
        :rtype: str
        """
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, supplier_name):
        """Sets the supplier_name of this DataCenter.


        :param supplier_name: The supplier_name of this DataCenter.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and supplier_name is None:
            raise ValueError("Invalid value for `supplier_name`, must not be `None`")  # noqa: E501

        self._supplier_name = supplier_name

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
        if issubclass(DataCenter, dict):
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
        if not isinstance(other, DataCenter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataCenter):
            return True

        return self.to_dict() != other.to_dict()