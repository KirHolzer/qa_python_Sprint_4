import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()