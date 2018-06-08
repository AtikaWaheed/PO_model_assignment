from ..tests.test_utility_page import BaseTest
from ..pages import fourth_page_execution

fourth_page_dict = {
        'Capital_of_Pakistan': {'empty_error': 'This is a required question'},
        'Capital_of_Punjab': {'empty_error': 'This is a required question'}
        }


class FourthPage(BaseTest):

    def setUp(self):
        super(FourthPage, self).setUp()
        self.fourth_page_execution = fourth_page_execution.FourthPageExecution(self.driver)

    def test_fourth_page_execution(self):
        """
        Verify 4th page
        """
        status = self.utility_page.status_of_page()
        self.assertEqual(status, 'Page 4 of 9')
        all_headings = self.utility_page.questions_headings()
        # all_headings is a list having all questions
        for ind, title in enumerate(all_headings):
            """
            This loop iterate all questions on page
            """
            title = title.text.replace(' *', '')
            key = title.replace(' ', '_')
            key = key.replace('?', '')
            self.utility_page.click_next_button()
            empty_field_error = self.utility_page.error_with_empty_and_wrong_fields(ind)
            self.assertEqual(empty_field_error, fourth_page_dict.get(key).get('empty_error'))
            self.fourth_page_execution.capital_answers(ind)
