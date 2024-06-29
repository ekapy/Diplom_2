import pytest
import requests
from helpers import CreateUserData
from data import Url


@pytest.fixture
def user_registration():
    user_data = CreateUserData.generation_data_for_registration()
    response = requests.post(Url.CREATE_USER, data=user_data)
    token = str(response.json()["accessToken"])
    yield user_data, token
    requests.delete(Url.DELETE_USER, headers={'Authorization': token})


@pytest.fixture
def create_user_data():
    payload = CreateUserData.generation_data_for_registration()
    return payload



