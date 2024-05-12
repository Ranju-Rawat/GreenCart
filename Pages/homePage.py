from selenium.webdriver.common.by import By


class homePage:

    def __init__(self, driver):
        self.driver = driver

    vegList = (By.XPATH, "//div[@class='product']")
    vegNm = (By.XPATH, "//div[@class='product']/h4")
    AddToCardButton = (By.XPATH, "//div[@class = 'product-action']/button")
    CartButton = (By.CSS_SELECTOR, "a[class='cart-icon']")
    Search = (By.CSS_SELECTOR, "input[type='search']")
    SelectedProd = (By.CSS_SELECTOR, "p[class='product-name']")
    CheckOutButton = (By.XPATH, "//div[@class = 'cart-preview active']/div/button")
    flightButton = (By.PARTIAL_LINK_TEXT, "Flight")

