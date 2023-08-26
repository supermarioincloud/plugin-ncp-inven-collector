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
    TextDyField.data_source('Description', 'data.description'),
    TextDyField.data_source('Maximum transmission unit', 'data.mtu'),
    TextDyField.data_source('Mode', 'data.subnet_creation_mode'),
    EnumDyField.data_source('Global Dynamic Routing', 'data.global_dynamic_route', default_state={
            'safe': ['On'],
            'warning': ['Off'],
    }),
    TextDyField.data_source('Dynamic Routing mode', 'data.dynamic_routing_mode'),
    DateTimeDyField.data_source('Creation Time', 'data.creation_timestamp'),
])

vpc_network_subnets_meta = TableDynamicLayout.set_fields('Subnets', root_path='data.subnetwork_data.subnets', fields=[
    TextDyField.data_source('Name', 'name'),
    TextDyField.data_source('Region', 'region'),
    TextDyField.data_source('Ip Address Ranges', 'ip_cidr_range'),
    TextDyField.data_source('Gateway', 'gateway_address'),
    TextDyField.data_source('Private Google Access', 'google_access'),
    TextDyField.data_source('Flow logs', 'flow_log'),
])

vpc_network_subnets_ip_address_meta = TableDynamicLayout.set_fields('Static Internal IP Addresses',
                                                                    root_path='data.ip_address_data', fields=[
    TextDyField.data_source('Name', 'name'),
    TextDyField.data_source('Internal Ip Address', 'address'),
    TextDyField.data_source('Subnetwork', 'subnet_name'),
    TextDyField.data_source('Region', 'region'),
    TextDyField.data_source('Version', 'ip_version_display'),
    ListDyField.data_source('In Used By', 'used_by'),
])


vpc_network_route_meta = TableDynamicLayout.set_fields('Routes', root_path='data.route_data.route', fields=[
    TextDyField.data_source('Name', 'name'),
    TextDyField.data_source('Description', 'description'),
    TextDyField.data_source('Destination IP Range', 'dest_range'),
    TextDyField.data_source('Priority', 'priority'),
    ListDyField.data_source('Instance Tags', 'tags',
                            default_badge={'type': 'outline', 'delimiter': '<br>'}),
    TextDyField.data_source('Next Hop', 'next_hop'),
])

vpc_network_peering_meta = TableDynamicLayout.set_fields('VPC Network Peering', root_path='data.peerings', fields=[
    TextDyField.data_source('Name', 'name'),
    TextDyField.data_source('Your VPC Network', 'display.your_network'),
    TextDyField.data_source('Peered VPC Network', 'display.peered_network'),
    TextDyField.data_source('Peered Project ID', 'display.project_id'),
    EnumDyField.data_source('Status', 'display.state_display', default_badge={
        'indigo.500': ['Active'], 'coral.600': ['Inactive']
    }),
    TextDyField.data_source('Exchange Custom Routes', 'display.ex_custom_route'),
    TextDyField.data_source('Exchange Subnet Routes With Public IP', 'display.ex_route_public_ip_display'),
])