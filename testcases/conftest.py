import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


# Adding Browser Addoption Functionalities
def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        site = webdriver.Chrome()
        print("Launching the Chrome Browser")

    elif browser == "firefox":
        site = webdriver.Firefox()
        print("Launching the Firefox Browser")

    elif browser == "edge":
        site = webdriver.Edge()
        print("Launching the Edge Browser")

    # site = webdriver.Chrome(options=chrome_options)       #For Headless Method
    else:
        site = webdriver.Chrome()
        # print("Launching headless mode")
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        # site = webdriver.Chrome(options=chrome_options)

    site.implicitly_wait(5)
    site.maximize_window()
    return site

def pytest_metadata(metadata):
    # to Add
    metadata["Environment"] = "Test"
    metadata["Project Name"] = "OrangeHRM"
    metadata["Module Name"] = "Employee"
    metadata["Tester"] = "TestBot1"

    # To Remove
    metadata.pop("Packages", None)
    # metadata.popitem("Platform", None)
    metadata.pop("Plugins", None)


@pytest.fixture(params=[
    ("Admin", "admin123", "Pass"),
    ("Admin1", "admin123", "Fail"),
    ("Admin", "admin1234", "Pass"),
    ("Admin1", "admin1234", "Fail")
])
def getDataforLogin(request):
    return request.param
