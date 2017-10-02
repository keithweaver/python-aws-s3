import boto3
from botocore.client import Config

ACCESS_KEY_ID = ''
ACCESS_SECRET_KEY = ''
BUCKET_NAME = ''
FILE_NAME = 'bitmoji.png';


data = open(FILE_NAME, 'rb')

# S3 Connect
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

listObjSummary = s3.Bucket(BUCKET_NAME).objects.all()

for objSum in listObjSummary:
    print ('Item:')
    print (objSum.key)



print ("Done")
