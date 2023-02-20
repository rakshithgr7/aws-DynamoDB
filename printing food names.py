import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('FooD_DataBase')
    groupname=event.get("groupname")
    response = table.scan(
        FilterExpression=Attr('GROUP').eq(groupname)
    )
    items = response['Items']
    print(f"food names related to group name : {groupname}")
    p=1
    for i in items:
        
        print(p,i['food_name'])
        p=p+1