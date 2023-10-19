
import json


FILENAME = "cudo_tags.json"

def write_to_disk(data):
    with open(FILENAME, 'w') as file:
        json.dump(data, file)

def read_from_disk():
    try:
        with open(FILENAME,'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

def get_tags(vm_id):
    data = read_from_disk()
    if vm_id in data:
        return data[vm_id]
    else:
        return {}

def set_tags(vm_id, tags):
    data = read_from_disk()
    data[vm_id] = tags
    write_to_disk(data)