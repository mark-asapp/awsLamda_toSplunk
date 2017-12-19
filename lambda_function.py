import requests
import json
import os


def post_to_splunk(payload):

	token = "Splunk " + os.environ['HTTP_TOKEN']
	#url = "http://localhost:8088/services/collector"
	url = os.environ['URL']
	headers = {'Authorization': token }
	return requests.post(url=url, data=payload, headers=headers)

def package_data(payload):

	data = {'event' : payload}
	response = post_to_splunk(json.dumps(data))
	return response.status_code

def lambda_handler(event, context):
	
	alerts = event["alerts"]
	status = []
	for alert in alerts:
		status.append(package_data(alert))
	
	return status
