import boto3

endpoint_url = "http://localhost:4000"

def read_regions_file():
    with open('regions.txt') as f:
        regions = f.read().split(",")
        print(regions)

# Helper to translate AWS datatime to ISO format
def datetime_converter(obj):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print(response)

