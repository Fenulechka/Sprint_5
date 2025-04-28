from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import UsersTestData
from urls import PROFILE_URL

class TestEntrancePersonalAccount:
    # переход в "Личный кабинет" по клику на Личный кабинет
    def test_navigate_to_personal_account_by_clicking_personal_account_button(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_LOGIN).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.PASSWORD_LOGIN).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_URL))
        assert driver.current_url.endswith("/account/profile")
