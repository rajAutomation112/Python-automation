


import pytest
from selenium import webdriver

from config.configreader import readdata
from utils.allureutil import attach_screenshot  # <-- fix import spelling

@pytest.fixture
def setup(request):
    # Read config data
    config_path = r"C:\Users\hp\PycharmProjects\pageObjectModelframework\config\config.ini"
    p = readdata(config_path)
    u = p.get("LoginData", "Base_url")
    c = p.get("LoginData", "Browser")
    user = p.get("LoginData", "Username")
    passw = p.get("LoginData", "Password")

    # Browser setup
    if c.lower() == "chrome":
        driver = webdriver.Chrome()
    elif c.lower() == "firefox":
        driver = webdriver.Firefox()
    elif c.lower() == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("Browser is not supported: " + c)

    # Attach driver to the test item for hooks
    request.node.driver = driver

    # Browser settings
    driver.maximize_window()
    driver.get(u)

    yield driver, user, passw
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    driver = getattr(item, "driver", None)
    if report.when == "call" and report.failed and driver:
        attach_screenshot(driver, name=f"{item.name}_failed")
