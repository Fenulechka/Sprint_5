import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from conftest import driver
from helper import create_random_email, create_random_password
from data import UsersTestData


class TestRegistration:
    # Регистрация нового аккаунта пользователя с валидными данными
    def test_registration_new_account_valid_data(self, driver):
        random_email = create_random_email()
        random_password = create_random_password()
        driver.find_element(*TestLocators.LOGIN_BUTTON_HOMEPAGE).click()
        driver.find_element(*TestLocators.REGISTER_LOGIN_LINK).click()
        driver.find_element(*TestLocators.NAME).send_keys(UsersTestData.username)
        driver.find_element(*TestLocators.EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url.endswith("/login")

    # Проверка появления сообщения "Некорректный пароль" при вводе невалидного по длине пароля
    @pytest.mark.parametrize('wrong_password', ['12345', '1',])
    def test_registration_invalid_password(self, driver, wrong_password):
        random_email = create_random_email()
        driver.find_element(*TestLocators.LOGIN_BUTTON_HOMEPAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.REGISTER_LOGIN_LINK))
        driver.find_element(*TestLocators.REGISTER_LOGIN_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.REG_BUTTON))
        driver.find_element(*TestLocators.NAME).send_keys(UsersTestData.username)
        driver.find_element(*TestLocators.EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(wrong_password)
        driver.find_element(*TestLocators.REG_BUTTON).click()
        assert driver.find_element(*TestLocators.INCORRECT_PASSWORD).text == 'Некорректный пароль'