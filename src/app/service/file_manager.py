
from typing import Union
from src.app.infra.file import File
from src.app.infra.dynamo_db import DynamoDB
from werkzeug.exceptions import HTTPException
import re

class InvalidFilename(HTTPException):
    code = 400
    description = '<p>Invalid Filename.</p>'

class FileManager():
    def __init__(self):
        self.file_provider = File()
        self.max_length_folder_name = 32
        
    def filename_validator(self, filename : str) -> None:
        if re.match("^[a-zA-Z0-9]+([_-][a-zA-Z0-9]+)*$", filename) is not None:
            return
        raise InvalidFilename
    
    def put_file(
        self, 
        file : bytes, 
        file_name : str,
        user_name : str
    ):
        self.file_provider.create_file_by_user(
            filename=file_name,
            file=file,
            user_name=user_name
        )
    
    def list_file(
        self,
        user_name : str,
        pagination_token : Union[str, None]
    ):
        self.file_provider
        
            
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