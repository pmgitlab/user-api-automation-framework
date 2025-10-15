import pytest
import allure
from api.user_api import UserAPI
from common.utils import random_username, random_email


@allure.feature("Get User Details API")
class TestGetUser:
    @allure.story("Get user details successfully")
    def test_get_user_valid(self):
        api = UserAPI()
        user = api.create_user(random_username(), random_email(), "123456").json()
        user_id = user.get("id") or user.get("data", {}).get("id", 1)
        res = api.get_user(user_id)
        assert res.status_code == 200

    @allure.story("Get user with invalid ID format")
    def test_get_user_invalid_id(self):
        api = UserAPI()
        res = api.get_user("abc")
        assert res.status_code in [400, 422, 404]

    @allure.story("Get user that does not exist")
    def test_get_user_not_found(self):
        api = UserAPI()
        res = api.get_user(999999)
        assert res.status_code in [404, 400]

    @allure.story("Get user with missing ID (edge case)")
    def test_get_user_missing_id(self):
        api = UserAPI()
        res = api.get_user("")  # empty path parameter
        assert res.status_code in [400, 404]
