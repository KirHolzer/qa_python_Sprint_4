import allure
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import OrderPageLocators, MainPaigeLocators, AboutRentLocators, BasePageLocators
from data.urls import TestUrls
from data.generators import GeneratedData


class OrderPage(BasePage):

    @allure.step('Открыть страницу заказа')
    def open_order_url(self):
        self.open_start_url(TestUrls.OrderPageUrl)
        self.accept_cookie()


    @allure.step('Кликнуть на кнопку "Далее"')
    def click_on_button_forward(self, browser):
        self.click_on_element(OrderPageLocators.ORDER_CONTINUE_BUTTON)
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AboutRentLocators.HEADING_ON_ABOUT_PAGE))

    @allure.step('Кликнуть на кнопку "Далее" не заполняя поля ')
    def click_on_button_forward_for_validate_error(self, browser):
        self.click_on_element(OrderPageLocators.ORDER_CONTINUE_BUTTON)
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.VALIDATE_ERROR_FIRST_NAME))

    @allure.step('Заполнить информацию о клиенте')
    def fill_client_info(self):
        self.add_value(OrderPageLocators.FIRST_NAME_INPUT, GeneratedData.generate_first_name())
        self.add_value(OrderPageLocators.SECOND_NAME_INPUT, GeneratedData.generate_last_name())
        self.add_value(OrderPageLocators.DELIVERY_ADDRESS_INPUT, GeneratedData.generate_delivery_address())
        self.add_value(OrderPageLocators.PHONE_NUMBER_INPUT, GeneratedData.generate_phone_number())

    @allure.step('Заполнить поле метро')
    def fill_metro_field_by_click(self):
        self.click_on_element(OrderPageLocators.METRO_STATION_INPUT)
        self.click_on_element(OrderPageLocators.METRO_STATION_FOR_CLICK)

    @allure.step('Открыть страницу "Про аренду"')
    def open_about_rent_page(self):
        self.open_order_url()
        self.fill_client_info()
        self.fill_metro_field_by_click()
        self.click_on_button_forward()
