import os
import json

from src import common


def response(status_code, payload):
    return {
        "statusCode": status_code,
        "body": json.dumps(payload) or "",
        # Regrettably, we need to add this CORS header ourselves
        # (the CloudFormation Global.Api.Cors setting is not enough).
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Content-Type': 'application/json'
        }
    }


## /blog endpoint
def get_all(event={}, context=None):
    print("getting", event)

    return response(*common.get_all())


def post(event, context=None):
    print("posting", event)
    body = json.loads(event["body"])

    return response(*common.post(body))


## /blog/{id} endpoint
def get(event, context=None):
    print("getting", event)
    id = event["pathParameters"].get("id")

    return response(*common.get(id))


def delete(event, context=None):
    print("deleting", event)
    id = event["pathParameters"].get("id")

    return response(*common.delete(id))

