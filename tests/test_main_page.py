import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from locators.locators import OrderPageLocators, BasePageLocators, MainPaigeLocators
from data.urls import TestUrls
from data.data import Answers
from pages.main_page import MainPage

@allure.feature('Действия на главной странице')
class TestMainPage:

    @allure.title('Кнопка cookie "Да все привыкли"')
    @allure.description('Нажимаем на кнопку "Да все привыкли" в правом нижнем углу страницы и проверям что блок куки принят и пропал')
    def test_accept_cookies_succsesfully(self, browser):
        MainPage(browser).open_main_url()
        MainPage(browser).close_cookie(browser)
        WebDriverWait(browser, 10).until(
            expected_conditions.invisibility_of_element_located(BasePageLocators.COOKIE)
        )
        try:
            browser.find_element(*BasePageLocators.ACCEPT_COOKIE_BUTTON)
            assert False, "Элемент 'ACCEPT_COOKIE_BUTTON' найден"
        except NoSuchElementException:
            assert True

    @allure.title('Проверка перехода из главной страницы на старницу "Яндекса" по клику на логотип ')
    @allure.description('Нажимаем на логотип "Яндекса" в хедере и переходим на страницу яндекса ')
    def test_click_yandex_logo_in_header(self, browser):
        main_page = MainPage(browser)
        main_page.open_main_url()
        main_page.click_yandex_logo_in_header(browser)
        assert browser.current_url == TestUrls.YandexMainUrl

    @allure.title('Проверка при клике на "Самокат" в хеддере мы остаемся на главной странице')
    @allure.description('Нажимаем на самокат в хедере на главной странице')
    def test_click_on_scooter_in_header(self, browser):
        main_page = MainPage(browser)
        main_page.open_main_url()
        main_page.click_on_scooter_in_header()
        assert browser.current_url == TestUrls.MainPageUrl

    @allure.title('Проверка перехода на страницу заказа при клике на "Заказать" в хедере')
    @allure.description('Нажимаем на "Заказать" в хедере и преходим на страницу заказа')
    def test_click_on_order_button_in_header(self, browser):
        main_page = MainPage(browser)
        main_page.open_main_url()
        main_page.click_on_order_button_in_heeader(browser)
        assert browser.current_url == TestUrls.OrderPageUrl

    @allure.title('Проверка перехода на страницу заказа при клике на "Заказать" в body')
    @allure.description('Нажимаем на "Заказать" в body и преходим на страницу заказа')
    def test_click_on_order_button_in_body(self, browser):
        main_page = MainPage(browser)
        main_page.open_main_url()
        main_page.accept_cookie()
        main_page.scroll_to_order_button_in_body(browser)
        main_page.click_on_order_button_in_body(browser)
        assert browser.current_url == TestUrls.OrderPageUrl

    @allure.title('Проверка списка часто задаваемых вопросов и ответов на главной странице')
    @allure.description('На главной странице ищем список часто задаваемых вопросов и ответов и проверяем корректность ответов')
    @pytest.mark.parametrize("index", range(8))
    def test_click_on_questions(self, browser, index):
        main_page = MainPage(browser)
        main_page.open_main_url()
        main_page.scroll_to_question_section()
        main_page.click_on_question(index)
        answer = main_page.get_answers()
        assert answer == Answers.answers[index]
