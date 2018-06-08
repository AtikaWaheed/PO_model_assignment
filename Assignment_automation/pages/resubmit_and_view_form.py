from utility_page import UtilityPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

#______________________
class ResubmitFormUsingStoredQuestions(UtilityPage):

    def edit_response(self):
        """
        Need to switch window first
        Click edit response link
        """
        self.driver.switch_to.window(self.driver.window_handles[0])
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.freebirdFormviewerViewResponseLinksContainer > a:nth-child(2)'))
        ).click()
        #self.driver.find_element_by_css_selector('.freebirdFormviewerViewResponseLinksContainer > a:nth-child(2)').click()
        #time.sleep(2)

    def first_uncheck_all_options(self, ind):
        """
        Need to uncheck all prechecked options
        :param ind: Ind describe each answer options
        """
        checked_options = self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            ind].find_elements_by_css_selector('.isChecked[aria-checked="true"]')
        # Loop : picking one by one all options from list and making them uncheck
        for option in checked_options:
            option.click()
            time.sleep(1)

    def correct_input_from_csv(self, ind, values):
        """
        Pick all correct answers from stored csv and put them into correct palaces
        :param ind: ind is fetched from a question div
        :param values: values are fetched next question from stored csv
        """
        self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            ind].find_element_by_css_selector('.docssharedWizToggleLabeledControl[aria-label="{hard_cord}"]'.format
                                                       (hard_cord=values)).click()

    def multiple_inputs_from_csv(self, values):
        """
        Some questions have multiple answers tp pick from csv
        :param values:  values are fetched next question from stored csv
        """
        self.driver.find_element_by_css_selector('.freebirdFormviewerViewItemList [aria-label="{hard_cord}"][aria-checked="false"]'.format
                                                 (hard_cord=values)).click()

    def view_submitted_form(self):
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.quantumWizButtonPaperbuttonLabel.exportLabel'))
        ).click()
        #self.driver.find_element_by_css_selector(".quantumWizButtonPaperbuttonLabel.exportLabel").click()
        #time.sleep(2)
        window = self.driver.window_handles[-2]
        self.driver.switch_to.window(window)
