"""
bla
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from elements.elements import elements as E
from time import sleep
from base_test import BaseTest


# @pytest.mark.usefixtures("driver_init")
@pytest.mark.incremental
class TestBooking(BaseTest):
    """
    bla
    """
    @pytest.mark.parametrize("url", ["http://blazedemo.com/"])
    # @pytest.mark.search
    def test_search_flight(self, url):
        """
        bla
        """
        wait = WebDriverWait(self.driver, 3)
        # self.driver.get("http://blazedemo.com/")
        self.driver.get(url)
        # wait.until(EC.visibility_of_element_located((By.XPATH, E.elements.'check'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@value="Find Flights"]'))).click()
        # assert 0
        print(self.test_search_flight.__name__)
        sleep(1)

    def test_choose_any_flight(self):
        """
        bla
        """
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//td[contains(text(),'12')]/preceding-sibling::td"))).click()
        text = self.driver.find_element_by_tag_name("h2").text
        print(text)
        with pytest.raises(AssertionError):

            assert text == "Your flight from Paris to Boston has been reserved."
        print("Seems like you have booked incorrect flight!")
        print(self.test_choose_any_flight.__name__)
        sleep(1)
