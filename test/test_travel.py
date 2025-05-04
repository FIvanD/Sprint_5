import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *




class TestTravelHeader:

    def test_travel_to_profile(self, login):
        login.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(login, 10).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        assert login.current_url == personal_account_url

    def test_travel_to_constructor(self, login):
        login.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(login, 10).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()
        assert login.current_url == service_url

    def test_travel_to_constructor_logo(self, login):
        login.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(login, 10).until(EC.element_to_be_clickable(Locators.LOGO_BUTTON)).click()
        assert login.current_url == service_url

class TestLogout:

    def test_logout(self, login):
        login.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(login, 10).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()
        WebDriverWait(login, 10).until(EC.element_to_be_clickable(Locators.LOGIN))
        assert login.current_url == login_url
