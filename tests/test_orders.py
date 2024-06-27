import requests
import allure
from data import Url, ErrorMessage, Ingredients


class TestCreateOrder:
    @allure.title('Создание заказа без авторизации')
    def test_create_order_no_auth(self):
        response = requests.post(Url.CREATE_ORDER, data=Ingredients.true_ingredients)
        assert response.status_code == 200 and response.json()["success"] is True and "number" in response.text

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_auth(self, get_token):
        token = get_token
        response = requests.post(Url.CREATE_ORDER, headers={'Authorization': token}, data=Ingredients.true_ingredients)
        assert response.status_code == 200 and response.json()["success"] is True
        assert "ingredients", "owner" in response.text

    @allure.title('Создание заказа с невалидным хешем')
    def test_create_order_incorrect_ingredient(self):
        response = requests.post(Url.CREATE_ORDER, data=Ingredients.false_ingredients)
        assert response.status_code == 500

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_incorrect_ingredient(self):
        response = requests.post(Url.CREATE_ORDER, data={})
        expected_response = {'success': False, 'message': ErrorMessage.NO_INGREDIENT}
        assert response.status_code == 400 and response.json() == expected_response

    @allure.title("Получение заказов авторизованным юзером")
    def test_get_order_auth_user(self, get_token):
        token = get_token()
        response = requests.get(Url.GET_ORDERS, headers={'Authorization': token})
        assert response.status_code == 200  and response.json()["success"] is True
        assert "orders" in response.text

    @allure.title("Получение заказов неавторизованным юзером")
    def test_get_order_auth_user(self):
        response = requests.get(Url.CREATE_ORDER)
        expected_response = {'success': False, 'message': ErrorMessage.NO_AUTH}
        assert response.status_code == 401 and response.json() == expected_response












