from deta import Deta

def connect_db_text():
    db = Deta(project_key="c0wmhhz3nbe_tc1hZ2nHqv9o6f8rrVRqpADMqxL7jtjX")
    db = db.Base(name="hogetter_text")
    return db


def connect_db_drive():
    db = Deta(project_key="c0wmhhz3nbe_aT8g675zLGZKhcfQKzvn7CaBTU6oqSjg")
    db = db.Drive(name="hogetter_drive")
    return db



def create_db(hogeet):
    
    connect_db_text().put({
        "text":hogeet
    })

def show_db():
    db = connect_db_text()
    fetch_data = db.fetch()
    
    #(3)
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



