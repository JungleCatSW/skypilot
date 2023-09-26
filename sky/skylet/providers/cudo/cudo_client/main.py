from __future__ import print_function
import time
import swagger_client
from sky.skylet.providers.cudo.cudo_client.swagger_client.rest import ApiException
from pprint import pprint


# Configure API key authorization: sso_auth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = '9fda3c8a5118d40d8129d4ff1603ee47db6f48a4d20488be45b2df92557b0be8'
configuration.debug = True
configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration.host = "https://rest.staging.compute.cudo.org"

sclient = swagger_client.ApiClient(configuration)
# create an instance of the API class
# api_instance = swagger_client.ProjectsApi(sclient)
vms_api = swagger_client.VirtualMachinesApi(sclient)

try:
    # Delete
    # api_response = api_instance.list_projects()
    # pprint(api_response)

    project_id = "long-term-test"
    vms = vms_api.list_vms(project_id)
    for i in vms.instances:
        pprint(i)
    pprint("done")
except ApiException as e:
    print("Exception when calling APIKeysApi->delete_api_key: %s\n" % e)