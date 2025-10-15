import yaml
import random
import string
from faker import Faker

fake = Faker()

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def random_username():
    return "user_" + ''.join(random.choices(string.ascii_lowercase, k=5))

def random_email():
    return fake.email()
