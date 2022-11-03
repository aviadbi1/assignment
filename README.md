# Zesty RnD Task
#### INTRO
We've managed to get our hands on a private AWS endpoint serving EC2 instances data of a secret organization.
Your mission, should you choose to accept it, is to extract the data in a readable manner, so that our engineers can use it in their task. This involves the development of two functions: a small ETL and an API router (there is no need to implement the API itself). Please read the following instructions before starting to work on your task. You don't want to miss any important instruction, especially those in [General Guidelines](#general-guidelines).

Prerequisites:
* Docker installed ([Mac](https://docs.docker.com/desktop/mac/install/), [Windows](https://docs.docker.com/desktop/windows/install/))

#### General Guidelines
Your code should be as simple as possible, yet well documented and robust.

Think about operational use cases from the real world.
Few examples:
1. What happens if things go wrong and code crashes?
1. Remember to reuse code, if applicable
1. Document used packages and versions


#### Ready for action?
Great.
First, review the files. There's a small boilerplate code to get you started.

We are going to implement two functions:

###### 1. First function (ETL)
Your mission is to list all EC2 instances (servers) in a particular region of AWS.

1. Read the content of `regions.txt` file into a variable.
1. Use AWS SDK for Python to get a list of existing EC2 instances in the region.
1. [!] Note: Since this is a private EC2 endpoint, it's different than what you're used to; it should work against a local endopint by using `endpoint_url` set in the boto3 client object. At the end of this document, you'll find instructions on how to set up the local endpoint.
1. Sort the instances by launch time (provided *datetime_converter* function will help you to convert AWS time object).
1. Save the result (a list of instances) in JSON format to a file. The file name should be `$region_name.json`
1. Now, let’s make this work for more than one region; change the content of `regions.txt` file to:
```
us-east-1, eu-west-1, ap-southeast-1
```

###### 2. Second function (API Route)
This function will serve as the API router. It will serve the pre-generated list of instances from a file (prepared by the ETL).

This function gets only one parameter - *region*.
It returns a list of instances from a file in a valid JSON format.


###### Setting up the local EC2 endpoint
Run the following:
```
docker run --rm -d --name zesty-ec2 -p 4000:4000 zestyco/ec2-challenge
```

The endpoint is now up and running (make sure it's running with `docker ps`. You can also view its logs with `docker logs zesty-ec2`).

Once you're done, kill the container with `docker kill zesty-ec2`.


#### Bonus
For each instance, print the amount of seconds since it was launched.
