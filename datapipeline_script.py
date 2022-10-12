import logging
from venv import create
import boto3
import csv
import pandas as pd
from botocore.exceptions import ClientError
import os

bucket_name='datapipeline-20221012'
region = 'ap-south-1'

def read_csv_file_auth():
    data= {}
    with open('./rootkey.csv', encoding='utf-8') as csvdata:
        reader = csv.DictReader(csvdata)
        print(reader)
        for value in reader:
            print(value)
            key = value['Access key ID']
            print(key)
            key2 = value['Secret access key']
            print(key2)

def authenticating_server():
    try:
        os.system('''
        sudo apt install aws_cli
        pip3 install awscli.clidriver
        aws conmfigure
        ''')
    except ClientError as e:
        logging.error(e)
    return True

def create_bucket(bucket_name, region):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = { 'LocationConstraint': region }
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__=='__main__':
    # create_bucket(bucket_name, region)
    read_csv_file_auth()
    authenticating_server()