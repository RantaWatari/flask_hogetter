from deta import Deta
from hashlib import sha256

def connect_db_drive():
    db = Deta(project_key="c0wmhhz3nbe_aT8g675zLGZKhcfQKzvn7CaBTU6oqSjg")
    db = db.Drive(name="hogetter_drive")
    return db

