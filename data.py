class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    CREATE_USER = f'{BASE_URL}api/auth/register'
    LOGIN_USER = f'{BASE_URL}api/auth/login'
    UPDATE_USER = f'{BASE_URL}api/auth/user'
    DELETE_USER = f'{BASE_URL}api/auth/user'
    CREATE_ORDER = f'{BASE_URL}api/orders'
    GET_ORDERS = f'{BASE_URL}api/orders'


class ErrorMessage:
    USER_ALREADY_EXIST = "User already exists"
    NO_REQUIRED_FIELD = "Email, password and name are required fields"
    INCORRECT_FIELD = "email or password are incorrect"
    NO_AUTH = "You should be authorised"
    NO_INGREDIENT = "Ingredient ids must be provided"


class Ingredients:
    true_ingredients = {"ingredients":["61c0c5a71d1f82001bdaaa7a"]}
    false_ingredients = {"ingredients":["testkate61c0c5a71d1f82001bdaaa7a"]}


