from selenium.webdriver.common.by import By

class AboutRentLocators:

    HEADING_ON_ABOUT_PAGE = By.XPATH, ".//div[text() = 'Про аренду']"
    HEADING_ORDER_CONFIRMED =By.XPATH, ".//div[text() = 'Заказ оформлен']"
    LOOK_AT_STATUS = By.XPATH, ".//button[text() = 'Заказ оформлен']"

    BACK_BUTTON = By.XPATH, ".//button[text() = 'Назад']"
    DELIVERY_DATE_INPUT = By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"
    CHOSE_DATE = By.XPATH, ".//div[contains(@class, 'react-datepicker__day--today')]"
    RENTAL_PERIOD = By.XPATH, ".//div[contains(@class, 'Dropdown-control')]"
    COMMENT_TO_COURIER_INPUT = By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"
    PERIOD_RENT_BUTTON = By.XPATH, ".//div[text() = '* Срок аренды']"
    CHOSE_RENT_PERIOD = By.XPATH, ".//div[text() = 'двое суток']"
    BLACK_COLOR = By.ID, 'black'
    BODY_ORDER_BUTTON = By.XPATH, ".//button[contains(@class, 'Button_Middle__1CSJM')and text() = 'Заказать']"
    HEADING_CONFIRMATION_MODAL = By.XPATH, ".//div[text() = 'Хотите оформить заказ?']"
    YES_BUTTON_MODAL = By.XPATH, ".//button[text() = 'Да']"
    NO_BUTTON_MODAL = By.XPATH, ".//button[text() = 'Да']"

