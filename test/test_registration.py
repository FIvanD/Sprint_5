import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from helper import generate_registration_data
from curl import *


@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.get(service_url)
    yield driver

    driver.quit()


class TestRegistration:
    def test_success_registration(self, driver):

        name, email, password = generate_registration_data()


        driver.find_element(*Locators.LOGIN_MAIN_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.CONTINUE_REG_BUTTON).click()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(Locators.LOGIN)
        )

        assert driver.current_url == login_url