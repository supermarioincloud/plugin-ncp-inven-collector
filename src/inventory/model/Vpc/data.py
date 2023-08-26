from schematics import Model
from schematics.types import ModelType, ListType, StringType, IntType, DateTimeType, BooleanType
from spaceone.inventory.libs.schema.cloud_service import BaseResource


class Labels(Model):
    key = StringType()
    value = StringType()


class CommonCode(Model):
    code = StringType()
    code_name = StringType()


class NatGatewayInstance(Model):
    vpc_no = StringType()
    vpc_name = StringType()
    nat_gateway_instance_no = StringType()
    nat_gateway_name = StringType()
    public_ip = StringType()
    nat_gateway_instance_status = ModelType(CommonCode)
    nat_gateway_instance_status_name = StringType()
    nat_gateway_instance_operation = ModelType(CommonCode)
    create_date = StringType()
    nat_gateway_description = StringType()
    zone_code = StringType()


class NetworkAcl(Model):
    network_acl_no = StringType()
    network_acl_name = StringType()
    vpc_no = StringType()
    network_acl_status = ModelType(CommonCode)
    network_acl_description = StringType()
    create_date = StringType()
    is_default = BooleanType()


class RouteParameter(Model):
    destination_cidr_block = StringType()
    target_type_code = StringType()
    target_no = StringType()
    target_name = StringType()


class VpcPeeringInstance(Model):
    vpc_peering_instance_no = StringType()
    vpc_peering_name = StringType()
    region_code = StringType()
    create_date = StringType()
    last_modify_date = StringType()
    vpc_peering_instance_status = CommonCode()
    vpc_peering_instance_status_name = StringType()
    vpc_peering_instance_operation = CommonCode()
    source_vpc_no = StringType()
    source_vpc_name = StringType()
    source_vpc_ipv4_cidr_block = StringType()
    source_vpc_login_id = StringType()
    target_vpc_no = StringType()
    target_vpc_name = StringType()
    target_vpc_ipv4_cidr_block = StringType()
    target_vpc_login_id = StringType()
    vpc_peering_description = StringType()
    has_reverse_vpc_peering = BooleanType()
    is_between_accounts = BooleanType()
    reverse_vpc_peering_instance_no = StringType()


class Subnet(Model):
    subnet_no = StringType()
    vpc_no = StringType()
    zone_code = StringType()
    subnet_name = StringType()
    subnet = StringType()
    subnet_status = CommonCode()
    create_date = StringType()
    subnet_type = CommonCode()
    usage_type = CommonCode()
    network_acl_no = StringType()


class RouteTable(Model):
    route_table_no = StringType()
    route_table_name = StringType()
    region_code = StringType()
    vpc_no = StringType()
    supported_subnet_type = CommonCode()
    is_default = BooleanType()
    route_table_status = CommonCode()
    route_table_description = StringType()


class Route(Model):
    destination_cidr_block = StringType()
    target_name = StringType()
    route_table_no = StringType()
    target_type = CommonCode()
    target_no = StringType()
    is_default = BooleanType()


class VPCNetwork(Model):
    vpc_no = StringType()
    vpc_name = StringType()
    ipv4_cidr_block = StringType()
    vpc_status = CommonCode()
    region_code = StringType()
    create_date = StringType()
