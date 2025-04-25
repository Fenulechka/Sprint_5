import pytest
from selenium import webdriver
from locators import TestLocators
from data import UsersTestData


# Фикстура веб-драйвера
@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1200,600')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


# Фикстура для авторизации с валидными данными логин и пароль перед тестами
@pytest.fixture
def login(driver):
    driver.find_element(*TestLocators.LOGIN_BUTTON_HOMEPAGE).click()
    driver.find_element(*TestLocators.EMAIL_LOGIN).send_keys(UsersTestData.email)
    driver.find_element(*TestLocators.PASSWORD_LOGIN).send_keys(UsersTestData.password)
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()