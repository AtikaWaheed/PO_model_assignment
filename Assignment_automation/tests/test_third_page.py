from ..tests.test_utility_page import BaseTest
from ..pages import third_page_execution

third_page_dict = {
        'Select_the_correct_answers': {'empty_error': 'This is a required question'},
        'Select_the_two_numbers_that_are_not_prime.': {'empty_error': 'This is a required question'}
        }


class ThirdPage(BaseTest):

    def setUp(self):
        super(ThirdPage, self).setUp()
        self.third_page_execution = third_page_execution.ThirdPageExecution(self.driver)

    def test_third_page_execution(self):
        """
        Verify third page
        """
        status = self.utility_page.status_of_page()
        self.assertEqual(status, 'Page 3 of 9')
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
            self.assertEqual(empty_field_error, third_page_dict.get(key).get('empty_error'))
            self.third_page_execution.choose_answers(ind)
