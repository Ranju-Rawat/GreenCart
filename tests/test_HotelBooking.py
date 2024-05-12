import time

from selenium.webdriver.support import expected_conditions

from Pages.HotelBookingPage import HotelBooking
from Pages.homePage import homePage
from Utilities.BaseClass import baseClass


class Test_HotelBooking(baseClass):

    def test_Open_HotelBooking_Page(self):
        HomePg = homePage(self.driver)
        hotel_page = HotelBooking(self.driver)
        try:
            original_window = self.driver.current_window_handle
            self.wait.until(expected_conditions.element_to_be_clickable(HomePg.flightButton)).click()
            self.open_New_window(original_window)
            self.wait.until(expected_conditions.presence_of_element_located(hotel_page.open_Hotel_Screen)).click()
            print("Hotel Booking button element", self.driver.title)
        except Exception as e:
            print(f"Error : {str(e)}")

