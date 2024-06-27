import random
import string
import allure


class CreateUserData:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    @allure.step('Генерация данных для регистрации пользователя')
    def generation_data_for_registration():
        email = 'testkate_' + CreateUserData.generate_random_string(5) +'@' + random.choice(["mail.ru", "gmail.com", "ya.ru"])
        password = CreateUserData.generate_random_string(8)
        name = 'testkate_' + CreateUserData.generate_random_string(5)

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        return payload






