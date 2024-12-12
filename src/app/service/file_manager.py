
from typing import Union
from infra.s3 import S3Provider
from infra.dynamo_db import DynamoDB
from werkzeug.exceptions import HTTPException
import re

class InvalidFilename(HTTPException):
    code = 400
    description = '<p>Invalid Filename.</p>'

class FileManager():
    def __init__(self):
        self.s3_provider = S3Provider()
        self.max_length_folder_name = 32
        
    def filename_validator(self, filename : str) -> None:
        if re.match("^[a-zA-Z0-9]+([_-][a-zA-Z0-9]+)*$", filename) is not None:
            return
        raise InvalidFilename
    
    def put_file(
        self, 
        file : bytes, 
        filename : str,
        user_name : str
    ):
        self.s3_provider.upload_file(
            file=file,
            key=f"{user_name}/{filename}"
        )
    
    def list_file(
        self,
        user_name : str,
        pagination_token : Union[str, None]
    ):
        result_paginate =  self.s3_provider.paginate_file(
            pagination_token=pagination_token,
            prefix=f"{user_name}/"
        )
        if not result_paginate.get("Contents"):
            return []
        result =  {
            "files" : list(
            map(
                lambda x: x["Key"],
                result_paginate["Contents"]
            )
        ),
        }
        if result_paginate.get("NextContinuationToken"):
            result["pagination_token"] = result_paginate["NextContinuationToken"]
        
        return result
    
    def update_users_info(
        user_name : str,
        file : bytes, 
        file_name : str
    ):
        dynamodb = DynamoDB()
        user = dynamodb.get_item(user_name)
        file_count = file.count()
        item={
            "user_email" : user_name,
            "heaviest_file_size" : user.get("heaviest_file_size", file_count),
            "heaviest_file_name" : user.get("heaviest_file_name", file_name),
            "lightest_file_size" : user.get("lightest_file_size", file_count),
            "lightest_file_name" : user.get("lightest_file_name", file_name)
        }
        if file_count > user.get("heaviest_file_size", file_count+1):
            item["heaviest_file_size"] = file_count
            item["heaviest_file_name"] = file_name
        if file_count < user.get("lightest_file_size", file_count-1):
            item["lightest_file_size"] = file_count
            item["lightest_file_name"] = file_name
        dynamodb.put_item(
            item=item
        )