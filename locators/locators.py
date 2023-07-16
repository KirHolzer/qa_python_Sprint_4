from selenium.webdriver.common.by import By

class BasePageLocators:

    HEADER_YANDEX_LOGO = By.XPATH, ".//a[contains(@class, 'Header_LogoYandex__3TSOI')]"
    HEADER_SCOOTER_LOGO = By.XPATH, ".//a[contains(@class, 'Header_LogoScooter__3lsAR')]"
    HEADER_ORDER_BUTTON = By.XPATH,  ".//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button__ra12g')]"
    ACCEPT_COOKIE_BUTTON = By.XPATH, " .//button[contains(@class, 'App_CookieButton')]"
    COOKIE = By.XPATH, ".//div[contains(@class, 'App_CookieConsent__1yUIN')]"


class MainPaigeLocators:

    BODY_ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button__ra12g')]"
    MAIN_PAGE_HEADING = By.XPATH, ".//div[text() = 'Самокат ']"
    DZEN_LOGO = By.XPATH, "//a[@aria-label='Логотип Дзен']"
    QUESTION = By.XPATH, "//div[contains(@class, 'accordion__item')]"
    QUESTION_SECTION = By.XPATH, ".//div[@class = 'Home_FourPart__1uthg']"
    ANSWER = (By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]")


class OrderPageLocators:

    HEADING_ON_ORDER_PAGE = By.XPATH, ".//div[text() = 'Для кого самокат']"
    ORDER_CONTINUE_BUTTON = By.XPATH, ".//button[text() = 'Далее']"
    FIRST_NAME_INPUT = By.XPATH, ".//input[@placeholder='* Имя']"
    SECOND_NAME_INPUT = By.XPATH, ".//input[@placeholder='* Фамилия']"
    DELIVERY_ADDRESS_INPUT = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    PHONE_NUMBER_INPUT = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    METRO_STATION_INPUT = By.XPATH, ".//input[@placeholder = '* Станция метро']"
    DIV_METRO_SECTION = By.XPATH, ".//div[@class = 'select-search__select']"
    METRO_STATION_FOR_CLICK = By.XPATH, ".//button[@value = '9']"
    VALIDATE_ERROR_FIRST_NAME = By.XPATH, ".//div[text() = 'Введите корректное имя']"
    VALIDATE_ERROR_SECOND_NAME = By.XPATH, ".//div[text() = 'Введите корректную фамилию']"
    VALIDATE_ERROR_DELIVERY_ADDRESS = By.XPATH, ".//div[text() = 'Введите корректный адрес]"
    VALIDATE_ERROR_METRO_STATION = By.XPATH, ".//div[text() = 'Выберите станцию']"
    VALIDATE_ERROR_PHONE_NUMBER = By.XPATH, ".//div[text() = 'Введите корректный номер']"


class AboutRentLocators:

    HEADING_ON_ABOUT_PAGE = By.XPATH, ".//div[text() = 'Про аренду']"
    HEADING_ORDER_CONFIRMED =By.XPATH, ".//div[text() = 'Заказ оформлен']"
    LOOK_AT_STATUS = By.XPATH, ".//button[text() = 'Посмотреть статус']"
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

