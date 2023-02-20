# C. Write a lambda function which outputs scientific names when we
# provide input foodname. Hint - use query api

import json
import boto3
from boto3.dynamodb.conditions import Key, Attr



def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('FooD_DataBase')
    foodname=event.get("foodname")
 
 
    try: 
    
        response = table.query(
        KeyConditionExpression=Key('food_name').eq(foodname)
        )
        items = response['Items']
        scintific_name=items[0]['scientific_name']
        print(items)
        # print(type(items))
        # print()
        # print(type(scintific_name))
        # print("hgvuyf",scintific_name)
        print(f"scientific_name of {foodname}:{scintific_name}")
        
    except Exception as e:
        print("enter a valid food name")
