import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import OrderPageLocators, MainPaigeLocators, AboutRentLocators
from data.urls import TestUrls
from pages.order_page import OrderPage


@allure.feature('Действия на странице заказа "Для кого самокат" ')
class TestOrderPage:


    @allure.title('Проверка перехода на страницу "Про аренду" по клику на кнопку "Далее" после успешного заполнения клиентскими данными')
    @allure.description('Заполнить данные клиента и перейти на страницу "Про аренду"')
    def test_fill_client_info_succsesfully(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.fill_client_info()
        order_page.fill_metro_field_by_click()
        order_page.click_on_button_forward(browser)
        expected_text = 'Про аренду'
        assert order_page.find_text(AboutRentLocators.HEADING_ON_ABOUT_PAGE) == expected_text

    @allure.title('Проверка ошибки на валидацию поля "Имя"')
    @allure.description('Оставить поле "Имя" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_first_name(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.click_on_button_forward_for_validate_error(browser)

        expected_text = 'Введите корректное имя'
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_FIRST_NAME) == expected_text

    @allure.title('Проверка ошибки на валидацию поля "Фамилия"')
    @allure.description('Оставить поле "Фамилия" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_second_name(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.click_on_button_forward_for_validate_error(browser)
        expected_text = 'Введите корректную фамилию'
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_SECOND_NAME) == expected_text

    @allure.title('Проверка ошибки на валидацию поля "* Адрес: куда привезти заказ"')
    @allure.description('Оставить поле "* Адрес: куда привезти заказ" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_delivery_address(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.click_on_button_forward_for_validate_error(browser)
        expected_text = 'Введите корректный адрес'
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_DELIVERY_ADDRESS) == expected_text

    @allure.title('Проверка ошибки на валидацию поля "* Станция метро"')
    @allure.description('Оставить поле "* Станция метро" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_metro_station(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.click_on_button_forward_for_validate_error(browser)
        expected_text = 'Выберите станцию'
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_METRO_STATION) == expected_text

    @allure.title('Проверка ошибки на валидацию поля "* Номера телефона"')
    @allure.description('Оставить поле "* Номера телефона" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_phone_number(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.click_on_button_forward_for_validate_error(browser)
        expected_text = 'Введите корректный номер'
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_PHONE_NUMBER) == expected_text
