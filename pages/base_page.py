from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_start_url(self, page_url):
        self.driver.get(page_url)

    def find_element(self, element):
        self.driver.find_element(*element)

    def click_on_element(self, element):
        self.driver.find_element(*element).click()

    def accept_cookie(self):
        self.click_on_element(BasePageLocators.ACCEPT_COOKIE_BUTTON)

    def add_value(self, element, value):
        self.driver.find_element(*element).send_keys(value)

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element))

    def find_text(self, element):
        return self.driver.find_element(*element).text

    def wait_element_visible(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element))

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator))

    def find_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_all_elements_located(locator))

