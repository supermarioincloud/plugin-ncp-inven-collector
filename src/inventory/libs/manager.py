import math
import json
import logging
import ipaddress
from urllib.parse import urlparse

from spaceone.core.manager import BaseManager
from inventory.libs.connector import NaverCloudConnector
from inventory.libs.schema.region import RegionResource, RegionResponse
from inventory.libs.schema.cloud_service import ErrorResourceResponse


_LOGGER = logging.getLogger(__name__)


class NaverCloudManager(BaseManager):
    connector_name = None
    cloud_service_types = []
    response_schema = None
    collected_region_codes = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def verify(self, options, secret_data, **kwargs):
        """ Check collector's status.
        """
        connector: NaverCloudConnector = NaverCloudConnector(secret_data=secret_data)
        connector.verify()

    def collect_cloud_service_type(self, params):
        options = params.get('options', {})

        for cloud_service_type in self.cloud_service_types:
            if 'service_code_mappers' in options:
                svc_code_maps = options['service_code_mappers']
                if getattr(cloud_service_type.resource, 'service_code') and \
                        cloud_service_type.resource.service_code in svc_code_maps:
                    cloud_service_type.resource.service_code = svc_code_maps[cloud_service_type.resource.service_code]

            if 'custom_asset_url' in options:
                _tags = cloud_service_type.resource.tags

                if 'spaceone:icon' in _tags:
                    _icon = _tags['spaceone:icon']
                    _tags['spaceone:icon'] = f'{options["custom_asset_url"]}/{_icon.split("/")[-1]}'

            yield cloud_service_type

    def collect_cloud_service(self, params) -> list:
        raise NotImplemented

    def collect_resources(self, params) -> list:
        total_resources = []

        try:
            # Collect Cloud Service Type
            total_resources.extend(self.collect_cloud_service_type(params))

            # Collect Cloud Service
            resources, error_resources = self.collect_cloud_service(params)
            total_resources.extend(resources)
            total_resources.extend(error_resources)

            # Collect Region
            # total_resources.extend(self.collect_region())

        except Exception as e:
            _LOGGER.error(f'[collect_resources] {e}', exc_info=True)
            error_resource_response = self.generate_error_response(e, self.cloud_service_types[0].resource.group,
                                                                   self.cloud_service_types[0].resource.name)
            total_resources.append(error_resource_response)

        return total_resources

    @staticmethod
    def generate_error_response(e, cloud_service_group, cloud_service_type):
        if type(e) is dict:
            error_resource_response = ErrorResourceResponse({
                'message': json.dumps(e),
                'resource': {
                    'cloud_service_group': cloud_service_group,
                    'cloud_service_type': cloud_service_type
                }})
        else:
            error_resource_response = ErrorResourceResponse({
                'message': str(e),
                'resource': {
                    'cloud_service_group': cloud_service_group,
                    'cloud_service_type': cloud_service_type
                }})

        return error_resource_response

    @staticmethod
    def generate_resource_error_response(e, cloud_service_group, cloud_service_type, resource_id):
        if type(e) is dict:
            error_resource_response = ErrorResourceResponse({
                'message': json.dumps(e),
                'resource': {
                    'cloud_service_group': cloud_service_group,
                    'cloud_service_type': cloud_service_type,
                    'resource_id': resource_id
                }})
        else:
            error_resource_response = ErrorResourceResponse({
                'message': str(e),
                'resource': {
                    'cloud_service_group': cloud_service_group,
                    'cloud_service_type': cloud_service_type,
                    'resource_id': resource_id
                }})
        return error_resource_response