import requests
import pytest
import allure
from helpers import CreateUserData
from data import Url, ErrorMessage


class TestCreateUser:
    @allure.title('Успешное создание пользователя')
    def test_create_user_pass(self, create_user_data):
        response = requests.post(Url.CREATE_USER, data=create_user_data)
        assert response.status_code == 200 and response.json()['success'] is True and 'accessToken' in response.text

    @allure.title('Создание уже зарегистрированного пользователя')
    def test_create_user_double(self, create_user_data):
        requests.post(Url.CREATE_USER, data=create_user_data)
        response_double = requests.post(Url.CREATE_USER, data=create_user_data)
        expected_response = {'success': False, 'message': ErrorMessage.USER_ALREADY_EXIST}
        assert response_double.status_code == 403 and response_double.json() == expected_response

    @allure.title('Создание пользователя без одного обязательного поля')
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_create_user_without_one_field(self, field, create_user_data):
        del create_user_data[field]
        response = requests.post(Url.CREATE_USER, data=create_user_data)
        expected_response = {'success': False, 'message': ErrorMessage.NO_REQUIRED_FIELD}
        assert response.status_code == 403 and response.json() == expected_response





