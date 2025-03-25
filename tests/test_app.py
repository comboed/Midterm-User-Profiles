import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()

        # Insert test user
        test_user = User(username='christopherbaldwin ', profile_picture='default.png')
        db.session.add(test_user)
        db.session.commit()

    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'christopherbaldwin' in response.data

def test_user_detail_page(client):
    response = client.get('/uid/1/')
    assert response.status_code == 200
    assert b'christopherbaldwin' in response.data

def test_nonexistent_user(client):
    response = client.get('/uid/999/')
    assert response.status_code == 404
