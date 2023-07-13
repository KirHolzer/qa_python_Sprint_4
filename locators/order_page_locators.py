from selenium.webdriver.common.by import By

class OrderPageLocators:

    HEADING_ON_ORDER_PAGE = By.XPATH, ".//div[text() = 'Для кого самокат']"
    ORDER_CONTINUE_BUTTON = By.XPATH, ".//button[text() = 'Далее']"
    FIRST_NAME_INPUT = By.XPATH, ".//input[@placeholder='* Имя']"
    SECOND_NAME_INPUT = By.XPATH, ".//input[@placeholder='* Фамилия']"
    DELIVERY_ADDRESS_INPUT = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    PHONE_NUMBER_INPUT = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    METRO_STATION_INPUT = By.XPATH, ".//input[@placeholder = '* Станция метро']"
    DIV_METRO_SECTION = By.XPATH, ".//div[@class = 'select-search__select']"
    METRO_STATION_FOR_CLICK = By.XPATH, ".//button[@value = '9']" #".//ul/li//button[@value = '9']"
    HEADING_ON_ABOUT_PAGE = By.XPATH, ".//div[text() = 'Про аренду']"
    """
    STATION_LOCATOR = (By.XPATH, "//input[@placeholder='* Станция метро']")
    REQUIRED_STATION_LOCATOR = (By.XPATH, "//ul/li/button[@value='103']")
    """





