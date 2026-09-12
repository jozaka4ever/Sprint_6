from urllib.parse import urlparse

import allure
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    def find_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click(self, locator):
        element = self.find_clickable(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        element = self.wait.until(ec.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            # На главной странице декоративный самокат иногда перекрывает
            # центр нижних элементов FAQ, хотя сами элементы доступны.
            self.driver.execute_script("arguments[0].click();", element)

    def click_if_visible(self, locator, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator)
            ).click()
            return True
        except TimeoutException:
            return False

    def type_text(self, locator, value):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.find_visible(locator).text

    def is_visible(self, locator):
        try:
            self.find_visible(locator)
            return True
        except TimeoutException:
            return False

    def is_current_url(self, expected_url):
        try:
            self.wait.until(ec.url_to_be(expected_url))
            return True
        except TimeoutException:
            return False

    def is_current_host(self, expected_host):
        def current_host(driver):
            host = urlparse(driver.current_url).hostname or ""
            return host.removeprefix("www.")

        try:
            self.wait.until(lambda driver: current_host(driver) == expected_host)
            return True
        except TimeoutException:
            return False

    def switch_to_new_window(self, old_windows):
        self.wait.until(ec.new_window_is_opened(old_windows))
        new_window = next(
            handle for handle in self.driver.window_handles if handle not in old_windows
        )
        self.driver.switch_to.window(new_window)
