import requests
from common.utils import read_yaml
import os

config = read_yaml("config/environment.yaml")
active_env = config["active_env"]
base_url = config["environments"][active_env]["base_url"]

class UserAPI:
    def __init__(self):
        self.base_url = base_url

    def create_user(self, username, email, password):
        return requests.post(f"{self.base_url}/users", json={
            "username": username,
            "email": email,
            "password": password
        })

    def get_user(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}")

    def update_user_email(self, user_id, new_email):
        return requests.put(f"{self.base_url}/users/{user_id}", json={"email": new_email})

    def delete_user(self, user_id):
        return requests.delete(f"{self.base_url}/users/{user_id}")

    def get_users(self, page=1, size=10, keyword=""):
        return requests.get(f"{self.base_url}/users", params={
            "page": page,
            "size": size,
            "keyword": keyword
        })
