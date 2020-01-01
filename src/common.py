import os
import json
import boto3


## Common functions, used by:
## - Lambda (directly mapped to API Gateway in CloudFormation)
## - Fargate (via Flask in fargate.py)


# Database setup
region = os.environ.get("AWS_REGION", "eu-west-1")
table_name = os.environ.get("TABLE_NAME", "ServerlessBlog")

dynamo = boto3.resource("dynamodb", region_name=region)
table = dynamo.Table(table_name)


# All functions return a Tuple (status_code:int, body:dict)

def get_all():
    try:
        result = table.scan()
        items = result.get("Items")
        return (200, items)
    except Exception as e:
        return (500, {"message": "Exception while getting item: " + str(e)})


def post(body):
    try:
        result = table.put_item(Item=body)
        print("result", result)

        return (200, {"message": "OK"})
    except Exception as e:
        return (500, {"message": "Exception during creation: " + str(e)})


def get(id):
    try:
        result = table.get_item(Key={"id": id})
        item = result.get("Item")

        return (200, item) if item else (404, {"message": "Item not found"})
    except Exception as e:
        return (500, {"message": "Exception while getting item: " + str(e)})


def delete(id):
    try:
        table.delete_item(Key={"id": id})
        return (200, {"message": "OK"})
    except Exception as e:
        return (500, {"message": "Exception during deletion: " + str(e)})

