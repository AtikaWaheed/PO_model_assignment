from utility_page import UtilityPage


class ThirdPageExecution(UtilityPage):
    """
    Execute third page which is 'Checkboxes'
    """
    def choose_answers(self, id):
        """
        Click checkboxes
        :param: * id is index which is fetched from question heading list
        """
        answers = self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            id].find_elements_by_css_selector('.docssharedWizToggleLabeledLabelText')
        # In 'answers' there is a list of answers
        answers[2].click()
        answers[3].click()
