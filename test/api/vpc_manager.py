import unittest
import os
from datetime import datetime, timedelta
from unittest.mock import patch

from spaceone.core.unittest.runner import RichTestRunner

from spaceone.core.config import init_conf
from inventory.connector.vpc.vpc import VpcConnector

from inventory.manager.vpc.vpc_manager import VPCNetworkManager


class TestServerManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize configuration
        init_conf(package='src.inventory')

        secret_data = {
            "access_key": "Rd0XGiJWKewPXRN6ziic",
            "secret_key": "q0m7L8Dr8JX9BbbgTSSfPD3hZ1mdQoLGfJwgxzRg"
        }

        cls.vpc_connector = VpcConnector(config={},
                                         secret_data=secret_data, name='vpc')
        cls.vpc_manager = VPCNetworkManager()

        super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def test_list_snapshots(self):
        server_list = self.vpc_connector.get_list_vpc_instance()
        for server in server_list:
            print('=====')
            print(server)
            print('=====')

        secret_data = {
            "access_key": "Rd0XGiJWKewPXRN6ziic",
            "secret_key": "q0m7L8Dr8JX9BbbgTSSfPD3hZ1mdQoLGfJwgxzRg"
        }
        params = {'options': {}, 'secret_data': secret_data, 'filter': {}}
        virtual_networks = self.vpc_manager.collect_cloud_service(params)

        print(virtual_networks)
        '''
        for virtual_network in virtual_networks:
            print('=====')
            print(virtual_network.to_primitive())
            print('=====')
        '''


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)