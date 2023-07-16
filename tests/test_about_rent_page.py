import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import OrderPageLocators, MainPaigeLocators, AboutRentLocators
from data.urls import TestUrls
from pages.about_rent_page import AboutRentPage
from pages.order_page import OrderPage
from pages.main_page import MainPage



class TestAboutRentPage:

    @allure.title('Проверка перехода на главную страницу по клику на "Самокат" со страницы "Про аренду"')
    @allure.description('Нажимаем на логотип "Самоката" и переходим на главную страницу')
    def test_return_to_main_by_click_on_scooter_in_header(self, browser):
        OrderPage(browser).open_about_rent_page()
        AboutRentPage(browser).click_on_scooter_in_header()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(MainPaigeLocators.MAIN_PAGE_HEADING))
        assert browser.current_url == TestUrls.MainPageUrl

    @allure.title('Проверка перехода на страницу заполнения клиентских данных по клику на кнопку "назад"')
    @allure.description('Нажимаем на кнопку "назад" и переходим на страницу заполнения клиентских данных')
    def test_click_on_back_button(self, browser):
        OrderPage(browser).open_about_rent_page()
        AboutRentPage(browser).click_on_back_button()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.HEADING_ON_ORDER_PAGE))
        expected_text = 'Для кого самокат'
        assert AboutRentPage(browser).find_text(OrderPageLocators.HEADING_ON_ORDER_PAGE) == expected_text

    @allure.title('Проверка перехода на модальную страницу подтверждения заказа')
    @allure.description('Заполняем поля "Про аренду" , переходим на модальную страницу подтверждения заказа')
    def test_go_to_modal_window(self, browser):
        OrderPage(browser).open_about_rent_page()
        AboutRentPage(browser).go_to_confirmation_modal_window()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AboutRentLocators.YES_BUTTON_MODAL))
        expected_text = 'Хотите оформить заказ?'
        assert AboutRentPage(browser).find_text(AboutRentLocators.HEADING_CONFIRMATION_MODAL).strip() == expected_text

    @allure.title('Проверка возврата на страницу "Про аренду" с модальноко окна подтверждения заказа')
    @allure.description('Заполняем поля "Про аренду" , переходим на модальную окно подтверждения заказа')
    def test_return_to_about_rent_from_modal(self, browser):
        OrderPage(browser).open_about_rent_page()
        AboutRentPage(browser).click_no_button_on_confirmation_modal_window()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AboutRentLocators.BODY_ORDER_BUTTON))
        expected_text = 'Про аренду'
        assert AboutRentPage(browser).find_text(AboutRentLocators.HEADING_ON_ABOUT_PAGE) == expected_text

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в правом верхнем углу главной страницы')
    @allure.description('Нажимаем на кнопку "Заказать" в правом верхнем углу страницы и проходим весь положительный '
                        'флоу оформления заказа')
    def test_order_confirmed_successfully_from_order_button_header(self, browser):
        MainPage(browser).open_main_url()
        MainPage(browser).click_on_order_button_in_heeader()
        OrderPage(browser).open_about_rent_page()
        AboutRentPage(browser).click_yes_button_on_confirmation_modal_window()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AboutRentLocators.LOOK_AT_STATUS))
        expected_text = 'Посмотреть статус'
        assert AboutRentPage(browser).find_text(AboutRentLocators.LOOK_AT_STATUS) == expected_text

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в нижней части главной страницы')
    @allure.description('Нажимаем на кнопку "Заказать" в нижней части главной страницы и проходим весь положительный '
                        'флоу оформления заказа')
    def test_order_confirmed_successfully_from_order_button_body(self, browser):
        MainPage(browser).open_main_url()
        MainPage(browser).scroll_to_order_button_in_body()
        MainPage(browser).click_on_order_button_in_body()
        OrderPage(browser).open_about_rent_page()
        AboutRentPage(browser).click_yes_button_on_confirmation_modal_window()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AboutRentLocators.LOOK_AT_STATUS))
        expected_text = 'Посмотреть статус'
        assert AboutRentPage(browser).find_text(AboutRentLocators.LOOK_AT_STATUS) == expected_text

