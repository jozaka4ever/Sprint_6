from datetime import date, timedelta

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from texts import OrderPageTexts


class OrderPage(BasePage):
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    METRO_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Станция метро')]")
    PHONE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    NEXT_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_NextButton')]"
        f"//button[normalize-space()='{OrderPageTexts.NEXT_BUTTON}']",
    )

    DELIVERY_DATE_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder, 'Когда привезти самокат')]",
    )
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    COMMENT_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder, 'Комментарий для курьера')]",
    )
    SUBMIT_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons')]"
        f"//button[normalize-space()='{OrderPageTexts.ORDER_BUTTON}']",
    )
    CONFIRM_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal')]"
        f"//button[normalize-space()='{OrderPageTexts.CONFIRM_BUTTON}']",
    )
    SUCCESS_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader') and "
        f"contains(., '{OrderPageTexts.SUCCESS_MODAL_HEADER}')]",
    )

    @staticmethod
    def metro_station(station_name):
        return (
            By.XPATH,
            f"//div[contains(@class, 'select-search__select')]"
            f"//div[normalize-space()='{station_name}']",
        )

    @staticmethod
    def rental_period(period):
        return (
            By.XPATH,
            f"//div[contains(@class, 'Dropdown-option') and normalize-space()='{period}']",
        )

    @staticmethod
    def scooter_color(color):
        return By.CSS_SELECTOR, f"label[for='{color}']"

    @allure.step("Заполнить первую страницу формы заказа")
    def fill_customer_details(self, order_data):
        self.type_text(self.FIRST_NAME_INPUT, order_data.first_name)
        self.type_text(self.LAST_NAME_INPUT, order_data.last_name)
        self.type_text(self.ADDRESS_INPUT, order_data.address)
        self.type_text(self.METRO_INPUT, order_data.metro_station)
        self.click(self.metro_station(order_data.metro_station))
        self.type_text(self.PHONE_INPUT, order_data.phone)

    @allure.step("Перейти ко второй странице формы заказа")
    def go_to_rent_details(self):
        self.click(self.NEXT_BUTTON)
        self.find_visible(self.DELIVERY_DATE_INPUT)

    @allure.step("Выбрать дату доставки через {days_from_today} дн.")
    def set_delivery_date(self, days_from_today):
        delivery_date = date.today() + timedelta(days=days_from_today)
        value = delivery_date.strftime("%d.%m.%Y")
        element = self.find_visible(self.DELIVERY_DATE_INPUT)
        element.clear()
        element.send_keys(value)
        element.send_keys(Keys.ENTER)

    @allure.step("Выбрать срок аренды: {period}")
    def set_rental_period(self, period):
        self.click(self.RENTAL_PERIOD_DROPDOWN)
        self.click(self.rental_period(period))

    @allure.step("Выбрать цвет самоката: {color}")
    def set_scooter_color(self, color):
        self.click(self.scooter_color(color))

    @allure.step("Заполнить вторую страницу формы заказа")
    def fill_rent_details(self, order_data):
        self.set_delivery_date(order_data.delivery_days_from_today)
        self.set_rental_period(order_data.rental_period)
        self.set_scooter_color(order_data.color)
        self.type_text(self.COMMENT_INPUT, order_data.comment)

    @allure.step("Подтвердить заказ")
    def submit_and_confirm_order(self):
        self.click(self.SUBMIT_ORDER_BUTTON)
        self.click(self.CONFIRM_ORDER_BUTTON)

    @allure.step("Проверить отображение сообщения об успешном заказе")
    def is_success_modal_displayed(self):
        return self.is_visible(self.SUCCESS_MODAL)
