# awsLamda_toSplunk
This is an aws lamda that catches a webhook payload then passes the data to splunk

Has two parameters that are configured in aws, the URL location of the splunk instance and the port it accepts for the http event collector (8088).  Second item is  the http event collector token.

The event.json is a sample json output from Threatstack webhook and can be used for local testing.  See https://pypi.python.org/pypi/python-lambda-local/ for more details on this.
