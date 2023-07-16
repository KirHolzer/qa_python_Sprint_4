from selenium.webdriver.common.by import By

class OrderPageLocators:

    HEADING_ORDER_PAGE = By.XPATH, ".//div[text() = 'Для кого самокат']"

    ORDER_CONTINUE_BUTTON = By.XPATH, ".//button[text() = 'Далее']"
    FIRST_NAME_INPUT = By.XPATH, ".//input[@placeholder='* Имя']"
    SECOND_NAME_INPUT = By.XPATH, ".//input[@placeholder='* Фамилия']"
    DELIVERY_ADDRESS_INPUT = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    PHONE_NUMBER_INPUT = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    METRO_STATION_INPUT = By.XPATH, ".//input[@placeholder = '* Станция метро']"
    DIV_METRO_SECTION = By.XPATH, ".//div[@class = 'select-search__select']"
    METRO_STATION_FOR_CLICK = By.XPATH, ".//button[@value = '9']" #".//ul/li//button[@value = '9']"
    HEADING_ON_ABOUT_PAGE = By.XPATH, ".//div[text() = 'Про аренду']"

    VALIDATE_ERROR_FIRST_NAME = By.XPATH, ".//div[text() = 'Введите корректное имя']"
    VALIDATE_ERROR_SECOND_NAME = By.XPATH, ".//div[text() = 'Введите корректную фамилию']"
    VALIDATE_ERROR_DELIVERY_ADDRESS = By.XPATH, ".//div[text() = 'Введите корректный адрес]"
    VALIDATE_ERROR_METRO_STATION = By.XPATH, ".//div[text() = 'Выберите станцию']"
    VALIDATE_ERROR_PHONE_NUMBER = By.XPATH, ".//div[text() = 'Введите корректный номер']"

    """
    STATION_LOCATOR = (By.XPATH, "//input[@placeholder='* Станция метро']")
    REQUIRED_STATION_LOCATOR = (By.XPATH, "//ul/li/button[@value='103']")
    """





