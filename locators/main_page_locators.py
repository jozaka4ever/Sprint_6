from selenium.webdriver.common.by import By

from texts import MainPageTexts


class MainPageLocators:
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
