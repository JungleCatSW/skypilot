# coding: utf-8

"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from sky.skylet.providers.cudo.cudo_client.swagger_client.api.virtual_machines_api import VirtualMachinesApi  # noqa: E501
from sky.skylet.providers.cudo.cudo_client.swagger_client.rest import ApiException


class TestVirtualMachinesApi(unittest.TestCase):
    """VirtualMachinesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.virtual_machines_api.VirtualMachinesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_connect_vm(self):
        """Test case for connect_vm

        Connect via VNC  # noqa: E501
        """
        pass

    def test_count_vms(self):
        """Test case for count_vms

        Count  # noqa: E501
        """
        pass

    def test_create_private_vm_image(self):
        """Test case for create_private_vm_image

        Create private VM image  # noqa: E501
        """
        pass

    def test_create_vm(self):
        """Test case for create_vm

        Create virtual machine  # noqa: E501
        """
        pass

    def test_delete_private_vm_image(self):
        """Test case for delete_private_vm_image

        Delete private VM image  # noqa: E501
        """
        pass

    def test_get_private_vm_image(self):
        """Test case for get_private_vm_image

        Get private VM image  # noqa: E501
        """
        pass

    def test_get_vm(self):
        """Test case for get_vm

        Get  # noqa: E501
        """
        pass

    def test_list_private_vm_images(self):
        """Test case for list_private_vm_images

        List private VM images  # noqa: E501
        """
        pass

    def test_list_public_vm_images(self):
        """Test case for list_public_vm_images

        List public VM images  # noqa: E501
        """
        pass

    def test_list_vm_data_centers(self):
        """Test case for list_vm_data_centers

        List data centers  # noqa: E501
        """
        pass

    def test_list_vm_disks(self):
        """Test case for list_vm_disks

        List disks attached to VM  # noqa: E501
        """
        pass

    def test_list_vm_machine_types(self):
        """Test case for list_vm_machine_types

        List machine types  # noqa: E501
        """
        pass

    def test_list_vms(self):
        """Test case for list_vms

        List  # noqa: E501
        """
        pass

    def test_monitor_vm(self):
        """Test case for monitor_vm

        Monitor  # noqa: E501
        """
        pass

    def test_reboot_vm(self):
        """Test case for reboot_vm

        Reboot  # noqa: E501
        """
        pass

    def test_resize_vm(self):
        """Test case for resize_vm

        Resize vCPU and memory of VM  # noqa: E501
        """
        pass

    def test_start_vm(self):
        """Test case for start_vm

        Start  # noqa: E501
        """
        pass

    def test_stop_vm(self):
        """Test case for stop_vm

        Stop  # noqa: E501
        """
        pass

    def test_terminate_vm(self):
        """Test case for terminate_vm

        Terminate  # noqa: E501
        """
        pass

    def test_update_private_vm_image(self):
        """Test case for update_private_vm_image

        Update private VM image  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()