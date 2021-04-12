import json
from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings

from .models import (Endpoint,
                     Device,
                     Status)

# View Functions
def api_base(request):
    return HttpResponse('Colheita-Feliz RESTful API v1')

def api_get_endpoints(request):
    if request.method != 'GET':
        return HttpResponse(status=405)

    query = Endpoint.objects.order_by('-last_seen')
    list_endpoints = [{'endpoint_id': ep.endpoint_id,
                       'name': ep.name,
                       'is_active': ep.is_active(),
                       'last_seen': get_tstamp(ep.last_seen),
                       'created': get_tstamp(ep.creation_time),
                       'modified': get_tstamp(ep.update_time)}
                      for ep in query]
    active_number = sum(1 for item in list_endpoints if item['is_active'])

    dict_payload = {'timezone':settings.TIME_ZONE,
                    'timestamp':get_tstamp(datetime.now()),
                    'total_number': len(list_endpoints),
                    'active_number': active_number,
                    'endpoints': list_endpoints}
    return JsonResponse(dict_payload,
                        json_dumps_params={'ensure_ascii': False})

def api_get_devices(request, endpoint_id):
    if request.method != 'GET':
        return HttpResponse(status=405)

    query = Device.objects.filter(endpoint_id=endpoint_id)
    if not query:
        return HttpResponse(status=204)

    list_devices = [{'device_id': dev.device_id,
                     'name': dev.name,
                     'description': dev.description,
                     'device_type': dev.get_device_type_display(),
                     'data_type': dev.get_data_type_display(),
                     'last_data': get_last_value(dev.device_id),
                     'unit': dev.unit,
                     'created': get_tstamp(dev.creation_time),
                     'modified': get_tstamp(dev.update_time)}
                    for dev in query]

    dict_payload = {'timezone':settings.TIME_ZONE,
                    'timestamp':get_tstamp(datetime.now()),
                    'total_number': len(list_devices),
                    'devices': list_devices}
    return JsonResponse(dict_payload,
                        json_dumps_params={'ensure_ascii': False})


def api_get_status(request, device_id):
    if request.method != 'GET':
        return HttpResponse(status=405)

    query = Status.objects.filter(device_id=device_id)\
                           .order_by('-send_time')[:1]
    if not query:
        return HttpResponse(status=204)

    status = query[0]
    dict_payload = {'status_id': status.status_id,
                    'measurement_timestamp': get_tstamp(status.send_time),
                    'value': status.value,}
    return JsonResponse(dict_payload,
                        json_dumps_params={'ensure_ascii': False})

def api_get_status_hour(request, device_id):
    if request.method != 'GET':
        return HttpResponse(status=405)

    query = Status.objects\
                  .filter(device_id=device_id,
                          send_time__gte=datetime.now()-timedelta(hours=1))\
                  .order_by('-send_time')
    return status_list_response(query)

def api_get_status_day(request, device_id):
    if request.method != 'GET':
        return HttpResponse(status=405)

    query = Status.objects\
                  .filter(device_id=device_id,
                          send_time__gte=datetime.now()-timedelta(days=1))\
                  .order_by('-send_time')
    return status_list_response(query)

def api_get_status_week(request, device_id):
    if request.method != 'GET':
        return HttpResponse(status=405)

    query = Status.objects\
                  .filter(device_id=device_id,
                          send_time__gte=datetime.now()-timedelta(days=7))\
                  .order_by('-send_time')
    return status_list_response(query)

def api_post_status(request):
    if request.method != 'POST':
        return HttpResponse(status=405)
    try:
        dict_payload = json.loads(request.body)
        print(dict_payload, type(dict_payload))
        UTC_offset = dict_payload['UTC_offset']
        timestamp = dict_payload['timestamp']
        endpoint_id = dict_payload['endpoint_id']
        name_reference = dict_payload['name_reference']
        samples = dict_payload['samples']
    except:
        return HttpResponse(status=400)

    try:
        UTC_offset = float(UTC_offset)
        if UTC_offset < -12.0 or UTC_offset > 14.0:
            raise
    except:
        return HttpResponse('Fix your UTC_offset', status=400)

    try:
        timestamp = float(timestamp)
        timestamp -= 3600*UTC_offset
        send_time = datetime.fromtimestamp(timestamp)
    except:
        return HttpResponse('Fix your timestamp', status=400)

    try:
        endpoint_id = int(endpoint_id)
    except:
        return HttpResponse('Irregular endpoint', status=400)

    if not Endpoint.objects.filter(endpoint_id=endpoint_id).exists():
        return HttpResponse('Unknown endpoint', status=400)

    try:
        name_reference = bool(name_reference)
    except:
        return HttpResponse('Fix your name_reference flag', status=400)

    Endpoint.objects.filter(endpoint_id=endpoint_id).update(last_seen=datetime.now())

    for sample in samples:
        print(sample, samples[sample])
        try:
            if name_reference:
                device = Device.objects.get(endpoint_id=endpoint_id,
                                            name=sample)
            else:
                device = Device.objects.get(device_id=sample)

            status = Status(value=samples[sample],
                            device_id=device,
                            send_time=send_time,
                            recept_time=datetime.now())
            status.save()
        except:
            pass

    return HttpResponse(status=200)


#Auxiliary Functions

def get_tstamp(dtime):
    if dtime:
        return round(datetime.timestamp(dtime), 3)
    else:
        return dtime

def get_last_value(device_id):
    q = Status.objects.filter(device_id=device_id)\
        .order_by('-send_time')[:1]
    if q:
        return q[0].value
    else:
        return None

def status_list_response(statuses):
    if not statuses:
        return HttpResponse(status=204)

    list_status = [{'status_id': status.status_id,
                    'measurement_timestamp': get_tstamp(status.send_time),
                    'value': status.value,}
                   for status in statuses]

    dict_payload = {'timezone':settings.TIME_ZONE,
                    'timestamp':get_tstamp(datetime.now()),
                    'total_number': len(list_status),
                    'status': list_status}
    return JsonResponse(dict_payload,
                        json_dumps_params={'ensure_ascii': False})
