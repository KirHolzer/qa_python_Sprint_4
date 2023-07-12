from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
class MainPage(BasePage):

    def click_order_button_in_header(self):
        self.wait_for_element_clickable_and_click(BasePageLocators.HEADER_OERDER_BUTTON).click()
