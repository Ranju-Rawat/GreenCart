from selenium.webdriver.common.by import By


class HotelBooking:

    def __init__(self, driver):
        self.driver = driver

    open_Hotel_Screen = (By.CSS_SELECTOR, "li[class='myspice_trip']")
    Destination_City = (By.ID, "ctl00_mainContent_txtOriginStation1_MST")