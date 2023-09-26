from typing import Dict
import sky.skylet.providers.cudo.config as config

import sky.skylet.providers.cudo.cudo_client.swagger_client as client
from sky.skylet.providers.cudo.cudo_client.swagger_client.rest import ApiException

def launch(name: str,
           instance_type: str,
           region: str,
           api_key: str,
           ssh_key_name: str):
    """Launches an INSTANCE_TYPE instance in region REGION with given NAME.
    The instance_type refers to the type found in the catalog.


    API_KEY is a secret registered with FluffyCloud. It is per-user.

    SSH_KEY_NAME corresponds to a ssh key registered with FluffyCloud.
    After launching, the user can ssh into INSTANCE_TYPE with that ssh key.

    Returns INSTANCE_ID if successful, otherwise returns None.
    """
    print("cudo launch" + name)


def remove(instance_id: str, api_key: str):
    """Removes instance with given INSTANCE_ID."""
    print("cudo remove" + instance_id)


def set_tags(instance_id: str, tags: Dict, api_key: str):
    """Set tags for instance with given INSTANCE_ID."""
    print("cudo set tags" + instance_id)


def list_instances(api_key: str):
    """Lists instances associated with API_KEY.

    Returns a dictionary:
    {
        instance_id_1:
        {
            status: ...,
            tags: ...,
            name: ...,
            ip: ....
        },
        instance_id_2: {...},
        ...
    }
    """
    print("cudo list instances")

def get_client():
    configuration = client.Configuration()
    key, err = config.get_api_key()

    if err != None:
        return None, err

    configuration.api_key['Authorization'] = key
    # configuration.debug = True
    configuration.api_key_prefix['Authorization'] = 'Bearer'
    configuration.host = "https://rest.compute.cudo.org"

    sclient = client.ApiClient(configuration)
    vms_api_client = client.VirtualMachinesApi(sclient)
    return vms_api_client, None

