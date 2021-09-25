import pytest
import json

from base import create_app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_ping_success(client):
    returned_value = client.get('/health')
    assert json.loads(returned_value.data)['success'] is True
    assert returned_value.status_code == 200


def test_argument_missing_failure(client):
    returned_value = client.get('/specialmath')
    assert returned_value.status_code == 400
    assert json.loads(returned_value.data)['error'] == "A value is needed to perform the special math calculation"


def test_string_argument_invalid_failure(client):
    returned_value = client.get('/specialmath/shark')
    assert returned_value.status_code == 422
    assert json.loads(returned_value.data)['error'] == "An invalid value was provided for the special math calculation"


def test_decimal_argument_invalid_failure(client):
    returned_value = client.get('/specialmath/1.22')
    assert returned_value.status_code == 422
    assert json.loads(returned_value.data)['error'] == "An invalid value was provided for the special math calculation"


def test_specialmath_success(client):
    returned_value = client.get('/specialmath/7')
    assert returned_value.status_code == 200
    assert json.loads(returned_value.data)['result'] == 79
