import pytest
import json

from app import app

def test_home_page(client):
    response = client.get('/')
    assert b'Index Page' in response.data
    assert response.status_code == 200

@pytest.mark.parametrize(('username', 'password', 'success'), (
    ('', '', False),
    ('wrong_username', '', False),
    ('a_username', '', False),
    ('a_username', 'wrong_password', False),
    ('a_username', 'a_password', True)
))
def test_login_credentials(client, username, password, success):
    mock_data = {
        'username':username,
        'password':password
    }
    response = client.post('/login', data=json.dumps(mock_data), follow_redirects=True)
    if success:
        assert response.status_code == 200
    else:
        assert response.status_code == 400