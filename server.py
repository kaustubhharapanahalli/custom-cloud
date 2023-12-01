import boto3
import os

input_bucket = "quiz-on-friday-project-3-input-data"
output_bucket = "quiz-on-friday-project-3-output-data"

test_cases = "test_cases/"

rgw_endpoint = "http://192.168.64.6:8080"

access_key = "useraccesskey"
secret_key = "usersecretkey"

def get_input_files(s3):

	global input_bucket
	list_obj = s3.list_objects_v2(Bucket=input_bucket)

    video_names = dict()
    invoked = set()
	try:
		for item in list_obj["Contents"]:

			key = item["Key"]

			

	except:

		print("Empty Bucket")



s3 = boto3.client('s3', endpoint_url=rgw_endpoint, aws_access_key_id=access_key, aws_secret_access_key=secret_key)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

get_input_files(s3)