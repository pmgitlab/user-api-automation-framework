import pytest
import allure
from api.user_api import UserAPI
from common.utils import random_username, random_email
from common.assertions import assert_response

@allure.feature("Create User API")
class TestCreateUser:
    @allure.story("Create user with valid details")
    def test_create_user_normal(self):
        api = UserAPI()
        username = random_username()
        email = random_email()
        res = api.create_user(username, email, "123456")
        assert res.status_code in [200, 201]

    @allure.story("Create user with missing field")
    def test_create_user_missing_email(self):
        api = UserAPI()
        res = api.create_user("user", "", "123456")
        assert res.status_code in [400, 422]

    @allure.story("Create user with invalid email")
    def test_create_user_invalid_email(self):
        api = UserAPI()
        res = api.create_user("user", "invalidemail", "123456")
        assert res.status_code in [400, 422]

    @allure.story("Create user with too long username (edge case)")
    def test_create_user_long_username(self):
        api = UserAPI()
        long_username = "user_" + "x" * 200
        res = api.create_user(long_username, random_email(), "123456")
        assert res.status_code in [400, 422]
    
    @allure.story("Create user with empty username")
    def test_create_user_empty_username(self):
        api = UserAPI()
        res = api.create_user("", random_email(), "123456")
        assert res.status_code in [400, 422]
    
    @allure.story("Create user with short password")
    def test_create_user_short_password(self):
        api = UserAPI()
        res = api.create_user(random_username(), random_email(), "12")
        assert res.status_code in [400, 422]
