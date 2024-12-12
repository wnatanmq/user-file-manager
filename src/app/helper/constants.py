import os

from dotenv import load_dotenv 


if os.getenv("ENVIRONMENT") is None:
    load_dotenv()


bucket_name : str = "UserFilerManagerBucket" if os.getenv("BUCKET_NAME") is None \
            else os.getenv("BUCKET_NAME")
dynamo_db_name : str = "UsersTable" if os.getenv("DYNAMOBD_NAME") is None \
            else os.getenv("DYNAMOBD_NAME")
