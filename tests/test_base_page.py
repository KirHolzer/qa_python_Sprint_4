from locators.base_page_locators import BasePageLocators
from data.urls import TestUrls
from pages.base_page import BasePage
import time

class TestBasePage:

    def test_go_to_yandex_from_main_page_logo(self, browser):
        BasePage(browser).click_on_element(BasePageLocators.HEADER_YANDEX_LOGO)
        time.sleep(10)
        browser.switch_to.window(browser.window_handles[-1])
        assert browser.current_url == TestUrls.YandexMainUrl  # TestUrls.YandexMainUrl


