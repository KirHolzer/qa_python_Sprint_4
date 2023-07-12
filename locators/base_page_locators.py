from selenium.webdriver.common.by import By

class BasePageLocators:

    HEADER_YANDEX_LOGO = By.XPATH, ".//a[contains(@class, 'Header_LogoYandex__3TSOI')]"
    HEADER_SCOOTER_LOGO = By.XPATH, ".//a[contains(@class, 'Header_LogoScooter__3lsAR')]"
    HEADER_ORDER_BUTTON = By.XPATH,  ".//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button__ra12g')]"
    # YaRuPopUP = By.ID, "distOverlayTitle"