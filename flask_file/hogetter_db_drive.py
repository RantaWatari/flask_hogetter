from deta import Deta
from flask import g
from hashlib import sha256

def connect_db_drive():
    db = Deta(project_key="c0wmhhz3nbe_aT8g675zLGZKhcfQKzvn7CaBTU6oqSjg")
    db = db.Drive(name="hogetter_drive")
    return db

def generate_content_id(hogeet_id:str,content_name:str,content_type:str) -> str:

    pre_new_id = f"{hogeet_id} + {content_name}".encode("utf-8")
    extension = content_type.split("/")[-1]
    content_id = f"{sha256(pre_new_id).hexdigest()}.{extension}"

    return content_id



def put_db_drive(name:str,data,content_type:str):
    connect_db_drive().put(name=name,data=data,content_type=content_type)

def show_db_drive(name:str):
    post = connect_db_drive().get(name)

    return post    