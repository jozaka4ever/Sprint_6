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

        main_page.wait_for_url(Urls.BASE_URL)
        assert driver.current_url == Urls.BASE_URL

    @allure.title("Логотип Яндекса открывает Яндекс или Дзен в новой вкладке")
    def test_yandex_logo_opens_expected_page_in_new_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_yandex_logo_and_switch()

        # На старом стенде переход завершался на dzen.ru, а актуальная версия
        # открывает ya.ru без дополнительного перенаправления.
        actual_host = main_page.wait_for_host(Urls.YANDEX_DESTINATION_HOSTS)
        assert actual_host in Urls.YANDEX_DESTINATION_HOSTS
