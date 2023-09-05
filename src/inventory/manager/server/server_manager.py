import logging
import time

from inventory.connector.server.server import ServerConnector
from inventory.libs.manager import NaverCloudManager
from inventory.libs.schema.base import ReferenceModel
from inventory.model.server.server.cloud_service import ServerInstanceResource, ServerInstanceResponse
from inventory.model.server.server.cloud_service_type import CLOUD_SERVICE_TYPES
from inventory.model.server.server.data import ServerInstance

_LOGGER = logging.getLogger(__name__)


class ServerManager(NaverCloudManager):
    connector_name = 'ServerConnector'
    cloud_service_types = CLOUD_SERVICE_TYPES

    def collect_cloud_service(self, params):
        """
        Args:
            params:
                - options
                - schema
                - secret_data
                - filter
                - zones
            Response:
                CloudServiceResponse/ErrorResourceResponse
        """
        _LOGGER.debug(f'** Server ServerInstance START **')

        start_time = time.time()
        collected_cloud_services = []
        error_responses = []
        schema_id = ""

        secret_data = params['secret_data']
        ##################################
        # 0. Gather All Related Resources
        # List all information through connector
        ##################################
        server_conn: ServerConnector = self.locator.get_connector(self.connector_name, **params)
        servers = server_conn.get_list_server_instance()

        for server in servers:
            try:
                ##################################
                # 1. Set Basic Information
                ##################################
                server_id = server.server_instance_no

                _name = server.server_name
                ##################################
                # 2. Make Base Data
                ##################################
                # server_data = ServerInstance(server)
                # print(server_data)
                server_data = {
                    'server_instance_no': server.server_instance_no,
                    'server_name': server.server_name
                }

                print(server_data)


                ##################################
                # 3. Make Return Resource
                ##################################
                server_resource = ServerInstanceResource({
                    'name': _name,
                    'data': server_data
                })
                print(server_resource.name)

                ##################################
                # 4. Make Collected Region Code
                ##################################
                # self.set_region_code('global')

                ##################################
                # 5. Make Resource Response Object
                # List of LoadBalancingResponse Object
                ##################################
                collected_cloud_services.append(ServerInstanceResponse({'resource': server_resource}))

                print(collected_cloud_services[0]['resource']['name'])

            except Exception as e:
                _LOGGER.error(f'[collect_cloud_service] => {e}', exc_info=True)
                error_response = self.generate_resource_error_response(e, 'Server', 'Server', server_id)
                error_responses.append(error_response)

        _LOGGER.debug(f'** Server ServerInstance Finished {time.time() - start_time} Seconds **')
        return collected_cloud_services, error_responses



