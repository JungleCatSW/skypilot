import json

import sky.skylet.providers.cudo.cudo_api_client as cudo_api
from sky.clouds.service_catalog.common import get_catalog_path

VMS_CSV = 'cudo/vms.csv'

cudo_gpu_model = {
    'RTX 3080': '3080',
    'RTX A4000': 'A4000',
    'RTX A4500': 'A4500',
    'RTX A5000': 'A5000',
    'RTX A6000': 'A6000',
}

cudo_gpu_mem = {
    '3080': 12,
    'A4000': 16,
    'A4500': 20,
    'A5000': 24,
    'A6000': 48,
}

machine_specs = [
    {'vcpu': 2, 'mem': 4, 'gpu': 1, },
    {'vcpu': 4, 'mem': 8, 'gpu': 1, },
    {'vcpu': 8, 'mem': 16, 'gpu': 2, },
    {'vcpu': 16, 'mem': 32, 'gpu': 2, },
    {'vcpu': 32, 'mem': 64, 'gpu': 4, },
    {'vcpu': 64, 'mem': 128, 'gpu': 8, },
]


def cudo_gpu_to_skypilot_gpu(model):
    if model in cudo_gpu_model:
        return cudo_gpu_model[model]
    else:
        return model.replace('RTX ', '')


def skypilot_gpu_to_cudo_gpu(model):
    for key, value in cudo_gpu_model.items():
        if value == model:
            return key
    return model


def get_gpu_info(count, model):
    mem = cudo_gpu_mem[model]
    # {'Name': 'A4000', 'Manufacturer': 'NVIDIA', 'Count': 1.0, 'MemoryInfo': {'SizeInMiB': 16384}}], 'TotalGpuMemoryInMiB': 16384}"
    info = {'Gpus': [{
        'Name': model,
        'Manufacturer': 'NVIDIA',
        'Count': str(count)+'.0',
        'MemoryInfo': {'SizeInMiB': 1024*mem}}],
        'TotalGpuMemoryInMiB': 1024*mem*count}

    return '"'+json.dumps(info).replace('"',"'")+'"'


def update_prices():
    rows = []
    # machine_types = cudo_api.machine_types(get_cudo_gpu_model('A4000'), 1, 2, 4, 'se-smedjebacken-1')
    gpu_types = cudo_api.gpu_types()
    for gpu in gpu_types:
        for spec in machine_specs:
            accelerator_name = cudo_gpu_to_skypilot_gpu(gpu)
            mts = cudo_api.machine_types(gpu, spec['mem'], spec['vcpu'], spec['gpu'])
            for hc in mts['host_configs']:
                row = {'instance_type': hc['machine_type'],
                       'accelerator_name': accelerator_name,
                       'accelerator_count': str(spec['gpu']) + '.0',
                       'vcpus': str(spec['vcpu']),
                       'memory_gib': str(spec['mem']),
                       'price': hc['total_price_hr']['value'],
                       'region': hc['data_center_id'],
                       'gpu_info': get_gpu_info(spec['gpu'], accelerator_name),
                       'spot_price': hc['total_price_hr']['value'],
                       }
                rows.append(row)
    path = get_catalog_path(VMS_CSV)
    with open(path, 'w') as file:
        file.write('InstanceType,AcceleratorName,AcceleratorCount,vCPUs,MemoryGiB,Price,Region,GpuInfo,SpotPrice\n')
        for row in rows:
            data = [row['instance_type'],
                    row['accelerator_name'],
                    row['accelerator_count'],
                    row['vcpus'],
                    row['memory_gib'],
                    row['price'],
                    row['region'],
                    row['gpu_info'],
                    row['spot_price'],
                    ]
            file.write(",".join(data) + '\n')

    # mt = machine_types.to_dict()
    return
