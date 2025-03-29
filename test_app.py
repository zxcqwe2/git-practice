import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_add_endpoint(client):
    response = client.get('/add/5/3')
    assert response.status_code == 200
    assert response.json['result'] == 8

def test_divide_by_zero(client):
    response = client.get('/divide/10/0')
    assert response.status_code == 400
    assert b'Cannot divide' in response.data