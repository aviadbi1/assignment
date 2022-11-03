import boto3
import json
import os
from handler import datetime_converter


endpoint_url = "http://localhost:4000"
aws_secret_access_key = 'xxx'
aws_access_key_id = 'xxx'


def read_regions_file():
    with open('regions.txt') as f:
        regions = f.read().strip().replace(" ","").split(",")
        print(regions)
        return regions

def get_aws_instances_per_region(region):
    ec2 = boto3.client('ec2', 
    	region_name = region, 
    	endpoint_url = endpoint_url,
    	aws_secret_access_key = aws_secret_access_key,
    	aws_access_key_id = aws_access_key_id)
    
    response = ec2.describe_instances()

    instances_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances_ids.append((instance['InstanceId'], instance['LaunchTime']))
    # if you want to print it
    #print(instances_ids)
    
    # sort the tuple that contains id and launchtime
    instances_ids.sort(key=lambda x: datetime_converter(x[1]))
    
    # return only the sorted ids
    return [i[0] for i in instances_ids]
    

def save_to_json(region, data):
    with open(f"{region}.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


regions = read_regions_file()
for region in regions:
    instances = get_aws_instances_per_region(region)
    save_to_json(region,instances)
