from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPaigeLocators
from data.urls import TestUrls




class MainPage(BasePage):

    def open_main_url(self):
        self.open_start_url(TestUrls.MainPageUrl)

    def click_yandex_logo_in_header(self):
        self.click_on_element(BasePageLocators.HEADER_YANDEX_LOGO)

    def click_on_scooter_in_header(self):
        self.click_on_element(BasePageLocators.HEADER_SCOOTER_LOGO)

    def click_on_order_button_in_heeader(self):
        self.click_on_element(BasePageLocators.HEADER_ORDER_BUTTON)

    def scroll_to_order_button_in_body(self):
        self.scroll_to(MainPaigeLocators.BODY_ORDER_BUTTON)

    def click_on_order_button_in_body(self):
        self.click_on_element(MainPaigeLocators.BODY_ORDER_BUTTON)

    def scroll_to_question_section(self):
        self.scroll_to(MainPaigeLocators.QUESTION_SECTION)

    def click_on_question(self, index):
        self.wait_element_visible(MainPaigeLocators.QUESTION_SECTION)
        questions = self.find_elements_located(MainPaigeLocators.QUESTION)
        questions[index].click()

    def get_answers(self):
        self.wait_element_visible(MainPaigeLocators.ANSWER)
        return self.find_element_located(MainPaigeLocators.ANSWER).text





#click_element(self.YANDEX_LOGO_BUTTON)


  #  def click_order_button_in_header(self, element):

