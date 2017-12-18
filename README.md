# awsLamda_toSplunk
This is an aws lamda that catches a webhook payload then passes the data to splunk

Has two parameters that are configured in aws, the URL location of the splunk instance and the port it accepts for the http event collector (8088).  Also needs the http event collector token
