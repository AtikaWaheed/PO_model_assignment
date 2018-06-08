from utility_page import UtilityPage
from selenium.webdriver.common.keys import Keys


class FirstPageExecution(UtilityPage):
    """
    Execute ist page
    """
    def enter_correct_values(self, **kwargs):
        """
        :param kwargs: id is index fethced from question list
        :param kwargs: values are the manual answsers which we consider to fill the form
        """
        value = self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsTextTextItem')[
            kwargs.get('id')].find_element_by_css_selector('.quantumWizTextinputPaperinputInputArea > input')
        value.send_keys(Keys.BACKSPACE)
        value.send_keys(kwargs.get('enter_values'))
