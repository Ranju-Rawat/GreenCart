import time
from selenium.webdriver.support import expected_conditions
from Pages.ConfirmationPage import ConfirmPage
from Pages.OrderPage import OrderPage
from Pages.homePage import homePage
from Utilities.BaseClass import baseClass


class Test_listScreen(baseClass):

    def test_TotalVegies(self):
        log = self.loggingDemo()
        print("this is main page")
        HomePg = homePage(self.driver)
        veglist = HomePg.vegList
        veggies = self.wait.until(expected_conditions.presence_of_all_elements_located(veglist))
        assert len(veggies) == 30
        log.info(veggies)


    def test_SelectVegies(self):
        log = self.loggingDemo()
        HomePg = homePage(self.driver)
        log.info("this is info")
        search = HomePg.Search
        searchTxt = self.wait.until(expected_conditions.element_to_be_clickable(search))
        SelectVeges = ["water", "pot", "cash"]
        for sv in SelectVeges:
            searchTxt.send_keys(sv)
            time.sleep(4)
            self.wait.until(expected_conditions.element_to_be_clickable(HomePg.AddToCardButton)).click()
            searchTxt.clear()

    def test_ProceedToCheckOut(self):
        HomePg = homePage(self.driver)
        ordPg = OrderPage(self.driver)
        vegToSelect = ["Water Melon - 1 Kg", "Potato - 1 Kg", "Cashews - 1 Kg"]
        Sel_veg = self.textFile("C:\\Users\\rawat\\PycharmProjects\\GreenCart\\GreenCart\\Reports\\veg.txt", "r")
        VegInCart = []
        self.wait.until(expected_conditions.element_to_be_clickable(HomePg.CartButton)).click()
        SelProducts = self.wait.until(expected_conditions.presence_of_all_elements_located(HomePg.SelectedProd))
        for prod in SelProducts:
            if prod.text != "":
                VegInCart.append(prod.text)
        assert VegInCart == vegToSelect
        self.wait.until(expected_conditions.element_to_be_clickable(HomePg.CheckOutButton)).click()
        self.wait.until(expected_conditions.element_to_be_clickable(ordPg.OrderBtn)).click()

    def test_FinalOrder(self):
        log = self.loggingDemo()
        ordPage = OrderPage(self.driver)
        select = self.sel_Dropdown(ordPage.countries)
        select.select_by_value("Bahrain")
        log.critical("This is critical")

        self.wait.until(expected_conditions.element_to_be_clickable(ordPage.termAndCond)).click()
        self.wait.until(expected_conditions.element_to_be_clickable(ordPage.submit)).click()
        screenShot_path = "C:\\Users\\rawat\\PycharmProjects\\GreenCart\\GreenCart\\Reports\\screenshot.png"
        self.driver.get_screenshot_as_file(screenShot_path)

    def test_ConfirmOrder(self):
        orderPg = ConfirmPage(self.driver)
        msg = self.wait.until(expected_conditions.visibility_of_element_located(orderPg.confirmMsg)).text
        assert "successfully" in msg
