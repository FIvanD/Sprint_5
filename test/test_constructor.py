import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *
from data import Credentials

@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.get(service_url)
    yield driver

    driver.quit()

@pytest.fixture
def login(driver):
    driver.get(login_url)
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON)
    )
    return driver


class TestConstructor:

    def test_chose_sauces_in_constructor(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SAUCES)).click()
        selected_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.BUNS))
        assert selected_section.is_displayed()


    def test_chose_fillings_in_constructor(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.FILLINGS)).click()
        selected_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.FILLINGS))
        assert selected_section.is_displayed()


    def test_chose_buns_in_constructor(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SAUCES)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUNS)).click()
        selected_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.BUNS))
        assert selected_section.is_displayed()