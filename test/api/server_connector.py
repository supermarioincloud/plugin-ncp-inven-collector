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
from src.inventory.connector.server.server import ServerConnector
from src.inventory.libs.connector import NaverCloudConnector


class TestServerConnector(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize configuration
        init_conf(package='src.inventory')

        secret_data = {
            "access_key": "",
            "secret_key": ""
        }

        cls.server_connector = ServerConnector( config={},
                                               secret_data=secret_data)

        super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def test_list_servers(self):
        server_list = self.server_connector.get_list_server_instance()

        for server in server_list:
            print('=====')
            print(server)
            print('=====')

if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
