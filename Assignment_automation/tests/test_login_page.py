from ..tests.test_utility_page import BaseTest
import os
from selenium.common.exceptions import NoSuchElementException
from ..pages.login_page import LoginPage
import time


class Login(BaseTest):

    def setUp(self):
        super(Login, self).setUp()
        self.login_page = LoginPage(self.driver)

    def test_login_scenarios(self):
        """
        Verify Login Page
        """
        query1 = os.environ.get("username")
        query2 = os.environ.get("password")
        try:
            self.login_page.sign_in_popup()
            time.sleep(5)
            self.login_page.wait_for_page()
            self.login_page.login('atika.waheed@arbisoft.com', '03044400510')
        except NoSuchElementException:
            self.utility_page.visit()
            self.login_page.sign_in_button()
