import os

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

cst_network = CloudServiceTypeResource()
cst_network.name = 'VPCNetworkManager'
cst_network.provider = 'Ncloud'
cst_network.group = 'Networking'
cst_network.service_code = 'Networking'
cst_network.is_primary = True
cst_network.labels = ['Vpc']
cst_network.tags = {
    'spaceone:icon': '',
    'spaceone:display_name': 'VPCNetwork'
}

cst_network._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('VPC name', 'data.vpc_list.vpc_name'),
        TextDyField.data_source('Vpc No', 'data.vpc_list.vpc_no'),
        '''
        TextDyField.data_source('Route No', 'data.vpc_list.vpc_no'),
        TextDyField.data_source('Subnet No', 'data.subnet_list.'),
        TextDyField.data_source('Network Peering Name', 'data.vpc_list.vpc_no'),
        '''
    ],

    search=[
        # SearchField.set(name='ID', key='data.vpc_list.vpc_no'),
        SearchField.set(name='Name', key='data.vpc_list.vpc_name'),
    ],

    widget=[
        CardWidget.set(**get_data_from_yaml(total_count_conf)),
        ChartWidget.set(**get_data_from_yaml(count_by_region_conf)),
        ChartWidget.set(**get_data_from_yaml(count_by_project_conf))
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_network}),
]