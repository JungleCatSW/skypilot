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
from sky.skylet.providers.cudo.cudo_client.swagger_client.api.api_keys_api import APIKeysApi  # noqa: E501
from sky.skylet.providers.cudo.cudo_client.swagger_client.rest import ApiException


class TestAPIKeysApi(unittest.TestCase):
    """APIKeysApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.api_keys_api.APIKeysApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_api_key(self):
        """Test case for delete_api_key

        Delete  # noqa: E501
        """
        pass

    def test_generate_api_key(self):
        """Test case for generate_api_key

        Generate  # noqa: E501
        """
        pass

    def test_list_api_keys(self):
        """Test case for list_api_keys

        List  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
