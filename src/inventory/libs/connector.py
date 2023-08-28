import logging

from spaceone.core.connector import BaseConnector
import ncloud_vserver
import ncloud_vpc
from ncloud_vserver.rest import ApiException
import ncloud_apikey


class NaverCloudConnector(BaseConnector):
    naver_client_service = 'server'
    version = 'v1'

    def __init__(self, *args, **kwargs):
        """
        kwargs
            - schema
            - options
            - secret_data
            - name

        secret_data(dict)
            - type: ..
            - project_id: ...
            - token_uri: ...
            - ...
        """

        super().__init__(*args, **kwargs)

        secret_data = kwargs.get('secret_data')
        name = kwargs.get('name')

        if name == 'vserver':
            configuration = ncloud_vserver.Configuration()
            configuration.access_key = secret_data.get('access_key')
            configuration.secret_key = secret_data.get('secret_key')
            self.api = ncloud_vserver.V2Api(ncloud_vserver.ApiClient(configuration))
        elif name == 'vpc':
            configuration = ncloud_vpc.Configuration()
            configuration.access_key = secret_data.get('access_key')
            configuration.secret_key = secret_data.get('secret_key')
            self.api = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))

    def verify(self, **kwargs):
        if self.api is None:
            self.set_connect(**kwargs)

    # 원래 확인하는 용도같은데 goole 라이브러리 메소드 중 하나같은데 ncp-sdk에는 이런거 없는듯 어떡하지? 더 찾아봐야지..

    def generate_query(self, **query):
        query.update({
            'project': self.project_id,
        })
        return query

    # 얘도 google sdk 요청보낼때 쓰이는 쿼리같은데 삭제해도 될듯

    def list_zones(self, **query):
        query = self.generate_query(**query)
        # result = self.client.zones().list(**query).execute()
        # return result.get('items', [])
        # zone 리스트 가져오는 거. 나중에 하자
