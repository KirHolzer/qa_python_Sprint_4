import allure
from data.urls import TestUrls
from pages.main_page import MainPage

@allure.feature('Действия на главной странице')
class TestMainPage:

    @allure.title('Кнопка cookie "Да все привыкли"')
    @allure.description('Нажимаем на кнопку "Да все привыкли" в правом нижнем углу страницы и проверям что блок куки принят и пропал')
    def test_accept_cookies_succsesfully(self, browser):
        main_page = MainPage(browser)
        main_page.open_main_url()
        main_page.close_cookie(browser)
        assert main_page.is_cookie_not_visible(), "Блок cookies не пропал с экрана"

    @allure.title('Проверка перехода из главной страницы на старницу "Яндекса" по клику на логотип ')
    @allure.description('Нажимаем на логотип "Яндекса" в хедере и переходим на страницу яндекса ')
    def test_click_yandex_logo_in_header(self, browser):
        main_page = MainPage(browser)
        main_page.open_main_url()
        main_page.click_yandex_logo_in_header()
        assert browser.current_url == TestUrls.YandexMainUrl,  'Произошёл некорректный редирект на страницу "Дзен"'

    @allure.title('Проверка при клике на "Самокат" в хеддере мы остаемся на главной странице')
    @allure.description('Нажимаем на самокат в хедере на главной странице')
    def test_click_on_scooter_in_header(self, browser):
        main_page = MainPage(browser)
        main_page.open_main_url()
        main_page.click_on_scooter_in_header()
        assert browser.current_url == TestUrls.MainPageUrl, 'Произошёл некорректный редирект на главную ' \
                                                                       'страницу "Яндекс.Самокат"'

    @allure.title('Проверка перехода на страницу заказа при клике на "Заказать" в хедере')
    @allure.description('Нажимаем на "Заказать" в хедере и преходим на страницу заказа')
    def test_click_on_order_button_in_header(self, browser):
        main_page = MainPage(browser)
        main_page.open_main_url()
        main_page.click_on_order_button_in_heeader(browser)
        assert browser.current_url == TestUrls.OrderPageUrl, 'Произошёл некорректный редирект на страницу ' \
                                                                       'заказа "Яндекс.Самокат" из хеддера'

    @allure.title('Проверка перехода на страницу заказа при клике на "Заказать" в body')
    @allure.description('Нажимаем на "Заказать" в body и преходим на страницу заказа')
    def test_click_on_order_button_in_body(self, browser):
        main_page = MainPage(browser)
        main_page.open_main_url()
        main_page.close_cookie(browser)
        main_page.scroll_to_order_button_in_body(browser)
        main_page.click_on_order_button_in_body(browser)
        assert browser.current_url == TestUrls.OrderPageUrl, 'Произошёл некорректный редирект на страницу ' \
                                                                       'заказа "Яндекс.Самокат" из body'
