import os
import ssl
import tempfile
from flask import Flask, session
from flask.testing import CliRunner, Client
import pytest
from flask_file import create_app

@pytest.fixture()
def app() -> Flask: # type: ignore
    app = create_app({"TESTING":True,})
    # other setup can go here
    
    yield app
    # clean up / reset resources here


@pytest.fixture() 
def client(app) -> Client:
    return app.test_client()

class AuthActions:
    def __init__(self, client):
        self._client = client

    def login(self, username="a", password="a"):
        return self._client.post(
            "/hogetter/login", data={"username": username, "password": password}
        )

    def logout(self):
        return self._client.get("hogetter/logout")
    


@pytest.fixture
def auth(client) -> AuthActions:
    return AuthActions(client)
