import boto3

from src.app.helper import constants

    
class S3Provider:
    def __init__(self):
        self.client         = boto3.client('s3')
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
        
    def paginate_file(
        self,
        pagination_token : str,
        prefix : str
    ):
        page_iterator_params= {
            "Bucket" : self.bucket_name,
            "Prefix" : prefix,
            "MaxKeys":4
        }
        if pagination_token:
            page_iterator_params["ContinuationToken"] = pagination_token
        return self.client.list_objects_v2(**page_iterator_params)    

    

def find_largest_file(self, prefix : str):
    paginator = self.client.get_paginator("list_objects_v2")
    largest_file = None
    largest_size = 0
    for page in paginator.paginate(Bucket=self.bucket_name, Prefix=prefix):
        if "Contents" in page:
            for obj in page["Contents"]:
                size = obj["Size"]
                if size > largest_size:
                    largest_size = size
                    largest_file = obj["Key"]

    return largest_file, largest_size