import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    """
    Base class to initialize the base page and will be call out from all pages
    """
    time_to_wait = 20

    def __init__(self, driver):
        """
        instantiate driver
        """
        self.driver = driver
        self.url = "https://docs.google.com/forms/d/e/1FAIpQLSfSGh4qzssK1gnZ6JEUe1D4E3lmGCelVD0VZgdHs_y7K_U7rA/viewform"


class UtilityPage(BasePage):

    def visit(self):
        self.driver.get(self.url)

    def click_next_button(self):
        """
        Click next button to move to next page
        """
        buttons = WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.quantumWizButtonPaperbuttonLabel.exportLabel'))
        )
        buttons[-1].click()
        time.sleep(2)

    def questions_headings(self):
        """
        Question Headings are question title on each page
        """
        all_headings = WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.freebirdFormviewerViewItemsItemItemTitle.freebirdCustomFont'))
        )
        # Get all questions only
        return all_headings

    def error_with_empty_and_wrong_fields(self, ind):
        """
        Note down the empty field error
        :param ind: ind is the index of each question in a list
        :return: error occurs with empty field
        """
        return self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            ind].find_element_by_css_selector('.freebirdFormviewerViewItemsItemErrorMessage').text

    def enter_some_wrong_values_in_fields(self, ind):
        """
        Enter some wrong value to get the error.
        :param ind: ind is the index of each question in a list
        """
        value = self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
                ind].find_element_by_css_selector('.quantumWizTextinputPaperinputInputArea > input')
        value.send_keys(Keys.BACKSPACE)
        value.send_keys('@')

    def status_of_page(self):
        """
        :return: Note down the current page status which is just like (etc Page 1 of 9)
        """
        return WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.freebirdFormviewerViewNavigationPercentComplete'))
        ).text

    def grading_question_list(self, ind, count):
        """
        This is about all pages only which needs re assessment
        :param ind: This is the number from the list which has only re assessment pages
        :param count: This is index of each question in the page
        :return: Return each question title
        """
        text = self.driver.find_elements_by_css_selector(".freebirdFormviewerViewItemList")[
            ind].find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            count].find_element_by_css_selector('.freebirdFormviewerViewItemsItemItemTitle').text
        return text

    def correct_answers(self, ind, count):
        """
        Collect all correct answers
        :param ind: This is the number from the list which has only correct answers box
        :param count: In selected 'ind' select question one by one
        :return: return that text
        """
        return self.driver.find_elements_by_css_selector(".freebirdFormviewerViewItemList")[
            ind].find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            count].find_elements_by_css_selector('.freebirdFormviewerViewItemsItemGradingGradingBox .docssharedWizToggleLabeledPrimaryText > span')

    def edit_response(self):
        """
        Need to switch window first
        Click edit response link
        """
        self.driver.switch_to.window(self.driver.window_handles[0])
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located(
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
            time.sleep(2)

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
        # from nose.tools import set_trace;set_trace()
        self.driver.find_element_by_css_selector('.freebirdFormviewerViewItemList [aria-label="{hard_cord}"][aria-checked="false"]'.format
                                                 (hard_cord=values)).click()
        time.sleep(2)

    def view_submitted_form(self):
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.quantumWizButtonPaperbuttonLabel.exportLabel'))
        ).click()
        #self.driver.find_element_by_css_selector(".quantumWizButtonPaperbuttonLabel.exportLabel").click()
        time.sleep(2)
        window = self.driver.window_handles[-2]
        time.sleep(1)
        self.driver.switch_to.window(window)
