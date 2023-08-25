import logging
import ncloud_server
from ncloud_server.api.v2_api import V2Api
from ncloud_server.rest import ApiException
import ncloud_apikey

from inventory.libs.connector import NaverCloudPlatformConnector

__all__ = ['ServerConnector']
_LOGGER = logging.getLogger(__name__)


class ServerConnector(NaverCloudPlatformConnector):
    naver_client_service = 'server'
    version = 'v1'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def list_server_names(self, **query):
        schema_names = []
        query.update({'parent': self._make_parent()})

        get_server_instance_list_request = ncloud_server.GetServerInstanceListRequest()
        try:
            api_response = self.api.get_server_instance_list(get_server_instance_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_login_key_list: %s\n" % e)

        # 원래 google용
        # request = self.client.projects().schemas().list(**query)
        #
        # while request is not None:
        #     response = request.execute()
        #     schema_names = [schema['name'] for schema in response.get('schemas', [])]
        #     request = self.client.projects().schemas().list_next(previous_request=request, previous_response=response)
        # return schema_names

    def _make_parent(self):
        return f'projects/{self.project_id}'
