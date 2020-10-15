# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:04:01 2020

@author: gabriel.r.ash
"""

import requests
import boto3
import uuid
import time
import random
import json

#client = boto3.client('kinesis', region_name = '')
#partition_key = str(uuid.uuid4())

while True:
    r = requests.get('https://randomuser.me/api/?exc=login')
    data = json.dumps(r.json())
    # client.put_record(
    #     StreamName='',
    #     Data=data,
    #     PartitionKey=partition_key )
    print(data)
    time.sleep(random.uniform(0,1))