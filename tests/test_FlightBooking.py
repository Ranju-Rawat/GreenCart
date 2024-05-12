import time

from selenium.webdriver.common import window
from selenium.webdriver.support import expected_conditions

from Pages.FBookingMainPage import Flight_Booking
from Pages.homePage import homePage
from Utilities.BaseClass import baseClass


class Test_FlightBooking(baseClass):

    def test_open_FlightScreen(self):
        HomePg = homePage(self.driver)
        original_window = self.driver.current_window_handle
        self.wait.until(expected_conditions.element_to_be_clickable(HomePg.flightButton)).click()
        self.open_New_window((original_window))
        print(self.driver.title)
        assert "Flight Booking" in self.driver.title, "Title mismatch: Expected 'Flight Booking' not found"

    def test_Search_flight(self):
        Flight_booking_pg = Flight_Booking(self.driver)
        log = self.loggingDemo()
        try:
            self.wait.until(expected_conditions.element_to_be_clickable(Flight_booking_pg.Depart_city)).send_keys("deh")
            selected_Dep_City = self.wait.until(
                expected_conditions.visibility_of_element_located(Flight_booking_pg.Depart_city)).get_attribute("value")
            assert "Dehradun" in selected_Dep_City
            self.wait.until(expected_conditions.element_to_be_clickable(Flight_booking_pg.Arrival_city)).click()
            self.wait.until(expected_conditions.element_to_be_clickable(Flight_booking_pg.Arrival_city_Name)).click()
            selected_Arrival_City = self.wait.until(
                expected_conditions.element_to_be_clickable(Flight_booking_pg.Arrival_city)).get_attribute("value")
            assert "BLR" in selected_Arrival_City
            self.wait.until(expected_conditions.element_to_be_clickable(Flight_booking_pg.Depart_Date)).click()
            Selected_Depart_Date = self.wait.until(
                expected_conditions.visibility_of_element_located(Flight_booking_pg.Selected_Depart_Date)).text
            assert Selected_Depart_Date == "Mon, Apr 29 2024"
            self.wait.until(expected_conditions.element_to_be_clickable(Flight_booking_pg.Arrival_Calendar)).click()
            self.wait.until(expected_conditions.element_to_be_clickable(Flight_booking_pg.Arrival_Date)).click()
            Selected_Arrival_Date = self.wait.until(
                expected_conditions.visibility_of_element_located(Flight_booking_pg.Selected_Arrival_Date)).text
            assert Selected_Arrival_Date == "Sat, May 18 2024"
            self.wait.until(expected_conditions.element_to_be_clickable(Flight_booking_pg.Passengers)).click()
            list_of_passengers = self.wait.until(
                expected_conditions.presence_of_all_elements_located(Flight_booking_pg.Passenger_options))
            self.wait.until(expected_conditions.element_to_be_clickable(Flight_booking_pg.Search_Button)).click()
        except Exception as e:
            print(f"An error occured : {str(e)}")
            screenshot = "C:\\Users\\rawat\\PycharmProjects\\GreenCart\\GreenCart\\Reports\\screenshot.png"
            self.driver.get_screenshot_as_file(screenshot)
            log.critical(str(e))





