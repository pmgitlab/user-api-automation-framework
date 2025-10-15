import pytest
import allure
from api.user_api import UserAPI
from common.utils import random_username, random_email


@allure.feature("Update User Email API")
class TestUpdateUser:
    @allure.story("Update user email successfully")
    def test_update_user_valid(self):
        api = UserAPI()
        user = api.create_user(random_username(), random_email(), "123456").json()
        user_id = user.get("id") or user.get("data", {}).get("id", 1)
        res = api.update_user_email(user_id, random_email())
        assert res.status_code in [200, 204]

    @allure.story("Update with invalid email format")
    def test_update_user_invalid_email(self):
        api = UserAPI()
        user = api.create_user(random_username(), random_email(), "123456").json()
        user_id = user.get("id") or user.get("data", {}).get("id", 1)
        res = api.update_user_email(user_id, "invalidemail")
        assert res.status_code in [400, 422]

    @allure.story("Update deleted/nonexistent user")
    def test_update_deleted_user(self):
        api = UserAPI()
        res = api.update_user_email(999999, random_email())
        assert res.status_code in [404, 400]

    @allure.story("Update user with missing email field (edge case)")
    def test_update_user_missing_email(self):
        api = UserAPI()
        user = api.create_user(random_username(), random_email(), "123456").json()
        user_id = user.get("id") or user.get("data", {}).get("id", 1)
        res = api.update_user_email(user_id, "")
        assert res.status_code in [400, 422]
