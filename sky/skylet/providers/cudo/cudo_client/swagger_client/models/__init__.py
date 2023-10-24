# coding: utf-8

# flake8: noqa
"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.any import Any
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.api_key import ApiKey
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.attach_storage_disk_response import AttachStorageDiskResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.body import Body
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.body1 import Body1
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.body2 import Body2
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.body3 import Body3
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.body4 import Body4
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.body5 import Body5
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.body6 import Body6
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.body7 import Body7
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.body8 import Body8
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.connect_vm_response import ConnectVMResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.count_vms_response import CountVMsResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.cpu_model_category import CpuModelCategory
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.create_disk_snapshot_response import CreateDiskSnapshotResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.create_network_response import CreateNetworkResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.create_private_vm_image_response import CreatePrivateVMImageResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.create_security_group_response import CreateSecurityGroupResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.create_storage_disk_response import CreateStorageDiskResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.create_vm_request_nic import CreateVMRequestNIC
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.create_vm_response import CreateVMResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.data_center import DataCenter
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.data_center_category import DataCenterCategory
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.decimal import Decimal
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.delete_disk_snapshot_response import DeleteDiskSnapshotResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.delete_network_response import DeleteNetworkResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.delete_private_vm_image_response import DeletePrivateVMImageResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.delete_security_group_response import DeleteSecurityGroupResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.delete_storage_disk_response import DeleteStorageDiskResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.detach_storage_disk_response import DetachStorageDiskResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.disk import Disk
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.disk_type import DiskType
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.generate_api_key_request import GenerateApiKeyRequest
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.get_disk_response import GetDiskResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.get_network_response import GetNetworkResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.get_private_vm_image_response import GetPrivateVMImageResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.get_security_group_response import GetSecurityGroupResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.get_vm_response import GetVMResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.gpu_model_category import GpuModelCategory
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.host_config_category import HostConfigCategory
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.identity_verification_session import IdentityVerificationSession
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.image import Image
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_api_keys_response import ListApiKeysResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_disk_snapshots_response import ListDiskSnapshotsResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_disks_response import ListDisksResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_networks_response import ListNetworksResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_private_vm_images_response import ListPrivateVMImagesResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_private_vm_images_response_private_image import ListPrivateVMImagesResponsePrivateImage
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_project_ssh_keys_response import ListProjectSshKeysResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_projects_response import ListProjectsResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_public_vm_images_response import ListPublicVMImagesResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_regions_response import ListRegionsResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_security_groups_response import ListSecurityGroupsResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_ssh_keys_response import ListSshKeysResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_user_permissions_response import ListUserPermissionsResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_vm_data_centers_response import ListVMDataCentersResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_vm_disks_response import ListVMDisksResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_vm_machine_types_request import ListVMMachineTypesRequest
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_vm_machine_types_response import ListVMMachineTypesResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.list_vms_response import ListVMsResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.monitor_vm_response import MonitorVMResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.network import Network
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.profile import Profile
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.project import Project
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.protocol import Protocol
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.reboot_vm_response import RebootVMResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.region import Region
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.resize_vm_response import ResizeVMResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.revert_disk_response import RevertDiskResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.role import Role
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.rule import Rule
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.rule_type import RuleType
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.security_group import SecurityGroup
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.security_group1 import SecurityGroup1
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.security_group_rule import SecurityGroupRule
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.snapshot import Snapshot
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.ssh_key import SshKey
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.ssh_key_source import SshKeySource
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.start_network_response import StartNetworkResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.start_vm_response import StartVMResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.status import Status
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.stop_network_response import StopNetworkResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.stop_vm_response import StopVMResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.storage_class import StorageClass
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.terminate_vm_response import TerminateVMResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.update_private_vm_image_response import UpdatePrivateVMImageResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.update_security_group_response import UpdateSecurityGroupResponse
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.user_permission import UserPermission
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.v1_private_image import V1PrivateImage
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.vm import VM
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.vm_monitoring_item import VMMonitoringItem
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.vmnic import VMNIC
from sky.skylet.providers.cudo.cudo_client.swagger_client.models.v_router_size import VRouterSize