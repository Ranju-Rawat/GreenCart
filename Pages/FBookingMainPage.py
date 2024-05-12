from selenium.webdriver.common.by import By


class Flight_Booking:

    def __init__(self, driver):
        self.driver = driver

    Depart_city = (By.CSS_SELECTOR, "#ctl00_mainContent_ddl_originStation1_CTXT")
    Arrival_city = (By.ID, "ctl00_mainContent_ddl_destinationStation1_CTXT")
    Arrival_city_Name = (By.PARTIAL_LINK_TEXT, "(BLR)")
    Depart_Date = (By.LINK_TEXT, "29")
    Selected_Depart_Date = (By.CSS_SELECTOR, "#view_fulldate_id_1")
    Arrival_Calendar = (By.CSS_SELECTOR, "#ctl00_mainContent_view_date2")
    Arrival_Date = (By.LINK_TEXT, "18")
    Selected_Arrival_Date = (By.CSS_SELECTOR, "#view_fulldate_id_2")
    Passengers = (By.ID, "divpaxinfo")
    Passenger_options = (By.ID, "divpaxOptions")
    Search_Button = (By.CSS_SELECTOR, "input[name = 'ctl00$mainContent$btn_FindFlights']")
