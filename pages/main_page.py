import allure
from pages.base_page import BasePage
from locators.locators import BasePageLocators, MainPaigeLocators
from data.urls import TestUrls


class MainPage(BasePage):

    @allure.step('Открыть главную страницу')
    def open_main_url(self):
        self.open_start_url(TestUrls.MainPageUrl)

    @allure.step('Кликнуть по логотипу в хедере')
    def click_yandex_logo_in_header(self):
        self.click_on_element(BasePageLocators.HEADER_YANDEX_LOGO)

    @allure.step('Кликнуть по логотипу самоката в хедере')
    def click_on_scooter_in_header(self):
        self.click_on_element(BasePageLocators.HEADER_SCOOTER_LOGO)

    @allure.step('Кликнтуь по кнопке "Заказать" в хедере')
    def click_on_order_button_in_heeader(self):
        self.click_on_element(BasePageLocators.HEADER_ORDER_BUTTON)

    @allure.step('Проскролить до кнопки заказать в body')
    def scroll_to_order_button_in_body(self):
        self.scroll_to(MainPaigeLocators.BODY_ORDER_BUTTON)

    @allure.step('Кликнуть по кнопке "Заказать" в body')
    def click_on_order_button_in_body(self):
        self.click_on_element(MainPaigeLocators.BODY_ORDER_BUTTON)

    @allure.step('Проскролить до секции вопросов')
    def scroll_to_question_section(self):
        self.scroll_to(MainPaigeLocators.QUESTION_SECTION)

    @allure.step('Кликнуть на вопрос')
    def click_on_question(self, index):
        self.wait_element_visible(MainPaigeLocators.QUESTION_SECTION)
        questions = self.find_elements_located(MainPaigeLocators.QUESTION)
        questions[index].click()

    @allure.step('Получить ответ')
    def get_answers(self):
        self.wait_element_visible(MainPaigeLocators.ANSWER)
        return self.find_element_located(MainPaigeLocators.ANSWER).text
