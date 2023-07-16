import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import OrderPageLocators, MainPaigeLocators, AboutRentLocators
from data.urls import TestUrls
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка перехода на главную страницу по клику на "Самокат" со страницы заказа')
    @allure.description('Нажимаем на логотип "Самоката" и переходим на главную страницу')
    def test_return_to_main_by_click_on_scooter_in_header(self, browser):
        OrderPage(browser).open_order_url()
        OrderPage(browser).click_on_scooter_in_header()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(MainPaigeLocators.MAIN_PAGE_HEADING))
        assert browser.current_url == TestUrls.MainPageUrl

    @allure.title('Проверка перехода на страницу "Про аренду" по клику на кнопку "Далее" после успешного заполнения клиентскими данными')
    @allure.description('Заполнить данные клиента и перейти на страницу "Про аренду"')
    def test_fill_client_info_succsesfully(self, browser):
        OrderPage(browser).open_order_url()
        OrderPage(browser).fill_client_info()
        OrderPage(browser).fill_metro_field_by_click()
        OrderPage(browser).click_on_button_forward()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AboutRentLocators.HEADING_ON_ABOUT_PAGE))
        expected_text = 'Про аренду'
        assert OrderPage(browser).find_text(AboutRentLocators.HEADING_ON_ABOUT_PAGE) == expected_text

    @allure.title('Проверка ошибки на валидацию поля "Имя"')
    @allure.description('Оставить поле "Имя" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_first_name(self, browser):
        OrderPage(browser).open_order_url()
        OrderPage(browser).click_on_button_forward()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.VALIDATE_ERROR_FIRST_NAME))
        expected_text = 'Введите корректное имя'
        assert OrderPage(browser).find_text(OrderPageLocators.VALIDATE_ERROR_FIRST_NAME) == expected_text

    @allure.title('Проверка ошибки на валидацию поля "Фамилия"')
    @allure.description('Оставить поле "Фамилия" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_second_name(self, browser):
        OrderPage(browser).open_order_url()
        OrderPage(browser).click_on_button_forward()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.VALIDATE_ERROR_SECOND_NAME))
        expected_text = 'Введите корректную фамилию'
        assert OrderPage(browser).find_text(OrderPageLocators.VALIDATE_ERROR_SECOND_NAME) == expected_text

    @allure.title('Проверка ошибки на валидацию поля "* Адрес: куда привезти заказ"')
    @allure.description('Оставить поле "* Адрес: куда привезти заказ" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_delivery_address(self, browser):
        OrderPage(browser).open_order_url()
        OrderPage(browser).click_on_button_forward()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.VALIDATE_ERROR_FIRST_NAME))
        expected_text = 'Введите корректный адрес'
        assert OrderPage(browser).find_text(OrderPageLocators.VALIDATE_ERROR_DELIVERY_ADDRESS) == expected_text

    @allure.title('Проверка ошибки на валидацию поля "* Станция метро"')
    @allure.description('Оставить поле "* Станция метро" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_metro_station(self, browser):
        OrderPage(browser).open_order_url()
        OrderPage(browser).click_on_button_forward()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.VALIDATE_ERROR_METRO_STATION))
        expected_text = 'Выберите станцию'
        assert OrderPage(browser).find_text(OrderPageLocators.VALIDATE_ERROR_METRO_STATION) == expected_text

    @allure.title('Проверка ошибки на валидацию поля "* Номера телефона"')
    @allure.description('Оставить поле "* Номера телефона" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_phone_number(self, browser):
        OrderPage(browser).open_order_url()
        OrderPage(browser).click_on_button_forward()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.VALIDATE_ERROR_PHONE_NUMBER))
        expected_text = 'Введите корректный номер'
        assert OrderPage(browser).find_text(OrderPageLocators.VALIDATE_ERROR_PHONE_NUMBER) == expected_text

