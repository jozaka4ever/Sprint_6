import allure
import pytest

from faq_data import FaqData
from pages.main_page import MainPage


@allure.feature("Вопросы о важном")
class TestFaq:
    @allure.story("Раскрытие ответа на вопрос")
    @pytest.mark.parametrize(
        "question_index, expected_answer",
        FaqData.CASES,
        ids=[f"faq-{index + 1}" for index, _ in FaqData.CASES],
    )
    def test_faq_answer_matches_question(
        self, driver, question_index, expected_answer
    ):
        allure.dynamic.title(f"Вопрос №{question_index + 1} открывает верный ответ")
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.open_faq_item(question_index)

        assert main_page.get_faq_answer(question_index) == expected_answer
