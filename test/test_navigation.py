import allure

from pages.main_page import MainPage
from urls import Urls


@allure.feature("Навигация по логотипам")
class TestNavigation:
    @allure.title("Логотип Самоката ведёт на главную страницу")
    def test_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.start_order("top")

        main_page.click_scooter_logo()

        assert main_page.is_current_url(Urls.BASE_URL)

    @allure.title("Логотип Яндекса открывает Яндекс в новой вкладке")
    def test_yandex_logo_opens_yandex_in_new_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_yandex_logo_and_switch()

        assert main_page.is_current_host(Urls.YANDEX_HOST)
