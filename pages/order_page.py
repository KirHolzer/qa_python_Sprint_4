from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import BasePageLocators
from data.data import MetroStation
from data.urls import TestUrls
from data.generators import GeneratedData

class OrderPage(BasePage):

    def open_order_url(self):
        self.open_start_url(TestUrls.OrderPageUrl)


    def click_on_scooter_in_header(self):
        self.click_on_element(BasePageLocators.HEADER_SCOOTER_LOGO)

    def click_on_button_forward(self):
        self.click_on_element(OrderPageLocators.ORDER_CONTINUE_BUTTON)

    def fill_client_info(self):
        self.add_value(OrderPageLocators.FIRST_NAME_INPUT, GeneratedData.generate_first_name())
        self.add_value(OrderPageLocators.SECOND_NAME_INPUT, GeneratedData.generate_last_name())
        self.add_value(OrderPageLocators.DELIVERY_ADDRESS_INPUT, GeneratedData.generate_delivery_address())
        self.add_value(OrderPageLocators.PHONE_NUMBER_INPUT, GeneratedData.generate_phone_number())

    def fill_metro_field_by_click(self):
        self.click_on_element(OrderPageLocators.METRO_STATION_INPUT)
        self.click_on_element(OrderPageLocators.METRO_STATION_FOR_CLICK)

    def fill_metro_field_by_input(self):
        self.click_on_element(OrderPageLocators.METRO_STATION_INPUT)
        self.add_value(OrderPageLocators.METRO_STATION_INPUT,MetroStation.station)










