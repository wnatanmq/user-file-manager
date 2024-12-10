
from infra.s3 import S3Provider
from werkzeug.exceptions import HTTPException
import re

class InvalidFilename(HTTPException):
    code = 400
    description = '<p>Invalid Filename.</p>'

class Uploader():
    def __init__(self):
        self.s3_provider = S3Provider()
        self.max_length_folder_name = 32
        
    def filename_validator(filename : str) -> None:
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