import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):
    @allure.step("Открыть главную страницу Самоката")
    def open_main_page(self):
        self.open(Urls.BASE_URL)
        self.close_cookie_banner()

    @allure.step("Закрыть баннер cookie, если он показан")
    def close_cookie_banner(self):
        self.click_if_visible(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Открыть ответ на вопрос №{index}")
    def open_faq_item(self, index):
        self.click(MainPageLocators.faq_question(index))

    @allure.step("Получить ответ на вопрос №{index}")
    def get_faq_answer(self, index):
        return self.get_text(MainPageLocators.faq_answer(index))

    @allure.step("Начать заказ через точку входа: {entry_point}")
    def start_order(self, entry_point):
        try:
            locator = MainPageLocators.ORDER_BUTTONS[entry_point]
        except KeyError as error:
            raise ValueError(f"Неизвестная точка входа: {entry_point}") from error
        self.click(locator)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса и перейти в новую вкладку")
    def click_yandex_logo_and_switch(self):
        old_windows = self.driver.window_handles
        self.click(MainPageLocators.YANDEX_LOGO)
        self.switch_to_new_window(old_windows)
