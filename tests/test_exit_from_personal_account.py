from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from urls import LOGIN_URL


class TestExitFromPersonalAccount:
    # переход по клику на "Конструктор" из личного кабинета
    def test_exit_from_personal_account(self, driver, login):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.PROFILE))
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url.endswith("/login")