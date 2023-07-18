import allure
from locators.locators import OrderPageLocators, AboutRentLocators
from pages.order_page import OrderPage
from data.data import ExpectedText as ExT


@allure.feature('Действия на странице заказа "Для кого самокат" ')
class TestOrderPage:

    @allure.title('Проверка перехода на страницу "Про аренду" по клику на кнопку "Далее" после успешного заполнения клиентскими данными')
    @allure.description('Заполнить данные клиента и перейти на страницу "Про аренду"')
    def test_fill_client_info_succsesfully(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.fill_client_info()
        order_page.fill_metro_field_by_click()
        order_page.click_on_button_forward()
        assert order_page.find_text(AboutRentLocators.HEADING_ON_ABOUT_PAGE) == ExT.heading_about_rent, 'Произошёл некорректный редирект на страницу' \
                                                                                                                ' про аренду '

    @allure.title('Проверка ошибки на валидацию поля "Имя"')
    @allure.description('Оставить поле "Имя" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_first_name(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.click_on_button_forward_for_validate_error()
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_FIRST_NAME) == ExT.messege_validate_first_name,  'нет ошибки о валидации' \
                                                                                                                            ' поля имя '

    @allure.title('Проверка ошибки на валидацию поля "Фамилия"')
    @allure.description('Оставить поле "Фамилия" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_second_name(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.click_on_button_forward_for_validate_error()
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_SECOND_NAME) == ExT.messege_validate_second_name,  'нет ошибки о валидации' \
                                                                                                                            ' поля фамилия '

    @allure.title('Проверка ошибки на валидацию поля "* Адрес: куда привезти заказ"')
    @allure.description('Оставить поле "* Адрес: куда привезти заказ" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_delivery_address(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.click_on_button_forward_for_validate_error()
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_DELIVERY_ADDRESS) == ExT.messege_validate_delivery_address,  'нет ошибки о валидации' \
                                                                                                                            ' поля адреса '

    @allure.title('Проверка ошибки на валидацию поля "* Станция метро"')
    @allure.description('Оставить поле "* Станция метро" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_metro_station(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.click_on_button_forward_for_validate_error()
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_METRO_STATION) == ExT.messege_validate_metro_station, 'нет ошибки о валидации' \
                                                                                                                        ' поля станции метро '

    @allure.title('Проверка ошибки на валидацию поля "* Номера телефона"')
    @allure.description('Оставить поле "* Номера телефона" пустым и кликнуть "Далее"')
    def test_validate_error_by_input_phone_number(self, browser):
        order_page = OrderPage(browser)
        order_page.open_order_url()
        order_page.click_on_button_forward_for_validate_error()
        assert order_page.find_text(OrderPageLocators.VALIDATE_ERROR_PHONE_NUMBER) == ExT.messege_validate_phone_number, 'нет ошибки о валидации' \
                                                                                                                      ' поля номера телефона'
