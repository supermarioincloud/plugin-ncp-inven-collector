MAX_WORKER = 20
SUPPORTED_RESOURCE_TYPE = ['inventory.CloudService', 'inventory.CloudServiceType', 'inventory.Region',
                           'inventory.ErrorResource']
SUPPORTED_FEATURES = ['garbage_collection']
SUPPORTED_SCHEDULES = ['hours']
FILTER_FORMAT = []
CLOUD_SERVICE_GROUP_MAP = {
    'Server': [
        'Server',
        'ServerManager',
        'BareMetalServer',
        'Storage',
        'Snapshot',
        'PublicIP',
        'InitScript',
        'NetworkInterface',
        'ACG',
        'FabricCluster'
    ],
    'Vpc': [
        'Vpc',
    ]
}
