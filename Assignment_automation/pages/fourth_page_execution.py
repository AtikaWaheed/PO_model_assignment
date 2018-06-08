from utility_page import UtilityPage
from selenium.common.exceptions import NoSuchElementException


class FourthPageExecution(UtilityPage):
    """
    Fourth Page execute which is 'Dropdown'
    """
    def capital_answers(self, id):
        """
        Select Capitals of Pakistan and Punjab
        :param: * id is index which is fetched from question heading list
        """
        self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            id].find_element_by_css_selector('.quantumWizMenuPaperselectContent').click()
        try:
            self.driver.find_element_by_css_selector('.exportSelectPopup [data-value="Islamabad"]').click()
        except NoSuchElementException:
            self.driver.find_element_by_css_selector('.exportSelectPopup [data-value="Lahore"]').click()
