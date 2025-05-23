from faker import Faker
from faker.generator import random

faker = Faker()

def generate_registration_data(pass_error = False):
    name = 'FIvanD'
    email = f'Ivan_Fedotikov_{random.randint(111, 999)}@yandex.ru'

    if pass_error:
        password = faker.password(length=4, special_chars=True, digits=True, upper_case=True, lower_case=True)
    else:
        password = faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

    return name, email, password