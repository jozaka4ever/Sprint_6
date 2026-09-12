from selenium.webdriver.common.by import By

from texts import OrderPageTexts


class OrderPageLocators:
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
            f"//div[contains(@class, 'Dropdown-option') and "
            f"normalize-space()='{period}']",
        )

    @staticmethod
    def scooter_color(color):
        return By.CSS_SELECTOR, f"label[for='{color}']"
