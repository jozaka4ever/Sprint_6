import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from texts import MainPageTexts
from urls import Urls


class MainPage(BasePage):
    COOKIE_BUTTON = (
        By.XPATH,
        f"//button[normalize-space()='{MainPageTexts.COOKIE_CONFIRM_BUTTON}']",
    )
    TOP_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Header_Nav')]"
        f"//button[normalize-space()='{MainPageTexts.ORDER_BUTTON}']",
    )
    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Home_FinishButton')]"
        f"//button[normalize-space()='{MainPageTexts.ORDER_BUTTON}']",
    )
    ORDER_BUTTONS = {
        "top": TOP_ORDER_BUTTON,
        "bottom": BOTTOM_ORDER_BUTTON,
    }
    SCOOTER_LOGO = (By.XPATH, "//a[.//img[@alt='Scooter']]")
    YANDEX_LOGO = (By.XPATH, "//a[.//img[@alt='Yandex']]")

    @staticmethod
    def faq_question(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def faq_answer(index):
        return By.ID, f"accordion__panel-{index}"

    @allure.step("Открыть главную страницу Самоката")
    def open_main_page(self):
        self.open(Urls.BASE_URL)
        self.close_cookie_banner()

    @allure.step("Закрыть баннер cookie, если он показан")
    def close_cookie_banner(self):
        self.click_if_visible(self.COOKIE_BUTTON)

    @allure.step("Открыть ответ на вопрос №{index}")
    def open_faq_item(self, index):
        self.click(self.faq_question(index))

    @allure.step("Получить ответ на вопрос №{index}")
    def get_faq_answer(self, index):
        return self.get_text(self.faq_answer(index))

    @allure.step("Начать заказ через точку входа: {entry_point}")
    def start_order(self, entry_point):
        try:
            locator = self.ORDER_BUTTONS[entry_point]
        except KeyError as error:
            raise ValueError(f"Неизвестная точка входа: {entry_point}") from error
        self.click(locator)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса и перейти в новую вкладку")
    def click_yandex_logo_and_switch(self):
        old_windows = self.driver.window_handles
        self.click(self.YANDEX_LOGO)
        self.switch_to_new_window(old_windows)
