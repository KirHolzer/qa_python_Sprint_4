import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPaigeLocators
from data.urls import TestUrls
from data.data import Answers
from pages.main_page import MainPage
from pages.order_page import OrderPage
import time

class TestOrderPage:

    def test_click_on_scooter_in_header(self, browser):
        OrderPage(browser).open_order_url()
        OrderPage(browser).click_on_scooter_in_header()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(MainPaigeLocators.MAIN_PAGE_HEADING))
        assert browser.current_url == TestUrls.MainPageUrl

    def test_fill_client_info_succsesfully(self, browser):
        OrderPage(browser).open_order_url()
        OrderPage(browser).fill_client_info()
        OrderPage(browser).fill_metro_field_by_click()
        OrderPage(browser).click_on_button_forward()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.HEADING_ON_ABOUT_PAGE))
        expected_text = 'Про аренду'
        assert OrderPage(browser).find_text(OrderPageLocators.HEADING_ON_ABOUT_PAGE) == expected_text

