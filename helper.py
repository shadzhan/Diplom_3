import random
import string
import faker
from faker import Faker


faker = Faker()

def generate_registration_data():
    name = faker.name
    email = faker.email()
    password = faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password


def generate_login_data():
    email = faker.email()
    password = faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return email, password


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase, k=10))
    return f"{username}@example.com"