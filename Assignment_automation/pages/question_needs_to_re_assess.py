from utility_page import UtilityPage
#____________________________

class QuestionNeedsReAssessment(UtilityPage):

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

