from selenium.webdriver.common.keys import Keys
from utility_page import UtilityPage
import time


class NinthPageExecution(UtilityPage):
    """
    Execute Ninth page which is about to select dates
    """
    def enter_date(self, **kwargs):
        """
        Enter current date and time which is fetched from dictionary
        :param kwargs: * values have the current month which is fetched from dict
                       * value1 has the current day which is fetched from dict
        :return:
        """
        mon = self.driver.find_element_by_css_selector("input[aria-label='Month']")
        # mon is month field
        mon.send_keys(Keys.BACKSPACE)
        mon.send_keys(kwargs.get('fist_value'))
        self.driver.find_element_by_css_selector("input[aria-label='Day of the month']").send_keys(kwargs.get('second_value'))

    def enter_time(self, **kwargs):
        """

        :param kwargs: * values have the current hour which is fetched from dict
                       * value1 has the current minute which is fetched from dict
        :return:
        """
        from nose.tools import set_trace;set_trace()
        hr = self.driver.find_element_by_css_selector("input[aria-label='Hour']")
        hr.click()
        # hr is hour field
        hr.send_keys(Keys.BACKSPACE)
        hr.send_keys(kwargs.get('fist_value'))
        mn = self.driver.find_element_by_css_selector("input[aria-label='Minute']")
        # min is minute field
        mn.send_keys(Keys.BACKSPACE)
        mn.send_keys(kwargs.get('second_value'))
