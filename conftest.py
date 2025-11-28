import pytest
import json
from pathlib import Path
import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

import utils.locators_utils as locators_utils

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name").lower()

    if browser_name == "chrome":
        options = ChromeOptions()
        drv = webdriver.Chrome(service=ChromeService(), options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        drv = webdriver.Firefox(service=FirefoxService(), options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        drv = webdriver.Edge(service=EdgeService(), options=options)
    else:
        options = ChromeOptions()
        drv = webdriver.Chrome(service=ChromeService(), options=options)

    yield drv
    try:
        drv.quit()
    except:
        pass

@pytest.fixture(scope="function")
def driver(browser):
    return browser

@pytest.fixture(scope="session")
def test_data():
    root = Path(__file__).parent
    json_path = root / "Data" / "train_test_data.json"
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture(scope="function")
def locators():
    return locators_utils

@pytest.fixture(scope="function")
def setup(browser, request):
    browser.get("https://www.redbus.in")
    browser.maximize_window()
    browser.implicitly_wait(5)
    request.cls.driver = browser
    yield browser
    try:
        browser.quit()
    except:
        pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = None
        try:
            driver = item.funcargs.get("driver")
        except Exception:
            driver = None
        if not driver:
            instance = getattr(item, "instance", None)
            if instance:
                driver = getattr(instance, "driver", None)

        if not driver:
            return
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        _ensure_dir(screenshot_dir)

        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        safe_name = getattr(item, "name", "test").replace("/", "_")
        file_name = f"{safe_name}_{time_stamp}.png"
        screenshot_path = os.path.join(screenshot_dir, file_name)

        try:
            driver.save_screenshot(screenshot_path)
        except Exception as e:
            print(f"[HOOK] could not take screenshot: {e}")
            return
        try:
            from pytest_html import extras
            extra = getattr(report, "extra", [])
            extra.append(extras.image(screenshot_path))
            report.extra = extra
        except Exception:
            print("[HOOK] pytest-html not available; screenshot saved to:", screenshot_path)


def pytest_configure(config):
    html_opt = getattr(config.option, "htmlpath", None)
    if not html_opt:
        _ensure_dir("reports")
        ts = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        config.option.htmlpath = os.path.join("reports", f"Test_Report_{ts}.html")
def _ensure_dir(path):
    try:
        os.makedirs(path, exist_ok=True)
    except Exception:
        pass
