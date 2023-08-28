from schematics.types import ModelType, StringType, PolyModelType
from inventory.libs.schema.metadata.dynamic_field import TextDyField, DateTimeDyField
from inventory.libs.schema.metadata.dynamic_layout import ItemDynamicLayout, TableDynamicLayout
from inventory.libs.schema.cloud_service import CloudServiceResource, CloudServiceResponse, CloudServiceMeta
from inventory.model.Vpc.vpc.data import VPCNetwork

'''
VPC Network
'''

# TAB - Bucket
vpc_network_detail_meta = TableDynamicLayout.set_fields('VPC Network Details', fields=[
    TextDyField.data_source('Name', 'data.vpc_list.vpcName'),
    TextDyField.data_source('Region code', 'data.vpc_list.region_code'),
    TextDyField.data_source('Status', 'data.vpcList.vpc_status'),
    TextDyField.data_source('Ipc4 Cidr Block', 'data.vpc_list.ipv4CidrBlock'),
    DateTimeDyField.data_source('Creation Time', 'data.vpc_list.createDate'),
])

vpc_network_subnets_meta = TableDynamicLayout.set_fields('Subnets', root_path='data.subnet_list', fields=[
    TextDyField.data_source('Name', 'subnet_name'),
    TextDyField.data_source('Region', 'zone_code'),
    TextDyField.data_source('Subnet Status', 'subnet_status'),
    TextDyField.data_source('Subnet Type', 'subnet_type'),
    TextDyField.data_source('Gateway', 'network_acl_no'),
])

vpc_network_route_meta = TableDynamicLayout.set_fields('Routes', root_path='data.route_list', fields=[
    TextDyField.data_source('Name', 'target_name'),
    TextDyField.data_source('Destination IP Range', 'destination_cidr_block'),
    TextDyField.data_source('Target number', 'target_no'),
    TextDyField.data_source('Target type', 'target_type_code'),
    TextDyField.data_source('Route Table No', 'route_table_mo'),
])

vpc_network_acl_meta = TableDynamicLayout.set_fields('NetworkAcl', fields=[
    TextDyField.data_source('Name', 'data.network_acl_name'),
    TextDyField.data_source('No', 'data.network_acl_no'),
    TextDyField.data_source('Description', 'data.network_acl_description'),
    TextDyField.data_source('NetworkAcl Status', 'data.network_acl_status'),
    TextDyField.data_source('Vpc No', 'data.vpc_no'),
])

vpc_network_gate_way_instance_meta = TableDynamicLayout.set_fields('Network Gateway Instance',
                                                                   root_path='data.nat_gateway_instance_list', fields=[
        TextDyField.data_source('Name', 'nat_gateway_name'),
        TextDyField.data_source('No', 'nat_gateway_instance_no'),
        TextDyField.data_source('Description', 'public_ip'),
        TextDyField.data_source('NetworkAcl Status', 'nat_gateway_instance_status'),
        TextDyField.data_source('NetworkAcl Status Name', 'nat_gateway_instance_status_name'),
        TextDyField.data_source('Vpc No', 'vpc_no'),
        TextDyField.data_source('Vpc Name', 'vpc_name'),
    ])

vpc_network_peering_meta = TableDynamicLayout.set_fields('VPC Network Peering', root_path='data.vpc_peering_instance_list',
                                                         fields=[
                                                             TextDyField.data_source('Name', 'source_vpc_name '),
                                                             TextDyField.data_source('Description',
                                                                                     ' vpc_peering_description'),
                                                             TextDyField.data_source('Your CIDR block',
                                                                                     'source_vpc_ipv4_cidr_block'),
                                                             TextDyField.data_source('Peered VPC Network',
                                                                                     'vpc_peering_instance_no'),
                                                             TextDyField.data_source('Peered VPC Network Name',
                                                                                     'vpc_peering_name '),
                                                             TextDyField.data_source('target User CIDR block',
                                                                                     'target_vpc_ipv4_cidr_block'),
                                                             TextDyField.data_source('target User ID',
                                                                                     'target_vpc_login_id'),
                                                             TextDyField.data_source('your User ID',
                                                                                     'source_vpc_login_id'),
                                                             TextDyField.data_source('Status',
                                                                                     'vpc_peering_instance_status'),
                                                         ])
'''
instance_template_meta = CloudServiceMeta.set_layouts([vpc_network_detail_meta,
                                                       vpc_network_subnets_meta,
                                                       vpc_network_acl_meta,
                                                       vpc_network_gate_way_instance_meta,
                                                       vpc_network_route_meta,
                                                       vpc_network_peering_meta])
'''
instance_template_meta = CloudServiceMeta.set_layouts([vpc_network_detail_meta])


class VPCResource(CloudServiceResource):
    cloud_service_group = StringType(default='Networking')


class VPCNetworkResource(VPCResource):
    cloud_service_type = StringType(default='VPCNetwork')
    data = ModelType(VPCNetwork)
    _metadata = ModelType(CloudServiceMeta, default=instance_template_meta, serialized_name='metadata')


class VPCNetworkResponse(CloudServiceResponse):
    resource = PolyModelType(VPCNetworkResource)
