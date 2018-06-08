from ..tests.test_utility_page import BaseTest
from ..pages import second_page_execution

second_page_dict = {
        'Select_the_name_which_is_NOT_a_type_of_the_locater': {'empty_error': 'This is a required question',
                                                               'value_as_an_option': 'ID'},
        'Use_of_Firebug_in_Selenium': {'empty_error': 'This is a required question',
                                       'value_as_an_option': 'Programming'}
        }


class SecondPage(BaseTest):

    def setUp(self):
        super(SecondPage, self).setUp()
        self.second_page_execution = second_page_execution.SecondPageExecution(self.driver)

    def test_second_page_execution(self):
        """
        Verify second page
        """
        status = self.utility_page.status_of_page()
        self.assertEqual(status, 'Page 2 of 9')
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
            self.assertEqual(empty_field_error, second_page_dict.get(key).get('empty_error'))
            self.second_page_execution.locator_and_firebug(id=ind,
                                                           select_option=second_page_dict.get(key).get('value_as_an_option'))
