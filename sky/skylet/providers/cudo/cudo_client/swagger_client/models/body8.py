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


class Body8(object):
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
        'boot_disk': 'Disk',
        'boot_disk_image_id': 'str',
        'cpu_model': 'str',
        'custom_ssh_keys': 'list[str]',
        'data_center_id': 'str',
        'gpu_model': 'str',
        'gpus': 'int',
        'machine_type': 'str',
        'max_price_hr': 'Decimal',
        'memory_gib': 'int',
        'nics': 'list[CreateVMRequestNIC]',
        'password': 'str',
        'security_group_ids': 'list[str]',
        'ssh_key_source': 'SshKeySource',
        'start_script': 'str',
        'storage_disk_ids': 'list[str]',
        'vcpus': 'int',
        'vm_id': 'str'
    }

    attribute_map = {
        'boot_disk': 'bootDisk',
        'boot_disk_image_id': 'bootDiskImageId',
        'cpu_model': 'cpuModel',
        'custom_ssh_keys': 'customSshKeys',
        'data_center_id': 'dataCenterId',
        'gpu_model': 'gpuModel',
        'gpus': 'gpus',
        'machine_type': 'machineType',
        'max_price_hr': 'maxPriceHr',
        'memory_gib': 'memoryGib',
        'nics': 'nics',
        'password': 'password',
        'security_group_ids': 'securityGroupIds',
        'ssh_key_source': 'sshKeySource',
        'start_script': 'startScript',
        'storage_disk_ids': 'storageDiskIds',
        'vcpus': 'vcpus',
        'vm_id': 'vmId'
    }

    def __init__(self, boot_disk=None, boot_disk_image_id=None, cpu_model=None, custom_ssh_keys=None, data_center_id=None, gpu_model=None, gpus=None, machine_type=None, max_price_hr=None, memory_gib=None, nics=None, password=None, security_group_ids=None, ssh_key_source=None, start_script=None, storage_disk_ids=None, vcpus=None, vm_id=None, _configuration=None):  # noqa: E501
        """Body8 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._boot_disk = None
        self._boot_disk_image_id = None
        self._cpu_model = None
        self._custom_ssh_keys = None
        self._data_center_id = None
        self._gpu_model = None
        self._gpus = None
        self._machine_type = None
        self._max_price_hr = None
        self._memory_gib = None
        self._nics = None
        self._password = None
        self._security_group_ids = None
        self._ssh_key_source = None
        self._start_script = None
        self._storage_disk_ids = None
        self._vcpus = None
        self._vm_id = None
        self.discriminator = None

        if boot_disk is not None:
            self.boot_disk = boot_disk
        self.boot_disk_image_id = boot_disk_image_id
        if cpu_model is not None:
            self.cpu_model = cpu_model
        if custom_ssh_keys is not None:
            self.custom_ssh_keys = custom_ssh_keys
        if data_center_id is not None:
            self.data_center_id = data_center_id
        if gpu_model is not None:
            self.gpu_model = gpu_model
        if gpus is not None:
            self.gpus = gpus
        if machine_type is not None:
            self.machine_type = machine_type
        if max_price_hr is not None:
            self.max_price_hr = max_price_hr
        if memory_gib is not None:
            self.memory_gib = memory_gib
        if nics is not None:
            self.nics = nics
        if password is not None:
            self.password = password
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if ssh_key_source is not None:
            self.ssh_key_source = ssh_key_source
        if start_script is not None:
            self.start_script = start_script
        if storage_disk_ids is not None:
            self.storage_disk_ids = storage_disk_ids
        if vcpus is not None:
            self.vcpus = vcpus
        self.vm_id = vm_id

    @property
    def boot_disk(self):
        """Gets the boot_disk of this Body8.  # noqa: E501


        :return: The boot_disk of this Body8.  # noqa: E501
        :rtype: Disk
        """
        return self._boot_disk

    @boot_disk.setter
    def boot_disk(self, boot_disk):
        """Sets the boot_disk of this Body8.


        :param boot_disk: The boot_disk of this Body8.  # noqa: E501
        :type: Disk
        """

        self._boot_disk = boot_disk

    @property
    def boot_disk_image_id(self):
        """Gets the boot_disk_image_id of this Body8.  # noqa: E501


        :return: The boot_disk_image_id of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._boot_disk_image_id

    @boot_disk_image_id.setter
    def boot_disk_image_id(self, boot_disk_image_id):
        """Sets the boot_disk_image_id of this Body8.


        :param boot_disk_image_id: The boot_disk_image_id of this Body8.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and boot_disk_image_id is None:
            raise ValueError("Invalid value for `boot_disk_image_id`, must not be `None`")  # noqa: E501

        self._boot_disk_image_id = boot_disk_image_id

    @property
    def cpu_model(self):
        """Gets the cpu_model of this Body8.  # noqa: E501


        :return: The cpu_model of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._cpu_model

    @cpu_model.setter
    def cpu_model(self, cpu_model):
        """Sets the cpu_model of this Body8.


        :param cpu_model: The cpu_model of this Body8.  # noqa: E501
        :type: str
        """

        self._cpu_model = cpu_model

    @property
    def custom_ssh_keys(self):
        """Gets the custom_ssh_keys of this Body8.  # noqa: E501


        :return: The custom_ssh_keys of this Body8.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_ssh_keys

    @custom_ssh_keys.setter
    def custom_ssh_keys(self, custom_ssh_keys):
        """Sets the custom_ssh_keys of this Body8.


        :param custom_ssh_keys: The custom_ssh_keys of this Body8.  # noqa: E501
        :type: list[str]
        """

        self._custom_ssh_keys = custom_ssh_keys

    @property
    def data_center_id(self):
        """Gets the data_center_id of this Body8.  # noqa: E501


        :return: The data_center_id of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._data_center_id

    @data_center_id.setter
    def data_center_id(self, data_center_id):
        """Sets the data_center_id of this Body8.


        :param data_center_id: The data_center_id of this Body8.  # noqa: E501
        :type: str
        """

        self._data_center_id = data_center_id

    @property
    def gpu_model(self):
        """Gets the gpu_model of this Body8.  # noqa: E501


        :return: The gpu_model of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._gpu_model

    @gpu_model.setter
    def gpu_model(self, gpu_model):
        """Sets the gpu_model of this Body8.


        :param gpu_model: The gpu_model of this Body8.  # noqa: E501
        :type: str
        """

        self._gpu_model = gpu_model

    @property
    def gpus(self):
        """Gets the gpus of this Body8.  # noqa: E501


        :return: The gpus of this Body8.  # noqa: E501
        :rtype: int
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        """Sets the gpus of this Body8.


        :param gpus: The gpus of this Body8.  # noqa: E501
        :type: int
        """

        self._gpus = gpus

    @property
    def machine_type(self):
        """Gets the machine_type of this Body8.  # noqa: E501


        :return: The machine_type of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type):
        """Sets the machine_type of this Body8.


        :param machine_type: The machine_type of this Body8.  # noqa: E501
        :type: str
        """

        self._machine_type = machine_type

    @property
    def max_price_hr(self):
        """Gets the max_price_hr of this Body8.  # noqa: E501


        :return: The max_price_hr of this Body8.  # noqa: E501
        :rtype: Decimal
        """
        return self._max_price_hr

    @max_price_hr.setter
    def max_price_hr(self, max_price_hr):
        """Sets the max_price_hr of this Body8.


        :param max_price_hr: The max_price_hr of this Body8.  # noqa: E501
        :type: Decimal
        """

        self._max_price_hr = max_price_hr

    @property
    def memory_gib(self):
        """Gets the memory_gib of this Body8.  # noqa: E501


        :return: The memory_gib of this Body8.  # noqa: E501
        :rtype: int
        """
        return self._memory_gib

    @memory_gib.setter
    def memory_gib(self, memory_gib):
        """Sets the memory_gib of this Body8.


        :param memory_gib: The memory_gib of this Body8.  # noqa: E501
        :type: int
        """

        self._memory_gib = memory_gib

    @property
    def nics(self):
        """Gets the nics of this Body8.  # noqa: E501


        :return: The nics of this Body8.  # noqa: E501
        :rtype: list[CreateVMRequestNIC]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this Body8.


        :param nics: The nics of this Body8.  # noqa: E501
        :type: list[CreateVMRequestNIC]
        """

        self._nics = nics

    @property
    def password(self):
        """Gets the password of this Body8.  # noqa: E501


        :return: The password of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Body8.


        :param password: The password of this Body8.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this Body8.  # noqa: E501


        :return: The security_group_ids of this Body8.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this Body8.


        :param security_group_ids: The security_group_ids of this Body8.  # noqa: E501
        :type: list[str]
        """

        self._security_group_ids = security_group_ids

    @property
    def ssh_key_source(self):
        """Gets the ssh_key_source of this Body8.  # noqa: E501


        :return: The ssh_key_source of this Body8.  # noqa: E501
        :rtype: SshKeySource
        """
        return self._ssh_key_source

    @ssh_key_source.setter
    def ssh_key_source(self, ssh_key_source):
        """Sets the ssh_key_source of this Body8.


        :param ssh_key_source: The ssh_key_source of this Body8.  # noqa: E501
        :type: SshKeySource
        """

        self._ssh_key_source = ssh_key_source

    @property
    def start_script(self):
        """Gets the start_script of this Body8.  # noqa: E501


        :return: The start_script of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._start_script

    @start_script.setter
    def start_script(self, start_script):
        """Sets the start_script of this Body8.


        :param start_script: The start_script of this Body8.  # noqa: E501
        :type: str
        """

        self._start_script = start_script

    @property
    def storage_disk_ids(self):
        """Gets the storage_disk_ids of this Body8.  # noqa: E501


        :return: The storage_disk_ids of this Body8.  # noqa: E501
        :rtype: list[str]
        """
        return self._storage_disk_ids

    @storage_disk_ids.setter
    def storage_disk_ids(self, storage_disk_ids):
        """Sets the storage_disk_ids of this Body8.


        :param storage_disk_ids: The storage_disk_ids of this Body8.  # noqa: E501
        :type: list[str]
        """

        self._storage_disk_ids = storage_disk_ids

    @property
    def vcpus(self):
        """Gets the vcpus of this Body8.  # noqa: E501


        :return: The vcpus of this Body8.  # noqa: E501
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this Body8.


        :param vcpus: The vcpus of this Body8.  # noqa: E501
        :type: int
        """

        self._vcpus = vcpus

    @property
    def vm_id(self):
        """Gets the vm_id of this Body8.  # noqa: E501


        :return: The vm_id of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this Body8.


        :param vm_id: The vm_id of this Body8.  # noqa: E501
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
        if issubclass(Body8, dict):
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
        if not isinstance(other, Body8):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Body8):
            return True

        return self.to_dict() != other.to_dict()
