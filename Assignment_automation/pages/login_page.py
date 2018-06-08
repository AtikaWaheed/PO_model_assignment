import time
from utility_page import UtilityPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(UtilityPage):

    def wait_for_page(self):
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#headingText'))
        )

    def login(self, username, password):
        """
        :param username: Enter username
        :param password: Enter password
        """
        # from nose.tools import set_trace;set_trace()
        user = WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
        )
        user.send_keys(username)
        time.sleep(5)
        user.send_keys(Keys.RETURN)
        time.sleep(5)
        # passcode is password field
        passcode = WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
        )
        passcode.send_keys(password)
        time.sleep(5)
        passcode.send_keys(Keys.RETURN)
        time.sleep(5)

    def sign_in_button(self):
        """
        Click sigIn button
        """
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.freebirdFormviewerViewMelbaSignInMsg'))
        ).click()

    def sign_in_popup(self):
        sign_in = WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#quantumwizdialogariabyid0'))
         )
        sign_in.send_keys(Keys.TAB)
        sign_in.send_keys(Keys.ENTER)
