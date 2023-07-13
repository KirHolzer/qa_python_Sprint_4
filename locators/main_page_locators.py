from selenium.webdriver.common.by import By


class MainPaigeLocators:

    BODY_ORDER_BUTTON = By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"
    MAIN_PAGE_HEADING = By.XPATH, ".//div[text() = 'Самокат ']"

    QUESTION = By.XPATH, "//div[contains(@class, 'accordion__item')]"
    QUESTION_SECTION = By.XPATH, ".//div[@class = 'Home_FourPart__1uthg']"
    ANSWER = (By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]")
