import csv
import boto3
import os

dynamodb = boto3.resource('dynamodb')



table = dynamodb.create_table(
    TableName='FooD_DataBase',
    KeySchema=[
        {
            'AttributeName': 'food_name',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'scientific_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'food_name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'scientific_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

# Wait until the table exists.
table.wait_until_exists()

print(table.item_count)
print(list(dynamodb.tables.all()))