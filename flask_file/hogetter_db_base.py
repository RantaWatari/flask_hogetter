from deta import Deta
import datetime
from flask import g
from hashlib import sha256

def connect_db_base():
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


def show_db_base_single(hogeet_id):
    post = connect_db_base().get(hogeet_id)

    return post


def sort(posts_unsorted): 
    posts_copy = posts_unsorted.copy()
    sort_p = {}
    for i in range(len(posts_unsorted)):
        bind_time = ""
        for j in posts_unsorted[i]["time"]:
            bind_time = bind_time + str(j)
        sort_p[int(bind_time)] = posts_unsorted[i]["key"]
    
    sort_in = sorted(sort_p,reverse=True)
    sorted_index = [sort_p[i] for i in sort_in]

    posts_sorted = []
    for i in sorted_index:
        for j in posts_copy:
            if j["key"] == i: posts_sorted.append(j)

    return posts_sorted



def show_db_base_all():
    db = connect_db_base()
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


    posts = sort(posts)

    return posts


def create_db_base(hogeet_text:str,hogeet_id:str,content_id:str):
    
    connect_db_base().put({
        "time":now_time(),
        "owner":g.user,
        "text":hogeet_text,
        "key":hogeet_id,
        "content_id":content_id
    })



def delete_db_base(hogeet_id):
    connect_db_base().delete(hogeet_id)


def update_db_base(hogeet_id,hogeet_text,content_id):
    connect_db_base().update({
        "text":hogeet_text,
        "content_id":content_id
    },key=hogeet_id)