import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from data.urls import TestUrls
from data.data import Answers
from pages.main_page import MainPage
import time

class TestMainPage:

    def test_click_yandex_logo_in_header(self, browser):
        MainPage(browser).click_yandex_logo_in_header()
        time.sleep(10)
        browser.switch_to.window(browser.window_handles[-1])
        assert browser.current_url == TestUrls.YandexMainUrl  # РАБОТАЕТ !!!

    def test_click_on_scooter_in_header(self, browser):
        MainPage(browser).click_on_scooter_in_header()
        assert browser.current_url == TestUrls.MainPageUrl # РАБОТАЕТ !!!

    def test_click_on_order_button_in_header(self, browser):
        MainPage(browser).click_on_order_button_in_heeader()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.HEADING_ON_ORDER_PAGE))
        assert browser.current_url == TestUrls.OrderPageUrl  # РАБОТАЕТ !!!

    def test_click_on_order_button_in_body(self, browser):
        MainPage(browser).scroll_to_order_button_in_body()
        MainPage(browser).click_on_order_button_in_body()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.HEADING_ON_ORDER_PAGE))
        assert browser.current_url == TestUrls.OrderPageUrl #Разобраться с дивом куки

    @pytest.mark.parametrize("index", range(8))
    def test_click_on_questions(self, browser, index):
        MainPage(browser).scroll_to_question_section()
        MainPage(browser).click_on_question(index)
        answer = MainPage(browser).get_answers()
        assert answer == Answers.answers[index]









