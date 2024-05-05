import ssl
from flask import Flask, url_for
from flask.testing import FlaskClient
from werkzeug import Client
from flask_file import create_app
from tests.conftest import AuthActions
import pytest


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING":True}).testing

def test_index(client: Client):
    response = client.get("/")
    #print(response.data)
    assert response.status_code == 302
    assert response.headers["Location"] == "/hogetter/"
    response.close()


def test_loginPage(client: Client):
    assert client.get("/hogetter/login").status_code == 200

@pytest.mark.filterwarnings( "ignore::pytest.PytestUnraisableExceptionWarning" ) 
def test_logout(auth: AuthActions,client: Client):
    auth.login()
    response = auth.logout()
    assert response.location == "/hogetter/"
    

@pytest.mark.filterwarnings( "ignore::pytest.PytestUnraisableExceptionWarning" ) 
def test_login(auth: AuthActions,client: Client):
    response = auth.login()
    response = client.get(response.location)
    #print(response.text)
    assert response.status_code == 200
    assert "Please login if want to hogeet or edit." not in response.text

@pytest.mark.filterwarnings( "ignore::pytest.PytestUnraisableExceptionWarning" ) 
def test_home(client: Client): 
    response = client.get("/hogetter/")
    #print(response.text)
    assert response.status_code == 200
    assert "Please login if want to hogeet or edit." in response.text