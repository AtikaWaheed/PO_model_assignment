from ..tests.test_utility_page import BaseTest
from ..pages import ninth_page_execution
from datetime import datetime
from datetime import date


ninth_page_dict = {
        'Enter_Current_time': {'empty_error': 'This is a required question',
                               'wrong_pattern_error': 'Invalid time'},
        'Enter_Current_date': {'empty_error': 'This is a required question',
                               'wrong_pattern_error': 'Invalid date'}
        }


class NinthPage(BaseTest):

    def setUp(self):
        super(NinthPage, self).setUp()
        self.ninth_page_execution = ninth_page_execution.NinthPageExecution(self.driver)

    def test_ninth_page_execution(self):
        """
        Vrify ninth page
        """
        status = self.utility_page.status_of_page()
        self.assertEqual(status, 'Page 9 of 9')
        # all_headings is a list having all questions
        all_headings = self.utility_page.questions_headings()
        # Using date control
        now = datetime.now()
        today = date.today()
        current_month = today.month
        current_day = today.day
        current_time_minutes = now.strftime('%M')
        current_time_hour = now.strftime('%I')
        for ind, title in enumerate(all_headings):
            """
            This loop iterate all questions on page
            """
            title = title.text.replace(' *', '')
            key = title.replace(' ', '_')
            key = key.replace('?', '')
            self.utility_page.click_next_button()
            empty_field_error = self.utility_page.error_with_empty_and_wrong_fields(ind)
            self.assertEqual(empty_field_error, ninth_page_dict.get(key).get('empty_error'))
            self.utility_page.enter_some_wrong_values_in_fields(ind)
            wrong_charac_error = self.utility_page.error_with_empty_and_wrong_fields(ind)
            self.assertEqual(wrong_charac_error, ninth_page_dict.get(key).get('wrong_pattern_error'))
            # getattr use for calling a funct from dictionary using keys
            # correct_input = getattr(self.ninth_page_execution, ninth_page_dict.get(key).get('correct_input'))
            if key == 'Enter Current date':
                self.ninth_page_execution.enter_date(fist_value=current_month, second_value=current_day)
            else:
                self.ninth_page_execution.enter_time(fist_value=current_time_hour, second_value=current_time_minutes)
