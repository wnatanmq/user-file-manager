import boto3

from helper import constants

    
class S3Provider:
    def __init__(self):
        self.client = boto3.client('s3')
        self.bucket_name    = constants.bucket_name

    def upload_file(
        self,
        file : bytes,
        key : str
    ):
        self.client.put_object(
            Bucket=self.bucket_name,
            Body=file,
            Key=key
        )
        
    