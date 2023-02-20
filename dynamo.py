import csv
import boto3
import os

dynamodb = boto3.resource('dynamodb')


table_name="FooD_DataBase"
FILE_PATH = r"C:\Users\Rraks\Downloads\generic-food.csv"
table = dynamodb.Table(table_name)
if os.path.exists(FILE_PATH):
    with open(FILE_PATH, 'r', newline='') as CSV_FILE:
        DATA = csv.reader(CSV_FILE, delimiter=',')
        COLUMNS = next(DATA)#remove the header
        for EACH_ITEM in DATA:
            table.put_item(
                            Item={
                                    
                                     'food_name':EACH_ITEM[0]
                                    ,'scientific_name':EACH_ITEM[1]
                                    ,'GROUP':EACH_ITEM[2]
                                    ,'SUB_GROUP':EACH_ITEM[3]
                                }
                            )

