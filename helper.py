import random
import string

# Генерация емейла для регистрации с двумя рандомными буквами и рандомным числом от 100 до 999
def create_random_email():
    random_letters = ''.join((random.choice(string.ascii_letters) for x in range(2)))
    random_email = f'tatykovr_20_{random_letters}_{random.randint(100, 999)}@yandex.ru'
    return random_email


# Генерация пароля для регистрации с двумя рандомными буквами и рандомным числом от 10 до 99
def create_random_password():
    random_letters = ''.join((random.choice(string.ascii_letters) for x in range(2)))
    random_password = f'qwerty{random_letters}{random.randint(10, 99)}'
    return random_password


