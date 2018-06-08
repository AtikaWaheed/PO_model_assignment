from utility_page import UtilityPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class NoteDownScoresGet(UtilityPage):
    """
    First submit form
    Click 'view score' button
    Note total points get
    """
    def confirmation_message(self):
        """
        To confirm if form has submitted
        :return: 'Response has recorded message'
        """
        return WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.freebirdFormviewerViewResponseConfirmationMessage'))
        ).text

    def view_score(self):
        """
        Click view score button
        """
        # from nose.tools import set_trace;set_trace()
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.quantumWizButtonPaperbuttonLabel.exportLabel'))
        ).click()
        time.sleep(2)
        window = self.driver.window_handles[-1]
        time.sleep(2)
        self.driver.switch_to.window(window)

    def total_score(self):
        """
        :return: Note the score get
        """
        return self.driver.find_element_by_css_selector(".freebirdFormviewerViewHeaderGradeFraction").text
