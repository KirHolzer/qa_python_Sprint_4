from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, element):
        self.driver.find_element(*element).click()

    def wait_for_element_clickable_and_click(self, element):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(element)).click()