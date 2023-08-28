import os

from inventory.conf.cloud_service_conf import *
from inventory.libs.common_parser import *
from inventory.libs.schema.metadata.dynamic_widget import CardWidget, ChartWidget
from inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, EnumDyField
from inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta
from inventory.conf.cloud_service_conf import *

current_dir = os.path.abspath(os.path.dirname(__file__))

total_count_conf = os.path.join(current_dir, 'widget/total_count.yml')
count_by_region_conf = os.path.join(current_dir, 'widget/count_by_region.yml')
count_by_project_conf = os.path.join(current_dir, 'widget/count_by_project.yml')

cst_server = CloudServiceTypeResource()
cst_server.name = 'Server'
cst_server.provider = 'naver_cloud'
cst_server.group = 'Server'
cst_server.service_code = 'Server'
cst_server.is_primary = True
cst_server.labels = ['Server']
cst_server.tags = {
    'spaceone:icon': '', #이미지없음
    'spaceone:display_name': 'Server'
}

cst_server._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Server ID', 'data.server_instance_no'),
        TextDyField.data_source('Server Name', 'data.server_name'),
        TextDyField.data_source('VPC ID', 'data.vpc_no'),
    ],
    search=[
        SearchField.set(name='Server Name', key='data.server_name')
    ],
    widget=[
        CardWidget.set(**get_data_from_yaml(total_count_conf)),
        ChartWidget.set(**get_data_from_yaml(count_by_region_conf)),
        ChartWidget.set(**get_data_from_yaml(count_by_project_conf))
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_server}),
]