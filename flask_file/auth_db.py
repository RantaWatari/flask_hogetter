from deta import Deta


def connect_db():
    db = Deta(project_key="c0wmhhz3nbe_KBbLfJ9kud5Ji9DCorDGKuJ3M4w61aUY")
    db = db.Base(name="users")
    return db


def signup_db(username,password):
    
    connect_db().put({
        "key":username, 
        "username":username,
        "password":password,
    })

def signout_db(username):
     connect_db().delete(username)


def get_account(username):
        stored_account = connect_db().get(username)
        return stored_account
    
