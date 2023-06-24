from deta import Deta

def connect_db_text():
    db = Deta(project_key="c0wmhhz3nbe_tc1hZ2nHqv9o6f8rrVRqpADMqxL7jtjX")
    db = db.Base(name="hogetter_text")
    return db


def connect_db_text():
    db = Deta(project_key="c0wmhhz3nbe_aT8g675zLGZKhcfQKzvn7CaBTU6oqSjg")
    db = db.Drive(name="hogetter_drive")
    return db

