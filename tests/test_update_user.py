import requests
import allure
from data import Url, ErrorMessage


class TestUpdateUser:
    @allure.title('Изменение данных email и name c авторизацией')
    def test_update_user_data(self, user_registration):
        user_before = requests.get(Url.UPDATE_USER, headers={'Authorization': user_registration[1]})
        payload = {
            "email": "update_",
            "name": "update_name"
        }

        response = requests.patch(Url.UPDATE_USER, headers={'Authorization': user_registration[1]}, data=payload)
        user_after = requests.get(Url.UPDATE_USER, headers={'Authorization': user_registration[1]})
        assert response.status_code == 200 and response.json()["user"] == payload
        assert user_before != user_after

    @allure.title('Изменение данных юзера без авторизацией')
    def test_update_user_data_without_token(self):
        response = requests.patch(Url.UPDATE_USER, data={})
        expected_response = {'success': False, 'message': ErrorMessage.NO_AUTH}
        assert response.status_code == 401 and response.json() == expected_response












