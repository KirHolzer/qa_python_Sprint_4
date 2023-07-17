import allure
from locators.locators import OrderPageLocators, AboutRentLocators
from data.urls import TestUrls
from pages.about_rent_page import AboutRentPage
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data.data import ExpectedText

@allure.feature('Действия на странице заказа "Про аренду". Полный сценария заказа')
class TestAboutRentPage:

    @allure.title('Проверка перехода на главную страницу по клику на "Самокат" со страницы "Про аренду"')
    @allure.description('Нажимаем на логотип "Самоката" и переходим на главную страницу')
    def test_return_to_main_by_click_on_scooter_in_header(self, browser):
        OrderPage(browser).open_about_rent_page(browser)
        about_rent_page = AboutRentPage(browser)
        about_rent_page.click_on_scooter_in_header(browser)
        assert browser.current_url == TestUrls.MainPageUrl, 'Произошёл некорректный редирект на главную ' \
                                                                       'страницу "Яндекс.Самокат"'

    @allure.title('Проверка перехода на страницу заполнения клиентских данных по клику на кнопку "назад"')
    @allure.description('Нажимаем на кнопку "назад" и переходим на страницу заполнения клиентских данных')
    def test_click_on_back_button(self, browser):
        OrderPage(browser).open_about_rent_page(browser)
        about_rent_page = AboutRentPage(browser)
        about_rent_page.click_on_back_button(browser)
        assert about_rent_page.find_text(OrderPageLocators.HEADING_ON_ORDER_PAGE) == ExpectedText.heading_on_order_page, 'Произошёл некорректный редирект при  ' \
                                                                                                                        'нажатии назад'

    @allure.title('Проверка перехода на модальную страницу подтверждения заказа')
    @allure.description('Заполняем поля "Про аренду" , переходим на модальную страницу подтверждения заказа')
    def test_go_to_modal_window(self, browser):
        OrderPage(browser).open_about_rent_page(browser)
        about_rent_page = AboutRentPage(browser)
        about_rent_page.go_to_confirmation_modal_window(browser)
        assert about_rent_page.find_text(AboutRentLocators.HEADING_CONFIRMATION_MODAL).strip() == ExpectedText.heading_on_confirmation_modal, 'Произошёл некорректный редирект на модалку' \
                                                                                                                                                'подтверждения заказа"'

    @allure.title('Проверка возврата на страницу "Про аренду" с модальноко окна подтверждения заказа')
    @allure.description('Заполняем поля "Про аренду" , возвращаемся на экран "про Аренду"')
    def test_return_to_about_rent_from_modal(self, browser):
        OrderPage(browser).open_about_rent_page(browser)
        about_rent_page = AboutRentPage(browser)
        about_rent_page.click_no_button_on_confirmation_modal_window(browser)
        assert about_rent_page.find_text(AboutRentLocators.HEADING_ON_ABOUT_PAGE) == ExpectedText.heading_about_rent, 'Произошёл некорректный возврат с  ' \
                                                                                                                            'с модального окна подтверждения"'

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в правом верхнем углу главной страницы')
    @allure.description('Нажимаем на кнопку "Заказать" в правом верхнем углу страницы и проходим весь положительный '
                        'флоу оформления заказа')
    def test_order_confirmed_successfully_from_order_button_header(self, browser):
        main_page = MainPage(browser)
        order_page = OrderPage(browser)
        about_rent_page = AboutRentPage(browser)
        main_page.open_main_url()
        main_page.click_on_order_button_in_heeader(browser)
        order_page.open_about_rent_page(browser)
        about_rent_page.click_yes_button_on_confirmation_modal_window(browser)
        assert about_rent_page.find_text(AboutRentLocators.LOOK_AT_STATUS) == ExpectedText.heading_look_at_status, 'Не удалось проверить статус заказа, поскольку номер заказа в урле ' \
                                                                                                                    'отсутствует либо не соответствует оформленному заказу'

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в нижней части главной страницы')
    @allure.description('Нажимаем на кнопку "Заказать" в нижней части главной страницы и проходим весь положительный '
                        'флоу оформления заказа')
    def test_order_confirmed_successfully_from_order_button_body(self, browser):
        main_page = MainPage(browser)
        order_page = OrderPage(browser)
        about_rent_page = AboutRentPage(browser)
        main_page.open_main_url()
        main_page.scroll_to_order_button_in_body(browser)
        main_page.click_on_order_button_in_body(browser)
        order_page.open_about_rent_page(browser)
        about_rent_page.click_yes_button_on_confirmation_modal_window(browser)
        assert about_rent_page.find_text(AboutRentLocators.LOOK_AT_STATUS) == ExpectedText.heading_look_at_status, 'Не удалось проверить статус заказа, поскольку номер заказа в урле ' \
                                                                                                                     'отсутствует либо не соответствует оформленному заказу'
