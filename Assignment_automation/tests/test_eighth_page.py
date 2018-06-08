from ..tests.test_utility_page import BaseTest
from ..pages import seventh_and_eighth_pages_execution


eighth_page_dict = {
        'Select_your_proficiency_in_following': {'empty_error': 'This question requires at least one response per row'}
        }


class EighthPage(BaseTest):

    def setUp(self):
        super(EighthPage, self).setUp()
        self.eighth_pages_execution = seventh_and_eighth_pages_execution.SeventhAndEighthPageExecution(self.driver)

    def test_eighth_page_execution(self):
        """
        Verify eighth page
        """
        status = self.utility_page.status_of_page()
        self.assertEqual(status, 'Page 8 of 9')
        eighth_page_question = self.utility_page.questions_headings()
        eighth_page_question = eighth_page_question[0].text.replace(' *', '')
        key = eighth_page_question.replace(' ', '_')
        key = key.replace('?', '')
        self.utility_page.click_next_button()
        empty_field_error = self.utility_page.error_with_empty_and_wrong_fields(
            eighth_page_dict.get(key).get('ind_number'))
        self.assertEqual(empty_field_error, eighth_page_dict.get(key).get('empty_error'))
        self.eighth_pages_execution.choice_grid(eighth_page_dict.get(key).get('ind_number'))
