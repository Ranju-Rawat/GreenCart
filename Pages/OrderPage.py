from selenium.webdriver.common.by import By


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    OrderBtn = (By.CSS_SELECTOR, "button:nth-child(14)")
    countries = (By.XPATH, "//select")
    termAndCond = (By.CLASS_NAME, "chkAgree")
    submit = (By.TAG_NAME, "button")
