from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from urls import BASE_URL

class TestNavigateFromPersonalAccount:
    # переход по клику на "Конструктор" из личного кабинета
    def test_navigate_to_constructor_from_personal_account(self, driver, login):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.PROFILE))
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    # переход по клику на логотип Stellar Burgers из личного кабинета
    def test_navigate_by_clicking_logo_from_personal_account(self, driver, login):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.PROFILE))
        driver.find_element(*TestLocators.LOGO_SWITCHING).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

