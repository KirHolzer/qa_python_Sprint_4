import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from data.urls import TestUrls

@pytest.fixture
def browser():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(TestUrls.MainPageUrl)
    #driver.get('https://qa-scooter.praktikum-services.ru/')
    #  driver.maximize_window()
    yield driver
    driver.quit()
