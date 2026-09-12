import os

import allure
import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver(request):
    options = Options()
    if os.getenv("HEADLESS") == "1":
        options.add_argument("-headless")

    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1440, 1000)
    browser.set_page_load_timeout(30)

    try:
        yield browser
    finally:
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            try:
                allure.attach(
                    browser.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG,
                )
            except WebDriverException:
                # Ошибка создания скриншота не должна мешать закрытию Firefox.
                pass
        browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
