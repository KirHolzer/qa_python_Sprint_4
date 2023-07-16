import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPaigeLocators
from data.urls import TestUrls
from data.data import Answers
from pages.about_rent_page import AboutRentPage
from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.about_rent_locators import AboutRentLocators
import time

class TestAboutRentPage:

    def test_return_to_main_by_click_on_scooter_in_header(self, browser):
        OrderPage(browser).open_about_rent_page()
        AboutRentPage(browser).click_on_scooter_in_header()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(MainPaigeLocators.MAIN_PAGE_HEADING))
        assert browser.current_url == TestUrls.MainPageUrl

    def test_click_on_back_button(self, browser):
        OrderPage(browser).open_about_rent_page()
        AboutRentPage(browser).click_on_back_button()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.HEADING_ORDER_PAGE))
        expected_text = 'Для кого самокат'
        assert AboutRentPage(browser).find_text(OrderPageLocators.HEADING_ORDER_PAGE) == expected_text


    def test_go_to_modal_window(self, browser):
        OrderPage(browser).open_about_rent_page()
        AboutRentPage(browser).go_to_confirmation_modal_window()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AboutRentLocators.YES_BUTTON_MODAL))
        expected_text = 'Хотите оформить заказ?'
        assert AboutRentPage(browser).find_text(AboutRentLocators.HEADING_CONFIRMATION_MODAL).strip() == expected_text


    def test_return_to_about_rent_from_modal(self, browser):
        OrderPage(browser).open_about_rent_page()
        AboutRentPage(browser).click_no_button_on_confirmation_modal_window()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AboutRentLocators.BODY_ORDER_BUTTON))
        expected_text = 'Про аренду'
        assert AboutRentPage(browser).find_text(AboutRentLocators.HEADING_ON_ABOUT_PAGE) == expected_text


    def test_order_confirmed_successfully_from_order_button_header(self, browser):
        MainPage(browser).open_main_url()
        MainPage(browser).click_on_order_button_in_heeader()
        OrderPage(browser).open_about_rent_page()
        AboutRentPage(browser).click_yes_button_on_confirmation_modal_window()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AboutRentLocators.LOOK_AT_STATUS))
        expected_text = 'Заказ оформлен'
        assert AboutRentPage(browser).find_text(AboutRentLocators.HEADING_ORDER_CONFIRMED) == expected_text

    def test_order_confirmed_successfully_from_order_button_body(self, browser):
        MainPage(browser).open_main_url()
        MainPage(browser).scroll_to_order_button_in_body()
        MainPage(browser).click_on_order_button_in_body()
        OrderPage(browser).open_about_rent_page()
        AboutRentPage(browser).click_yes_button_on_confirmation_modal_window()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AboutRentLocators.LOOK_AT_STATUS))
        expected_text = 'Заказ оформлен'
        assert AboutRentPage(browser).find_text(AboutRentLocators.HEADING_ORDER_CONFIRMED) == expected_text






""" 
    def test_make_order_successfully(self, browser):
        OrderPage(browser).open_about_rent_page()
        AboutRentPage(browser).choose_delivery_date()
        AboutRentPage(browser).choose_rent_period()
        AboutRentPage(browser).choose_color()
        AboutRentPage(browser).fill_comment_for_courier()
        AboutRentPage(browser).

"""



