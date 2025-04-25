import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from conftest import driver
from data import UsersTestData

class TestEntrance:
    # вход по кнопке "Войти в аккаунт" на главной
    def test_login_on_the_main_page(self, driver):
        driver.find_element(*TestLocators.LOGIN_BUTTON_HOMEPAGE).click()
        driver.find_element(*TestLocators.EMAIL_LOGIN).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.PASSWORD_LOGIN).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url.endswith("/login")

    # вход через кнопку "Личный кабинет"
    def test_login_button_personal_account(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_LOGIN).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.PASSWORD_LOGIN).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url.endswith("/login")

    # вход через кнопку в форме регистрации
    def test_login_button_registration_form(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.REGISTER_LOGIN_LINK).click()
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        driver.find_element(*TestLocators.EMAIL_LOGIN).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.PASSWORD_LOGIN).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url.endswith("/login")

    # вход через кнопку в форме восстановления пароля
    def test_login_button_password_recovery(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.RESET_PASSWORD_LINK).click()
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        driver.find_element(*TestLocators.EMAIL_LOGIN).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.PASSWORD_LOGIN).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url.endswith("/login")