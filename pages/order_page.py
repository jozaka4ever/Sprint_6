from datetime import date, timedelta

import allure
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Заполнить первую страницу формы заказа")
    def fill_customer_details(self, order_data):
        self.type_text(OrderPageLocators.FIRST_NAME_INPUT, order_data.first_name)
        self.type_text(OrderPageLocators.LAST_NAME_INPUT, order_data.last_name)
        self.type_text(OrderPageLocators.ADDRESS_INPUT, order_data.address)
        self.type_text(OrderPageLocators.METRO_INPUT, order_data.metro_station)
        self.click(OrderPageLocators.metro_station(order_data.metro_station))
        self.type_text(OrderPageLocators.PHONE_INPUT, order_data.phone)

    @allure.step("Перейти ко второй странице формы заказа")
    def go_to_rent_details(self):
        self.click(OrderPageLocators.NEXT_BUTTON)
        self.find_visible(OrderPageLocators.DELIVERY_DATE_INPUT)

    @allure.step("Выбрать дату доставки через {days_from_today} дн.")
    def set_delivery_date(self, days_from_today):
        delivery_date = date.today() + timedelta(days=days_from_today)
        value = delivery_date.strftime("%d.%m.%Y")
        element = self.find_visible(OrderPageLocators.DELIVERY_DATE_INPUT)
        element.clear()
        element.send_keys(value)
        element.send_keys(Keys.ENTER)

    @allure.step("Выбрать срок аренды: {period}")
    def set_rental_period(self, period):
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.rental_period(period))

    @allure.step("Выбрать цвет самоката: {color}")
    def set_scooter_color(self, color):
        self.click(OrderPageLocators.scooter_color(color))

    @allure.step("Заполнить вторую страницу формы заказа")
    def fill_rent_details(self, order_data):
        self.set_delivery_date(order_data.delivery_days_from_today)
        self.set_rental_period(order_data.rental_period)
        self.set_scooter_color(order_data.color)
        self.type_text(OrderPageLocators.COMMENT_INPUT, order_data.comment)

    @allure.step("Подтвердить заказ")
    def submit_and_confirm_order(self):
        self.click(OrderPageLocators.SUBMIT_ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Проверить отображение сообщения об успешном заказе")
    def is_success_modal_displayed(self):
        return self.is_visible(OrderPageLocators.SUCCESS_MODAL)
