from werkzeug.exceptions import HTTPException
from flask import Flask, Response, request
from dotenv import load_dotenv
from os import getenv

from src.app.service.file_manager  import FileManager

UPLOAD_FOLDER = './'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if getenv("ENVIRONMENT") is None:
    load_dotenv()


@app.get("/healthcheck")
def health_check():
    return "ok!"

@app.put("/file")
def user_upload_file():
    try:
        uploader = FileManager()
        file = request.get_data()
        user_name = request.args.get('user_name')
        file_name = request.args.get('filename')
        uploader.filename_validator(file_name)
        uploader.put_file(
            user_name=user_name,
            file=file,
            file_name=file_name
        )
        if file is None:
            raise HTTPException("no file has uploaded.")
        if user_name is None or file_name is None:
            raise HTTPException("no file has uploaded.")
        fi
    except Exception as e:
        return Response("", status=500, mimetype='application/json')
    except HTTPException as e:
        return Response("", status=400, mimetype='application/json')

@app.get("/file")
def user_list_file():
    user_name = request.args.get('user_name')
    pagination_token = request.args.get('pagination_token')
    if user_name is None:
        raise HTTPException("no file has uploaded.")    
    try:
        file_manager = FileManager()
        file = file_manager.list_file(
            user_name=user_name,
            pagination_token=pagination_token
        )
        return file
    except Exception as e:
        print(e)
        return Response("", status=500, mimetype='application/json')
    except HTTPException as e:
        return Response("", status=400, mimetype='application/json')
