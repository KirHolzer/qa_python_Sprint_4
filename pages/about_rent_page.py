from pages.order_page import OrderPage
from data.data import Comments
from locators.base_page_locators import BasePageLocators
from locators.about_rent_locators import AboutRentLocators


class AboutRentPage(OrderPage):

    def click_on_scooter_in_header(self):
        self.click_on_element(BasePageLocators.HEADER_SCOOTER_LOGO)

    def click_on_back_button(self):
        self.click_on_element(AboutRentLocators.BACK_BUTTON)
    #def input_date(self):

    def choose_delivery_date(self):
        self.click_on_element(AboutRentLocators.DELIVERY_DATE_INPUT)
        self.click_on_element(AboutRentLocators.CHOSE_DATE)

    def choose_rent_period(self):
        self.click_on_element(AboutRentLocators.RENTAL_PERIOD)
        self.click_on_element(AboutRentLocators.CHOSE_RENT_PERIOD)

    def choose_color(self):
        self.click_on_element(AboutRentLocators.BLACK_COLOR)

    def fill_comment_for_courier(self):
        #self.click_on_element(AboutRentLocators.COMMENT_TO_COURIER_INPUT)
        self.add_value(AboutRentLocators.COMMENT_TO_COURIER_INPUT, Comments.comments)

    def go_to_confirmation_modal_window(self):
        self.choose_delivery_date()
        self.choose_rent_period()
        self.choose_color()
        self.fill_comment_for_courier()
        self.click_on_element(AboutRentLocators.BODY_ORDER_BUTTON)

    def click_no_button_on_confirmation_modal_window(self):
        self.go_to_confirmation_modal_window()
        self.click_on_element(AboutRentLocators.NO_BUTTON_MODAL)

    def click_yes_button_on_confirmation_modal_window(self):
        self.go_to_confirmation_modal_window()
        self.click_on_element(AboutRentLocators.YES_BUTTON_MODAL)

