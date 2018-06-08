import os
import unittest
from selenium import webdriver
from ..pages.utility_page import UtilityPage
from selenium.common.exceptions import NoSuchElementException
from ..pages.login_page import LoginPage
import time


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.utility_page = UtilityPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.utility_page.visit()

    def test_login_scenarios(self):
        """
        Verify Login Page
        """
        # from nose.tools import set_trace;set_trace()
        query1 = os.environ.get("username")
        query2 = os.environ.get("password")
        try:
            self.login_page.sign_in_popup()
            # self.login_page.wait_for_page()
            self.login_page.login(query1, query2)
        except NoSuchElementException:
            self.utility_page.visit()
            self.login_page.sign_in_button()

    def tearDown(self):
            """
            Verify page has closed
            """
            self.driver.close()
            #self.driver.quit()


if __name__ == "__main__":
        unittest.main()
