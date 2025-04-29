import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators



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