import requests
import allure
from data import Url, ErrorMessage


class TestLoginUser:
    @allure.title('Успешная авторизация пользователя')
    def test_login_user_pass(self, user_registration):
        payload = {
            "email": user_registration.get("email"),
            "password": user_registration.get("password")
        }
        response = requests.post(Url.LOGIN_USER, data=payload)
        assert response.status_code == 200 and response.json()["success"] is True

    def test_login_user_pass_uu(self, user_registration):
        payload = {
            "email": user_registration["email"],
            "password": user_registration["password"]
        }
        response = requests.post(Url.LOGIN_USER, data=payload)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Авторизация пользователя с неверным email')
    def test_login_user_invalid_email(self, user_registration):
        payload = {
            "email": user_registration.get("email") + 'surprice',
            "password": user_registration.get("password")
        }
        response = requests.post(Url.LOGIN_USER, data=payload)
        expected_response = {'success': False, 'message': ErrorMessage.INCORRECT_FIELD}
        assert response.status_code == 401 and response.json() == expected_response

    def test_login_user_invalid_emailgfd(self, user_registration):
        payload = {
            "email": user_registration["email"] + 'surprice',
            "password": user_registration["password"]
        }
        response = requests.post(Url.LOGIN_USER, data=payload)
        expected_response = {'success': False, 'message': ErrorMessage.INCORRECT_FIELD}
        assert response.status_code == 401 and response.json() == expected_response

    @allure.title('Авторизация пользователя с неверным password')
    def test_login_user_invalid_password(self, user_registration):
        payload = {
            "email": user_registration.get("email"),
            "password": user_registration.get("password") + 'surprice'
        }
        response = requests.post(Url.LOGIN_USER, data=payload)
        expected_response = {'success': False, 'message': ErrorMessage.INCORRECT_FIELD}
        assert response.status_code == 401 and response.json() == expected_response



