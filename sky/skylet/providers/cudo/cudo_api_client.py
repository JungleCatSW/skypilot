from typing import Dict
import random
import string
import sky.skylet.providers.cudo.config as config

import sky.skylet.providers.cudo.cudo_client.swagger_client as client
import sky.skylet.providers.cudo.config as cudo_config
import sky.skylet.providers.cudo.cudo_api_client as cudo_api
from sky.skylet.providers.cudo.cudo_client.swagger_client import Body8
from sky.skylet.providers.cudo.cudo_client.swagger_client import Disk

from sky.skylet.providers.cudo.cudo_client.swagger_client.rest import ApiException
def generate_random_string(length):
    # Define the characters to choose from
    characters = string.ascii_lowercase + string.digits

    # Generate a random string of the specified length
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string

def launch(name: str,
           instance_type: str,
           region: str,
           api_key: str,
           ssh_key: str):
    """

    Launches an INSTANCE_TYPE instance in region REGION with given NAME.
    The instance_type refers to the type found in the catalog.

    Returns INSTANCE_ID if successful, otherwise returns None.
    """
    # need a datacenter id ?

    disk = Disk(storage_class="STORAGE_CLASS_NETWORK", size_gib=50, id=generate_random_string(10)) #, disk_type=disk_type)
    key_source = "SSH_KEY_SOURCE_NONE" # SshKeySource()
    #You must specify a data center and machine type or a maximum price per hour.
    #standard
    #intel-haswell
    #epyc-rome-rtx-4000
    #intel-broadwell
    #epyc-milan-rtx-a5000

    request = Body8(ssh_key_source=key_source, custom_ssh_keys=[ssh_key],vm_id=name, machine_type='intel-broadwell',
                    data_center_id='gb-bournemouth-1', boot_disk_image_id='ubuntu-nvidia-docker',
                    memory_gib=8, vcpus=4, boot_disk=disk)


    try:
        project_id, e = cudo_config.get_project()
        c, e = cudo_api.get_client()
        vm = c.create_vm(project_id,request)
        return vm.to_dict()['id']
    except ApiException as e: # TODO what to do with errors ?
        raise e


def remove(instance_id: str, api_key: str):
    """Removes instance with given INSTANCE_ID."""
    print("cudo remove" + instance_id)


def set_tags(instance_id: str, tags: Dict, api_key: str):
    """Set tags for instance with given INSTANCE_ID."""
    print("cudo set tags" + instance_id)


def list_instances():
    try:
        project_id, e = cudo_config.get_project()
        c, e = cudo_api.get_client()
        vms = c.list_vms(project_id)
        instances = {}
        vms_dict = vms.to_dict()
        for vm in vms_dict['vms']:
            instance = {
                'status': vm['short_state'], # active_state, init_state, lcm_state, short_state
                'tags': [], #TODO add tags to API
                'name': vm['id'], # TODO check ip address for private networks
                'ip': vm['public_ip_address'] # public_ip_address, external_ip_address,
             }
            instances[vm['id']] = instance
        return instances
    except ApiException as e: # TODO what to do with errors ?
        raise e

def get_client():
    configuration = client.Configuration()
    key, err = config.get_api_key()

    if err != None:
        return None, err

    configuration.api_key['Authorization'] = key
    configuration.debug = True
    configuration.api_key_prefix['Authorization'] = 'Bearer'
    configuration.host = "https://rest.compute.cudo.org"

    sclient = client.ApiClient(configuration)
    vms_api_client = client.VirtualMachinesApi(sclient)
    return vms_api_client, None

