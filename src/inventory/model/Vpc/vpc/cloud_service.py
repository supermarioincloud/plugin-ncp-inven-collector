from schematics.types import ModelType, StringType, PolyModelType
from inventory.libs.schema.metadata.dynamic_field import TextDyField, DateTimeDyField
from inventory.libs.schema.metadata.dynamic_layout import ItemDynamicLayout, TableDynamicLayout
from inventory.libs.schema.cloud_service import CloudServiceResource, CloudServiceResponse, CloudServiceMeta
from inventory.model.Vpc import VPCNetwork
'''
VPC Network
'''

# TAB - Bucket
vpc_network_detail_meta = ItemDynamicLayout.set_fields('VPC Network Details', fields=[
    TextDyField.data_source('Name', 'data.vpcList.vpcName'),
    TextDyField.data_source('Region code', 'data.vpcList.region_code'),
    TextDyField.data_source('Status', 'data.vpcList.vpcStatus'),
    TextDyField.data_source('Ipc4 Cidr Block', 'data.vpcList.ipv4CidrBlock'),
    DateTimeDyField.data_source('Creation Time', 'data.vpcList.createDate'),
])


vpc_network_subnets_meta = TableDynamicLayout.set_fields('Subnets', root_path='data.subnetList', fields=[
    TextDyField.data_source('Name', 'subnetName'),
    TextDyField.data_source('Region', 'zoneCode'),
    TextDyField.data_source('Subnet Status', 'subnetStatus'),
    TextDyField.data_source('Subnet Type', 'subnetType'),
    TextDyField.data_source('Gateway', 'networkAclNo'),
])


vpc_network_route_meta = TableDynamicLayout.set_fields('Routes', root_path='data.routeList', fields=[
    TextDyField.data_source('Name', 'targetName'),
    TextDyField.data_source('Destination IP Range', 'destinationCidrBlock'),
    TextDyField.data_source('Target number', 'targetNo'),
    TextDyField.data_source('Target type', 'targetTypeCode'),
    TextDyField.data_source('Route Table No', 'routeTableNo'),
])

vpc_network_acl_meta = TableDynamicLayout.set_fields('NetworkAcl',fields=[
    TextDyField.data_source('Name', 'data.networkAclName'),
    TextDyField.data_source('No', 'data.networkAclNo'),
    TextDyField.data_source('Description', 'data.networkAclDescription'),
    TextDyField.data_source('NetworkAcl Status', 'data.networkAclStatus'),
    TextDyField.data_source('Vpc No', 'data.vpcNo'),
])

vpc_network_gate_way_instance_meta = TableDynamicLayout.set_fields('Network Gateway Instance',root_path='data.natGatewayInstanceList', fields=[
    TextDyField.data_source('Name', 'natGatewayName'),
    TextDyField.data_source('No', 'natGatewayInstanceNo'),
    TextDyField.data_source('Description', 'publicIp'),
    TextDyField.data_source('NetworkAcl Status', 'natGatewayInstanceStatus'),
    TextDyField.data_source('NetworkAcl Status Name', 'natGatewayInstanceStatusName'),
    TextDyField.data_source('Vpc No', 'vpcNo'),
    TextDyField.data_source('Vpc Name', 'vpcName'),
])

vpc_network_peering_meta = TableDynamicLayout.set_fields('VPC Network Peering', root_path='data.vpcPeeringInstanceList', fields=[
    TextDyField.data_source('Name', 'sourceVpcName '),
    TextDyField.data_source('Description', ' vpcPeeringDescription'),
    TextDyField.data_source('Your CIDR block', 'sourceVpcIpv4CidrBlock'),
    TextDyField.data_source('Peered VPC Network', 'vpcPeeringInstanceNo'),
    TextDyField.data_source('Peered VPC Network Name', 'vpcPeeringName '),
    TextDyField.data_source('target User CIDR block', 'targetVpcIpv4CidrBlock'),
    TextDyField.data_source('target User ID', 'targetVpcLoginId'),
    TextDyField.data_source('your User ID', 'sourceVpcLoginId'),
    TextDyField.data_source('Status', 'vpcPeeringInstanceStatus'),
])

instance_template_meta = CloudServiceMeta.set_layouts([vpc_network_detail_meta,
                                                       vpc_network_subnets_meta,
                                                       vpc_network_acl_meta,
                                                       vpc_network_gate_way_instance_meta,
                                                       vpc_network_route_meta,
                                                       vpc_network_peering_meta])

class VPCResource(CloudServiceResource):
    cloud_service_group = StringType(default='Networking')


class VPCNetworkResource(VPCResource):
    cloud_service_type = StringType(default='VPCNetwork')
    data = ModelType(VPCNetwork)
    _metadata = ModelType(CloudServiceMeta, default=instance_template_meta, serialized_name='metadata')


class VPCNetworkResponse(CloudServiceResponse):
    resource = PolyModelType(VPCNetworkResource)