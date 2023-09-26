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


class Project(object):
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
        'billing_account_id': 'str',
        'create_by': 'str',
        'resource_count': 'int'
    }

    attribute_map = {
        'billing_account_id': 'billingAccountId',
        'create_by': 'createBy',
        'resource_count': 'resourceCount'
    }

    def __init__(self, billing_account_id=None, create_by=None, resource_count=None, _configuration=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._billing_account_id = None
        self._create_by = None
        self._resource_count = None
        self.discriminator = None

        self.billing_account_id = billing_account_id
        if create_by is not None:
            self.create_by = create_by
        if resource_count is not None:
            self.resource_count = resource_count

    @property
    def billing_account_id(self):
        """Gets the billing_account_id of this Project.  # noqa: E501


        :return: The billing_account_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._billing_account_id

    @billing_account_id.setter
    def billing_account_id(self, billing_account_id):
        """Sets the billing_account_id of this Project.


        :param billing_account_id: The billing_account_id of this Project.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and billing_account_id is None:
            raise ValueError("Invalid value for `billing_account_id`, must not be `None`")  # noqa: E501

        self._billing_account_id = billing_account_id

    @property
    def create_by(self):
        """Gets the create_by of this Project.  # noqa: E501


        :return: The create_by of this Project.  # noqa: E501
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this Project.


        :param create_by: The create_by of this Project.  # noqa: E501
        :type: str
        """

        self._create_by = create_by

    @property
    def resource_count(self):
        """Gets the resource_count of this Project.  # noqa: E501


        :return: The resource_count of this Project.  # noqa: E501
        :rtype: int
        """
        return self._resource_count

    @resource_count.setter
    def resource_count(self, resource_count):
        """Sets the resource_count of this Project.


        :param resource_count: The resource_count of this Project.  # noqa: E501
        :type: int
        """

        self._resource_count = resource_count

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
        if issubclass(Project, dict):
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
        if not isinstance(other, Project):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Project):
            return True

        return self.to_dict() != other.to_dict()
