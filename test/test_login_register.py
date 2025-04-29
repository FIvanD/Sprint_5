import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *




class TestLogin:

    def test_login_on_registration_form(self, driver):
        driver.find_element(*Locators.LOGIN_MAIN_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert driver.current_url == login_url
