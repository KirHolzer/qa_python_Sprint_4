import allure
from pages.base_page import BasePage
from data.data import Comments
from locators.locators import BasePageLocators, AboutRentLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import MainPaigeLocators, OrderPageLocators


class AboutRentPage(BasePage):

    @allure.step('Клик на логотип самоката')
    def click_on_scooter_in_header(self, browser):
        self.click_on_element(BasePageLocators.HEADER_SCOOTER_LOGO)
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(MainPaigeLocators.MAIN_PAGE_HEADING))

    @allure.step('Клик на кнопку "Назад"')
    def click_on_back_button(self, browser):
        self.click_on_element(AboutRentLocators.BACK_BUTTON)
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.HEADING_ON_ORDER_PAGE))

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
    def fill_comment_for_courier(self, comment=Comments.comments):
        self.add_value(AboutRentLocators.COMMENT_TO_COURIER_INPUT, comment)

    @allure.step('Кликнуть на кнопку "Заказать" , чтобы перейти на модальное окно подтверждения')
    def go_to_confirmation_modal_window(self, browser):
        self.choose_delivery_date()
        self.choose_rent_period()
        self.choose_color()
        self.fill_comment_for_courier()
        self.click_on_element(AboutRentLocators.BODY_ORDER_BUTTON)
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AboutRentLocators.YES_BUTTON_MODAL))

    @allure.step('Кликнуть на кнопку "Нет" в модальном окне подтверждения заказа')
    def click_no_button_on_confirmation_modal_window(self, browser):
        self.go_to_confirmation_modal_window(browser)
        self.click_on_element(AboutRentLocators.NO_BUTTON_MODAL)
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AboutRentLocators.BODY_ORDER_BUTTON))

    @allure.step('Кликнуть на кнопку "Да" в модальном окне подтверждения заказа')
    def click_yes_button_on_confirmation_modal_window(self, browser):
        self.go_to_confirmation_modal_window(browser)
        self.click_on_element(AboutRentLocators.YES_BUTTON_MODAL)
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AboutRentLocators.LOOK_AT_STATUS))
