import os
import unittest
import json

from spaceone.core.unittest.result import print_data
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.core import config
from spaceone.core import utils
from spaceone.core.transaction import Transaction
from spaceone.tester import TestCase, print_json


class TestCollector(TestCase):

    def test_init(self):
        v_info = self.inventory.Collector.init({'options': {}})
        print_json(v_info)

    def test_verify(self):
        options = {
        }
        secret_data = {
            "access_key": "Rd0XGiJWKewPXRN6ziic",
            "secret_key": "q0m7L8Dr8JX9BbbgTSSfPD3hZ1mdQoLGfJwgxzRg"
        }
        v_info = self.inventory.Collector.verify({'options': options, 'secret_data': secret_data})
        print_json(v_info)

    def test_collect(self):
        options = {}
        secret_data = {
            "access_key": "Rd0XGiJWKewPXRN6ziic",
            "secret_key": "q0m7L8Dr8JX9BbbgTSSfPD3hZ1mdQoLGfJwgxzRg"
        }
        filter = {}
        resource_stream = self.inventory.Collector.collect({'options': options, 'secret_data': secret_data,
                                                            'filter': filter})
        # print(resource_stream)

        for res in resource_stream:
            print_json(res)


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
