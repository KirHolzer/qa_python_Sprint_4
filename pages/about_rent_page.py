import allure
from pages.base_page import BasePage
from data.data import Comments
from locators.locators import BasePageLocators, AboutRentLocators


class AboutRentPage(BasePage):

    @allure.step('Клик на логотип самоката')
    def click_on_scooter_in_header(self):
        self.click_on_element(BasePageLocators.HEADER_SCOOTER_LOGO)

    @allure.step('Клик на кнопку "Назад"')
    def click_on_back_button(self):
        self.click_on_element(AboutRentLocators.BACK_BUTTON)

    @allure.step('Выбрать "Когда привезти самокат"')
    def choose_delivery_date(self):
        self.click_on_element(AboutRentLocators.DELIVERY_DATE_INPUT)
        self.click_on_element(AboutRentLocators.CHOSE_DATE)

    @allure.step('Выбрать срок аренды')
    def choose_rent_period(self):
        self.click_on_element(AboutRentLocators.RENTAL_PERIOD)
        self.click_on_element(AboutRentLocators.CHOSE_RENT_PERIOD)

    @allure.step('Выбрать цвет самоката')
    def choose_color(self):
        self.click_on_element(AboutRentLocators.BLACK_COLOR)

    @allure.step('Заполнить поле ввода "Комментарий для курьера"')
    def fill_comment_for_courier(self):
        self.add_value(AboutRentLocators.COMMENT_TO_COURIER_INPUT, Comments.comments)

    @allure.step('Кликнуть на кнопку "Заказать" , чтобы перейти на модальное окно подтверждения')
    def go_to_confirmation_modal_window(self):
        self.choose_delivery_date()
        self.choose_rent_period()
        self.choose_color()
        self.fill_comment_for_courier()
        self.click_on_element(AboutRentLocators.BODY_ORDER_BUTTON)

    @allure.step('Кликнуть на кнопку "Нет" в модальном окне подтверждения заказа')
    def click_no_button_on_confirmation_modal_window(self):
        self.go_to_confirmation_modal_window()
        self.click_on_element(AboutRentLocators.NO_BUTTON_MODAL)

    @allure.step('Кликнуть на кнопку "Да" в модальном окне подтверждения заказа')
    def click_yes_button_on_confirmation_modal_window(self):
        self.go_to_confirmation_modal_window()
        self.click_on_element(AboutRentLocators.YES_BUTTON_MODAL)
