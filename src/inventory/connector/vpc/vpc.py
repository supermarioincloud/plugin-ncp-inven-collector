import logging
import ncloud_vserver
import ncloud_vpc
from ncloud_vpc.rest import ApiException


from inventory.libs.connector import NaverCloudConnector

__all__ = ['VpcConnector']
_LOGGER = logging.getLogger(__name__)


class VpcConnector(NaverCloudConnector):
    naver_client_service = 'vpc'
    version = 'v1'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_list_vpc_instance(self):
        instance_list = []

        get_vpc_list_request = ncloud_vpc.GetVpcListRequest()
        print(get_vpc_list_request)
        print('get_list_server_instance method 시작')
        try:
            api_response = self.api.get_vpc_list(get_vpc_list_request)
            print(api_response)

            for VpcInstance in api_response.vpc_list:
                instance_list.append(VpcInstance)

            return instance_list
        except ApiException as e:
            print("Exception when calling V2Api->get_login_key_list: %s\n" % e)


