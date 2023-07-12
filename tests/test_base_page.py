from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from data.urls import TestUrls
from pages.base_page import BasePage
import time

class TestBasePage:

    def test_go_to_yandex_from_base_logo(self, browser):
        BasePage(browser).click_on_element(BasePageLocators.HEADER_YANDEX_LOGO)
        time.sleep(10)
        browser.switch_to.window(browser.window_handles[-1])
        assert browser.current_url == TestUrls.YandexMainUrl  # TestUrls.YandexMainUrl

    def test_no_redirect_to_yandex_on_click_scooter_logo(self, browser):
        BasePage(browser).click_on_element(BasePageLocators.HEADER_SCOOTER_LOGO)
        assert browser.current_url == TestUrls.MainPageUrl

    def test_go_to_order_page_from_base(self, browser):
        BasePage(browser).click_on_element(BasePageLocators.HEADER_ORDER_BUTTON)
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.HEADING_ON_ORDER_PAGE))
        assert browser.current_url == TestUrls.OrderPageUrl


