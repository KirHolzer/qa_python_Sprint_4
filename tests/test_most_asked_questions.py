import allure
import pytest
from data.data import Answers
from pages.main_page import MainPage

@allure.feature('Раздел часто задаваемых вопросов')
class TestMostAskedQuestions:
    @allure.title('Проверка списка часто задаваемых вопросов и ответов на главной странице')
    @allure.description('На главной странице ищем список часто задаваемых вопросов и ответов и проверяем корректность ответов')
    @pytest.mark.parametrize("index", range(8))
    def test_click_on_questions(self, browser, index):
        main_page = MainPage(browser)
        main_page.open_main_url()
        main_page.scroll_to_question_section()
        main_page.click_on_question(index)
        answer = main_page.get_answers()
        assert answer == Answers.answers[index], f'Получен некорректный текст ответа. Ожидалось: {Answers.answers[index]}'
