from deta import Deta
import datetime
from flask import g
from hashlib import sha256

def connect_db_text():
    db = Deta(project_key="c0wmhhz3nbe_tc1hZ2nHqv9o6f8rrVRqpADMqxL7jtjX")
    db = db.Base(name="hogetter_text")
    return db


def now_time():
    now_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))) 
    now_time_tuple = now_time.timetuple()
    now = []
    
    for i in range(len(now_time_tuple[:6])):
        time = str(now_time_tuple[i])
        if i == 0 :
            time = time.zfill(4)
        else:
            time = time.zfill(2)
        now.append(time)
    # year~microsecond 
    time = (str(now_time.microsecond))
    now.append(time.zfill(6))
    return now


def generate_hogeet_id(hogeet_text:str) -> str:

    pre_new_id = f"{g.user} + {now_time()} + {hogeet_text}".encode("utf-8")
    hogeet_id = sha256(pre_new_id).hexdigest()

    return hogeet_id


def show_db_text_single(hogeet_id):
    post = connect_db_text().get(hogeet_id)

    return post



def show_db_text_all():
    db = connect_db_text()
    fetch_data = db.fetch()
    
    try:  
        ## Usefull only deploy enviroment
        for i in fetch_data:
            datas = i
        posts = []
        for j in datas:
            posts.append(j)

    except TypeError:
        ## Usefull Only local enviroment
        posts = fetch_data.items

    return posts


def create_db_text(hogeet_text:str,hogeet_id:str,content_id:str):
    
    connect_db_text().put({
        "time":now_time(),
        "owner":g.user,
        "text":hogeet_text,
        "key":hogeet_id,
        "content_id":content_id
    })



def delete_db_text(hogeet_id):
    connect_db_text().delete(hogeet_id)


def update_db_text(hogeet_id,hogeet_text):
    connect_db_text().update({
        "text":hogeet_text
    },key=hogeet_id)