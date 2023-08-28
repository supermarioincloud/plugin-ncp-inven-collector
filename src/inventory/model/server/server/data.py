from schematics.types import StringType, ModelType, IntType, ListType, BooleanType
from schematics import Model
from inventory.libs.schema.cloud_service import BaseResource


class CommonCode(Model):
    code = StringType()
    code_name = StringType()


class ServerInstance(BaseResource):
    server_instance_no = StringType(serialize_when_none=False)
    server_name = StringType(serialize_when_none=False)
    server_description = StringType(serialize_when_none=False)
    cpu_count = IntType(serialize_when_none=False)
    memory_size = IntType(serialize_when_none=False)
    platform_type = ModelType(CommonCode, serialize_when_none=False)
    login_key_name = StringType(serialize_when_none=False)
    public_ip_instance_no = StringType(serialize_when_none=False)
    public_ip = StringType(serialize_when_none=False)
    server_instance_status = ModelType(CommonCode, serialize_when_none=False)
    server_instance_operation = ModelType(CommonCode, serialize_when_none=False)
    server_instance_status_name = StringType(serialize_when_none=False)
    create_date = StringType(serialize_when_none=False)
    uptime = StringType(serialize_when_none=False)
    server_image_product_code = StringType(serialize_when_none=False)
    server_product_code = StringType(serialize_when_none=False)
    is_protect_server_termination = BooleanType(serialize_when_none=False)
    zone_code = StringType(serialize_when_none=False)
    region_code = StringType(serialize_when_none=False)
    vpc_no = StringType(serialize_when_none=False)
    subnet_no = StringType(serialize_when_none=False)
    network_interface_no_list = ListType(StringType(), default=[], serialize_when_none=False)
    init_script_no = StringType(serialize_when_none=False)
    server_instance_type = ModelType(CommonCode, serialize_when_none=False)
    base_block_storage_disk_type = ModelType(CommonCode, serialize_when_none=False)
    base_block_storage_disk_detail_type = ModelType(CommonCode, serialize_when_none=False)
    placement_group_no = StringType(serialize_when_none=False)


