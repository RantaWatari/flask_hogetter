import pytest
#import sys
#print(sys.path)

from ..flask_file import app as hogetter

@pytest.fixture()
def app():
    app = hogetter
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()