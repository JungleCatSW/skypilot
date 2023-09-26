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


class Body(object):
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
        'data_center_id': 'str',
        'project_id': 'str',
        'role': 'Role',
        'user_email': 'str'
    }

    attribute_map = {
        'data_center_id': 'dataCenterId',
        'project_id': 'projectId',
        'role': 'role',
        'user_email': 'userEmail'
    }

    def __init__(self, data_center_id=None, project_id=None, role=None, user_email=None, _configuration=None):  # noqa: E501
        """Body - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data_center_id = None
        self._project_id = None
        self._role = None
        self._user_email = None
        self.discriminator = None

        if data_center_id is not None:
            self.data_center_id = data_center_id
        if project_id is not None:
            self.project_id = project_id
        self.role = role
        self.user_email = user_email

    @property
    def data_center_id(self):
        """Gets the data_center_id of this Body.  # noqa: E501


        :return: The data_center_id of this Body.  # noqa: E501
        :rtype: str
        """
        return self._data_center_id

    @data_center_id.setter
    def data_center_id(self, data_center_id):
        """Sets the data_center_id of this Body.


        :param data_center_id: The data_center_id of this Body.  # noqa: E501
        :type: str
        """

        self._data_center_id = data_center_id

    @property
    def project_id(self):
        """Gets the project_id of this Body.  # noqa: E501


        :return: The project_id of this Body.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Body.


        :param project_id: The project_id of this Body.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def role(self):
        """Gets the role of this Body.  # noqa: E501


        :return: The role of this Body.  # noqa: E501
        :rtype: Role
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Body.


        :param role: The role of this Body.  # noqa: E501
        :type: Role
        """
        if self._configuration.client_side_validation and role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def user_email(self):
        """Gets the user_email of this Body.  # noqa: E501


        :return: The user_email of this Body.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this Body.


        :param user_email: The user_email of this Body.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_email is None:
            raise ValueError("Invalid value for `user_email`, must not be `None`")  # noqa: E501

        self._user_email = user_email

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
        if issubclass(Body, dict):
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
        if not isinstance(other, Body):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Body):
            return True

        return self.to_dict() != other.to_dict()
