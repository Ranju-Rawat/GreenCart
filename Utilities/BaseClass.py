import os

import pytest
import inspect
import logging

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("preSetup")
class baseClass:

    def loggingDemo(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filePath = os.path.join("C:\\Users\\rawat\\PycharmProjects\\GreenCart\\GreenCart\\Reports", "logfile.log")
        fileHandler = logging.FileHandler(filePath)
        # fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def textFile(self, filePath, mode):
        try:
            with open(filePath, mode) as vegFile:
                vegToSelect = vegFile.read()
                vegFile.close()
                return vegToSelect
        except IOError:
            print("File does not exists")

    def sel_Dropdown(self, data):
        wait = WebDriverWait(self.driver, 5)
        val = wait.until(expected_conditions.element_to_be_clickable(data))
        option = Select(val)
        return option

    def open_New_window(self, original_window):
        self.wait.until(expected_conditions.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)


