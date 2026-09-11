import allure
import pytest

from order_data import OrderTestData
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:
    @allure.story("Позитивный сценарий заказа")
    @pytest.mark.parametrize(
        "order_data",
        OrderTestData.CASES,
        ids=[case.case_id for case in OrderTestData.CASES],
    )
    def test_order_can_be_created(self, driver, order_data):
        allure.dynamic.title(
            f"Заказ оформляется через точку входа: {order_data.entry_point}"
        )
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_main_page()

        main_page.start_order(order_data.entry_point)
        order_page.fill_customer_details(order_data)
        order_page.go_to_rent_details()
        order_page.fill_rent_details(order_data)
        order_page.submit_and_confirm_order()

        assert order_page.is_success_modal_displayed()
