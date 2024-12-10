import os

from dotenv import load_dotenv 


if os.getenv("ENVIRONMENT") is None:
    load_dotenv()


bucket_name = "UserFilerManagerBucket" if os.getenv("BUCKET_NAME") is None \
            else os.getenv("BUCKET_NAME")
