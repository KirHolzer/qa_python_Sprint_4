from selenium.webdriver.common.by import By

class BasePageLocators:

    HEADER_YANDEX_LOGO = By.XPATH, ".//a[contains(@class, 'Header_LogoYandex__3TSOI')]"
    HEADER_SCOOTER_LOGO = By.XPATH, ".//a[contains(@class, 'Header_LogoScooter__3lsAR')]"
    HEADER_ORDER_BUTTON = By.XPATH,  ".//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button__ra12g')]"
    ACCEPT_COOKIE_BUTTON = By.XPATH, " .//button[contains(@class, 'App_CookieButton')]"
    COOKIE = By.XPATH, ".//div[contains(@class, 'App_CookieConsent__1yUIN')]"
    # YaRuPopUP = By.ID, "distOverlayTitle"