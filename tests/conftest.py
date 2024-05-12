import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox", help="my option: type1 or type2"
    )


@pytest.fixture(scope="class")
def preSetup(request):
    headless_options = Options()
    headless_options.add_argument("headless")
    browserName = request.config.getoption("browser_name").lower()
    print(browserName)
    if "chrome" in browserName:
        driver_path = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=driver_path, options=headless_options)
    elif "edge" in browserName:
        driver_path = Service("C:\\Users\\rawat\\Downloads\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=driver_path, options=headless_options)
    elif "firefox" in browserName:
        option = Options()
        option.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        driver_path = Service("C:\\Users\\rawat\\Downloads\\geckodriver-v0.34.0-win32\\geckodriver.exe")
        # merge_option = merge_options(option, headless_options)
        # print("Merge_options", type(merge_option))
        driver = webdriver.Firefox(service=driver_path, options=option)
    else:
        print("Browser does not exists")

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    wait = WebDriverWait(driver, 5)
    request.cls.driver = driver
    request.cls.wait = wait
    yield driver
    time.sleep(10)
    driver.quit()

# @pytest.fixture(params=["water", "pot", "cash"])
# def SearchVeggies(request):
#     return request.param
