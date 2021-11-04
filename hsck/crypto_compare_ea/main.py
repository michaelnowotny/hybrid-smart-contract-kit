import json

from hsck.crypto_compare_ea.adapter import Adapter


def lambda_handler(event, context):
    adapter = Adapter(event)
    return adapter.result


def gcs_handler(request):
    adapter = Adapter(request.json)
    return json.dumps(adapter.result)
