from ..tests.test_utility_page import BaseTest
from ..pages import seventh_and_eighth_pages_execution


seventh_page_dict = {
        'How_satisfied_are_you_with_the_following': {'empty_error': 'This question requires one response per row'}
        }


class SeventhPage(BaseTest):

    def setUp(self):
        super(SeventhPage, self).setUp()
        self.seventh_page_execution = seventh_and_eighth_pages_execution.SeventhAndEighthPageExecution(self.driver)

    def test_seventh_page_execution(self):
        """
        Verify seventh page
        """
        status = self.utility_page.status_of_page()
        self.assertEqual(status, 'Page 7 of 9')
        seventh_page_question = self.utility_page.questions_headings()
        seventh_page_question = seventh_page_question[0].text.replace(' *', '')
        key = seventh_page_question.replace(' ', '_')
        key = key.replace('?', '')
        self.utility_page.click_next_button()
        empty_field_error = self.utility_page.error_with_empty_and_wrong_fields(int(0))
        self.assertEqual(empty_field_error, seventh_page_dict.get(key).get('empty_error'))
        self.seventh_page_execution.choice_grid(seventh_page_dict.get(key).get('ind_number'))
