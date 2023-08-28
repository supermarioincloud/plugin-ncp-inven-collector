import logging
import ncloud_vserver
from ncloud_vserver.rest import ApiException
import ncloud_apikey

from src.inventory.libs.connector import NaverCloudConnector

__all__ = ['ServerConnector']
_LOGGER = logging.getLogger(__name__)


class ServerConnector(NaverCloudConnector):
    naver_client_service = 'server'
    version = 'v1'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_list_server_instance(self):
        instance_list = []

        get_server_instance_list_request = ncloud_vserver.GetServerInstanceListRequest()
        print('get_list_server_instance method 시작')
        try:
            api_response = self.api.get_server_instance_list(get_server_instance_list_request)
            print(api_response)

            for ServerInstance in api_response.get('server_instance_list', []):
                instance_list.append(ServerInstance)

            return instance_list
        except ApiException as e:
            print("Exception when calling V2Api->get_login_key_list: %s\n" % e)
