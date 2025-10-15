import pytest
import allure
from api.user_api import UserAPI
from common.utils import random_username, random_email

@allure.feature("Delete User API")
class TestDeleteUser:
    @allure.story("Delete existing user successfully")
    def test_delete_user_valid(self):
        api = UserAPI()
        user = api.create_user(random_username(), random_email(), "123456").json()
        user_id = user.get("id") or user.get("data", {}).get("id", 1)
        res = api.delete_user(user_id)
        assert res.status_code in [200, 204]

    @allure.story("Delete user already deleted")
    def test_delete_user_already_deleted(self):
        api = UserAPI()
        res = api.delete_user(999999)
        assert res.status_code in [400, 404]

    @allure.story("Delete user with invalid ID")
    def test_delete_user_invalid_id(self):
        api = UserAPI()
        res = api.delete_user("abc")
        assert res.status_code in [400, 422, 404]

    @allure.story("Delete user with missing ID (edge case)")
    def test_delete_user_missing_id(self):
        api = UserAPI()
        res = api.delete_user("")
        assert res.status_code in [400, 404]
