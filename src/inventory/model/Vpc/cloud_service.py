from schematics.types import ModelType, StringType, PolyModelType

from spaceone.inventory.model.networking.vpc_network.data import *
from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, EnumDyField, ListDyField, DateTimeDyField
from spaceone.inventory.libs.schema.metadata.dynamic_layout import ItemDynamicLayout, TableDynamicLayout
from spaceone.inventory.libs.schema.cloud_service import CloudServiceResource, CloudServiceResponse, CloudServiceMeta


'''
VPC Network
'''

# TAB - Bucket
vpc_network_detail_meta = ItemDynamicLayout.set_fields('VPC Network Details', fields=[
    TextDyField.data_source('Name', 'data.vpc_name'),
    TextDyField.data_source('Region code', 'data.region_code'),
    TextDyField.data_source('Status', 'data.vpc_status'),
    TextDyField.data_source('Ipc4 Cidr Block', 'data.ipv4_cidr_block'),
    DateTimeDyField.data_source('Creation Time', 'data.create_date'),
])

#root_path는 찍어봐야지 확정 지을수 있을듯
vpc_network_subnets_meta = TableDynamicLayout.set_fields('Subnets', root_path='data.subnetwork_data.subnets', fields=[
    TextDyField.data_source('Name', 'subnet_name'),
    TextDyField.data_source('Region', 'zone_code'),
    TextDyField.data_source('Subnet Status', 'subnet_status'),
    TextDyField.data_source('Gateway', 'network_acl_no'),
])


vpc_network_route_meta = TableDynamicLayout.set_fields('Routes', root_path='data.route_data.route', fields=[
    TextDyField.data_source('Name', 'target_name'),
    TextDyField.data_source('Destination IP Range', 'destination_cidr_block'),
    TextDyField.data_source('Target number', 'target_no'),
    TextDyField.data_source('Target type', 'target_type_code'),
])
#defaualt_badge도 commonCode가 찍히는거 보고 해야할듯
vpc_network_peering_meta = TableDynamicLayout.set_fields('VPC Network Peering', root_path='data.peerings', fields=[
    TextDyField.data_source('Name', 'source_vpc_name '),
    TextDyField.data_source('Description', ' vpc_peering_description'),
    TextDyField.data_source('Your VPC Network', 'source_vpc_ipv4_cidr_block'),
    TextDyField.data_source('Peered VPC Network', 'vpc_peering_instance_no'),
    TextDyField.data_source('Peered VPC Network Name', 'vpc_peering_name '),
    TextDyField.data_source('Peered Project ID', 'display.project_id'),
    EnumDyField.data_source('Status', 'vpc_peering_instance_status', default_badge={
        'indigo.500': ['Active'], 'coral.600': ['Inactive']
    }),
    TextDyField.data_source('Exchange Custom Routes', 'display.ex_custom_route'),
    TextDyField.data_source('Exchange Subnet Routes With Public IP', 'display.ex_route_public_ip_display'),
])