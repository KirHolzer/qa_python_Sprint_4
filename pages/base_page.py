from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_start_url(self, page_url):
        self.driver.get(page_url)

    def find_element(self, element):
        return self.driver.find_element(*element)

    def click_on_element(self, element):
        self.find_element(element).click()

    def accept_cookie(self, element):
        self.click_on_element(element)

    def wait_element_visible(self, element, time=10):
        WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located(element))

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def add_value(self, element, value):
        self.find_element(element).send_keys(value)

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(element))
        self.find_element_located(element)

    def find_text(self, element):
        return self.find_element(element).text


    def find_element_located(self, element, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(element))

    def find_element_clickable(self, element, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(element))

    def find_element_not_located(self, element, time=10):
        return WebDriverWait(self.driver, time).until_not(expected_conditions.presence_of_element_located(element))

    def find_elements_located(self, element, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_all_elements_located(element))
