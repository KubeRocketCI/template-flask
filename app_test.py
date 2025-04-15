"""Unit test for application."""
from app import app


def test_hello():
    """Returns Hello, World."""
    response = app.test_client().get('/api/hello')

    assert response.status_code == 200
    assert response.data == b'Hello, World!'
