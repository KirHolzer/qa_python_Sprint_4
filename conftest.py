import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from data.urls import TestUrls

@pytest.fixture
def browser():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    #  driver.maximize_window()
    yield driver
    driver.quit()
