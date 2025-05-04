import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *



class TestLogin:

    def test_login_on_main(self, driver):
        driver.find_element(*Locators.LOGIN_MAIN_BUTTON).click()
        assert driver.current_url == login_url


    def test_login_on_personal_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.current_url == login_url



    def test_login_on_password_remember_form(self, driver):
        driver.get(forgot_password_url)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert driver.current_url == login_url

