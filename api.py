import json


def get_instances_by_region(region):
   try:
     data = get_instances_from_file(f"{region}.json")
     return (200,data)
   except:
     return 400


def get_instances_from_file(region_file):
   data = []
   with open(region_file, 'r') as f:
       data = json.load(f)
   return data
   
