import pytest
import allure
from api.user_api import UserAPI
from common.utils import random_username, random_email

@allure.feature("Batch Query Users API")
class TestBatchQueryUsers:
    @allure.story("List users successfully (default page)")
    def test_list_users(self):
        api = UserAPI()
        res = api.get_users(page=1, size=10)
        assert res.status_code == 200

    @allure.story("Search users by keyword")
    def test_search_user_keyword(self):
        api = UserAPI()
        username = random_username()
        api.create_user(username, random_email(), "123456")
        res = api.get_users(keyword=username)
        assert res.status_code == 200

    @allure.story("List users on empty page (edge case)")
    def test_list_users_empty_page(self):
        api = UserAPI()
        res = api.get_users(page=9999, size=10)
        assert res.status_code == 200

    @allure.story("List users with invalid parameters")
    def test_list_users_invalid_params(self):
        api = UserAPI()
        res = api.get_users(page="abc", size=-1)
        assert res.status_code in [400, 422]

    @allure.story("List users with large page size (edge case)")
    def test_list_users_large_size(self):
        api = UserAPI()
        res = api.get_users(page=1, size=1000)
        assert res.status_code in [200, 400]
