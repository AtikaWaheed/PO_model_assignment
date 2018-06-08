from ..tests.test_utility_page import BaseTest
from ..pages import first_page_execution


first_page_dict = {
            'CNIC': {'correct_input': 'enter_correct_values', 'wrong_pattern_error': 'Must match pattern',
                     'empty_error': 'This is a required question',
                     'value_as_an_argument': '3333333333333'},
            'Phone_Number': {'correct_input': 'enter_correct_values', 'wrong_pattern_error': 'Must match pattern',
                             'func_to_call_for_wrong_character': 'error_with_wrong_value',
                             'empty_error': 'This is a required question',
                             'value_as_an_argument': '33333333333'},
            'Name': {'correct_input': 'enter_correct_values', 'empty_error': 'This is a required question',
                     'value_as_an_argument': 'Atika'},
            'Email': {'correct_input': 'enter_correct_values', 'wrong_pattern_error': 'Must be a valid email address',
                      'empty_error': 'This is a required question', 'value_as_an_argument': 'a@a.com'}
            }


class FirstPage(BaseTest):

    def setUp(self):
        super(FirstPage, self).setUp()
        self.first_page_execution = first_page_execution.FirstPageExecution(self.driver)

    def test_first_page_execution(self):
        """
        Verify ist page executed
        """
        status = self.utility_page.status_of_page()
        self.assertEqual(status, 'Page 1 of 9')
        all_headings = self.utility_page.questions_headings()
        for ind, title in enumerate(all_headings):
            """
            This loop iterate all questions on page
            """
            title = title.text.replace(' *', '')
            key = title.replace(' ', '_')
            key = key.replace('?', '')
            self.utility_page.click_next_button()
            empty_field_error = self.utility_page.error_with_empty_and_wrong_fields(ind)
            self.assertEqual(empty_field_error, first_page_dict.get(key).get('empty_error'))
            if key != 'Name':
                self.utility_page.enter_some_wrong_values_in_fields(ind)
                wrong_charac_error = self.utility_page.error_with_empty_and_wrong_fields(ind)
                self.assertEqual(wrong_charac_error, first_page_dict.get(key).get('wrong_pattern_error'))
            self.first_page_execution.enter_correct_values(id=ind,
                                                           enter_values=first_page_dict.get(key).get('value_as_an_argument'))