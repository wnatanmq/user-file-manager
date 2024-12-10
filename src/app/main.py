from werkzeug.exceptions import HTTPException
from flask import Flask, request
from dotenv import load_dotenv
from os import getenv

from service.uploader import Uploader
from infra.s3 import S3Provider

UPLOAD_FOLDER = './'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if getenv("ENVIRONMENT") is None:
    load_dotenv()


@app.get("/healthcheck")
def health_check():
    S3Provider().list_s3()
    return "ok!"

@app.put("/")
def test(a : str):
    print(a)

@app.put("/upload")
def user_upload_file():
    file = request.get_data()
    user_name = request.args.get('user_name')
    filename = request.args.get('filename')    
    if file is None:
        raise HTTPException("no file has uploaded.")
    Uploader().put_file(
        filename=filename,
        file=file,
        user_name=user_name
    )
    return "ok"
