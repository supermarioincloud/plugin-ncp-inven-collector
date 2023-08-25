import logging

from spaceone.core.connector import BaseConnector
import ncloud_server
from ncloud_server.api.v2_api import V2Api
from ncloud_server.rest import ApiException
import ncloud_apikey


class NaverCloudPlatformConnector(BaseConnector):
    naver_client_service = 'compute'
    version = 'v1'

    def __init__(self, *args, **kwargs):
        """
        kwargs
            - schema
            - options
            - secret_data

        secret_data(dict)
            - type: ..
            - project_id: ...
            - token_uri: ...
            - ...
        """

        super().__init__(*args, **kwargs)
        secret_data = kwargs.get('secret_data')
        self.project_id = secret_data.get('project_id')
        # self.credentials = google.oauth2.service_account.Credentials.from_service_account_info(secret_data)
        # self.client = googleapiclient.discovery.build(self.google_client_service,
        #                                               self.version,
        #                                               credentials=self.credentials)
        # ncp는 credentials 대신 api로 유저정보 저장한 다음 사용하는듯

        configuration = ncloud_server.Configuration()

        apikeys = ncloud_apikey.ncloud_key.NcloudKey().keys()
        configuration.access_key = apikeys['access_key']
        configuration.secret_key = apikeys['secret_key']

        self.api = V2Api(ncloud_server.ApiClient(configuration))

    # def verify(self, **kwargs):
    #     if self.api is None:
    #         self.set_connect(**kwargs)
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
