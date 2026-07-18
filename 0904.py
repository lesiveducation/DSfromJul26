import boto3

s3 = boto3.client(
    "s3",
    endpoint_url="https://s3.us-west-004.backblazeb2.com",
    aws_access_key_id="69a8ecf2122c",
    aws_secret_access_key="0035f0b3651e9e19ddd9a12b3a6d52d9538164b388"
)
s3.upload_file("Project1_HH.cv/data/hhdata.csv", "1stDLBucket", "hhdata.csv")