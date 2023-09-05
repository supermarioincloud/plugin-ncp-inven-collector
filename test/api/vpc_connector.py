import unittest
import os
from datetime import datetime, timedelta
from unittest.mock import patch

from spaceone.core.unittest.result import print_data
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.core import config
from spaceone.core import utils
from spaceone.core.transaction import Transaction
from spaceone.core.config import init_conf
from inventory.connector.vpc.vpc import VpcConnector
from inventory.connector.server.server import ServerConnector
from inventory.libs.connector import NaverCloudConnector


class TestServerConnector(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize configuration
        init_conf(package='src.inventory')

        secret_data = {
            "access_key": "Rd0XGiJWKewPXRN6ziic",
            "secret_key": "q0m7L8Dr8JX9BbbgTSSfPD3hZ1mdQoLGfJwgxzRg"
        }

        cls.vpc_connector = VpcConnector(config={},
                                         secret_data=secret_data,name='vpc')

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


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
