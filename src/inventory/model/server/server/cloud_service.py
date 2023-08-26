from schematics.types import ModelType, StringType, PolyModelType

from inventory.libs.schema.cloud_service import CloudServiceResource, CloudServiceResponse, CloudServiceMeta
from inventory.libs.schema.metadata.dynamic_field import TextDyField
from inventory.libs.schema.metadata.dynamic_layout import TableDynamicLayout
from inventory.model.server.server.data import ServerInstance

server_instance_details = TableDynamicLayout.set_fields('Server', root_path='data.subnetwork_data.subnets', fields=[
    TextDyField.data_source('Server ID', 'data.server_instance_no'),
    TextDyField.data_source('Server Name', 'data.server_name'),
    TextDyField.data_source('VPC ID', 'data.vpc_no'),
])

instance_template_meta = CloudServiceMeta.set_layouts([server_instance_details])


class ServerResource(CloudServiceResource):
    cloud_service_group = StringType(default='Server')


class ServerInstanceResource(ServerResource):
    cloud_service_type = StringType(default='Schema')
    data = ModelType(ServerInstance)
    _metadata = ModelType(CloudServiceMeta, default=instance_template_meta, serialized_name='metadata')


class SchemaResponse(CloudServiceResponse):
    resource = PolyModelType(ServerInstanceResource)
