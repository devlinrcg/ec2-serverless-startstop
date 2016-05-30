#Script to Stop EC2 Instances with tag-key AutoStartStop and tag-value TRUE
#Import libraries
import smtplib
import botocore
import boto3
from datetime import *
import time
#Import Session on boto3
import boto3.session
def lambda_handler(event, context):
	client = boto3.resource('ec2' , region_name='sa-east-1')
	instances = client.instances.filter(
		Filters=[{'Name': 'tag-key', 'Values': ['AutoStartStop']}, {'Name': 'tag-value', 'Values': ['TRUE']}])
	for instance in instances:
		if instance.state["Name"] == 'stopped':
			print "Instance %s" % instance.id, "is stopped; I'm starting it"
			instance.start()
		else:
			print "Instance %s" % instance.id, "is already in a running state"
