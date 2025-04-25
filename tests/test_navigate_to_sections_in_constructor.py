import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from conftest import driver

class TestNavigateToSectionsInConstructor:
    # переход в конструкторе из раздела "Начинки" в раздел "Булки", без авторизации в личном кабинете
    def test_navigate_from_fillings_to_buns_in_constructor(self, driver):
        driver.find_element(*TestLocators.FILLINGS_TAB).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.FILLINGS_TAB_ACTIVE))
        driver.find_element(*TestLocators.BUNS_TAB).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BUNS_TAB_ACTIVE))
        assert driver.find_element(*TestLocators.BUNS_TAB_ACTIVE).is_displayed()

    # переход в конструкторе из раздела "Начинки" в раздел "Соусы", без авторизации в личном кабинете
    def test_navigate_from_fillings_to_sauces_in_constructor(self, driver):
        driver.find_element(*TestLocators.FILLINGS_TAB).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.FILLINGS_TAB_ACTIVE))
        driver.find_element(*TestLocators.SAUCES_TAB).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.SAUCES_TAB_ACTIVE))
        assert driver.find_element(*TestLocators.SAUCES_TAB_ACTIVE).is_displayed()

    # переход в конструкторе из раздела "Соусов" в раздел "Булки", без авторизации в личном кабинете
    def test_navigate_from_sauces_to_buns_in_constructor(self, driver):
        driver.find_element(*TestLocators.SAUCES_TAB).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.SAUCES_TAB_ACTIVE))
        driver.find_element(*TestLocators.BUNS_TAB).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BUNS_TAB_ACTIVE))
        assert driver.find_element(*TestLocators.BUNS_TAB_ACTIVE).is_displayed()

    # переход в конструкторе из раздела "Соусов" в раздел "Начинки", без авторизации в личном кабинете
    def test_navigate_from_sauces_to_fillings_in_constructor(self, driver):
        driver.find_element(*TestLocators.SAUCES_TAB).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.SAUCES_TAB_ACTIVE))
        driver.find_element(*TestLocators.FILLINGS_TAB).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.FILLINGS_TAB_ACTIVE))
        assert driver.find_element(*TestLocators.FILLINGS_TAB_ACTIVE).is_displayed()

    # переход в конструкторе из раздела "Булки" в раздел "Начинки", без авторизации в личном кабинете
    def test_navigate_from_buns_to_fillings_in_constructor(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BUNS_TAB_ACTIVE))
        driver.find_element(*TestLocators.FILLINGS_TAB).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.FILLINGS_TAB_ACTIVE))
        assert driver.find_element(*TestLocators.FILLINGS_TAB_ACTIVE).is_displayed()

    # переход в конструкторе из раздела "Булки" в раздел "Соусы", без авторизации в личном кабинете
    def test_navigate_from_buns_to_sauces_in_constructor(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.BUNS_TAB_ACTIVE))
        driver.find_element(*TestLocators.SAUCES_TAB).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.SAUCES_TAB_ACTIVE))
        assert driver.find_element(*TestLocators.SAUCES_TAB_ACTIVE).is_displayed()

