from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching Chrome")
    elif browser == 'Edge':
        driver = webdriver.Edge()
        print("Launching Edge")
    else:
        driver = webdriver.Chrome()
 #   driver.set_page_load_timeout(10)  # Specify the timeout value as needed
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser") # Returns the Browser value to setup method


################## HTML Report #####################

# This Hook adds environment info to HTML report
def pytest_configure(config):
    config._metadata = {
        "Project": "Automation nop commerce",
        "Project Module": "Customer",
        "Project Tester": "Vithika"
    }


