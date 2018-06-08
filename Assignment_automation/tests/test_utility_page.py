from ..tests.test_utility1_page import BaseTest
from ..pages import first_page_execution
from ..pages import second_page_execution
from ..pages import third_page_execution
from ..pages import fourth_page_execution
from ..pages import fifth_page_execution
from ..pages import sixth_page_execution
from ..pages import seventh_and_eighth_pages_execution
from ..pages import ninth_page_execution
from datetime import datetime
from datetime import date
from ..tests.test_first_page import first_page_dict
from ..tests.test_second_page import second_page_dict
from ..tests.test_third_page import third_page_dict
from ..tests.test_fourth_page import fourth_page_dict
from ..tests.test_fifth_page import fifth_page_dict
from ..tests.test_sixth_page import sixth_page_dict
from ..tests.test_seventh_page import seventh_page_dict
from ..tests.test_eighth_page import eighth_page_dict
from ..tests.test_ninth_page import ninth_page_dict


class TestMainClass(BaseTest):

    def setUp(self):
        super(TestMainClass, self).setUp()
        self.first_page_execution = first_page_execution.FirstPageExecution(self.driver)
        self.second_page_execution = second_page_execution.SecondPageExecution(self.driver)
        self.third_page_execution = third_page_execution.ThirdPageExecution(self.driver)
        self.fourth_page_execution = fourth_page_execution.FourthPageExecution(self.driver)
        self.fifth_page_execution = fifth_page_execution.FifthPageExecution(self.driver)
        self.sixth_page_execution = sixth_page_execution.SixthPageExecution(self.driver)
        self.seventh_page_execution = seventh_and_eighth_pages_execution.SeventhAndEighthPageExecution(self.driver)
        self.eighth_pages_execution = seventh_and_eighth_pages_execution.SeventhAndEighthPageExecution(self.driver)
        self.ninth_page_execution = ninth_page_execution.NinthPageExecution(self.driver)

    def test_first_page_execution(self):
        """
        Verify ist page executed
        """
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

    def test_second_page_execution(self):
        """
        Verify second page
        """
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

    def test_third_page_execution(self):
        """
        Verify third page
        """
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

    def test_fourth_page_execution(self):
        """
        Verify 4th page
        """
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

    def test_fifth_page_execution(self):
        """
        Verify fifth page
        """
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
            self.assertEqual(empty_field_error, fifth_page_dict.get(key).get('empty_error'))
            self.fifth_page_execution.upload_files(ind)

    def test_sixth_page_execution(self):
        """
        Verify sixth Page
        """
        sixth_page_scale_question = self.utility_page.questions_headings()
        sixth_page_scale_question = sixth_page_scale_question[0].text.replace(' *', '')
        key = sixth_page_scale_question.replace(' ', '_')
        key = key.replace('?', '')
        self.utility_page.click_next_button()
        empty_field_error = self.utility_page.error_with_empty_and_wrong_fields(int(0))
        self.assertEqual(empty_field_error, sixth_page_dict.get(key).get('empty_error'))
        self.sixth_page_execution.scale_ranking()

    def test_seventh_page_execution(self):
        """
        Verify seventh page
        """
        seventh_page_question = self.utility_page.questions_headings()
        seventh_page_question = seventh_page_question[0].text.replace(' *', '')
        key = seventh_page_question.replace(' ', '_')
        key = key.replace('?', '')
        self.utility_page.click_next_button()
        empty_field_error = self.utility_page.error_with_empty_and_wrong_fields(int(0))
        self.assertEqual(empty_field_error, seventh_page_dict.get(key).get('empty_error'))
        self.seventh_page_execution.choice_grid(int(0))

    def test_eighth_page_execution(self):
        """
        Verify eighth page
        """
        eighth_page_question = self.utility_page.questions_headings()
        eighth_page_question = eighth_page_question[0].text.replace(' *', '')
        key = eighth_page_question.replace(' ', '_')
        key = key.replace('?', '')
        self.utility_page.click_next_button()
        empty_field_error = self.utility_page.error_with_empty_and_wrong_fields(int(0))
        self.assertEqual(empty_field_error, eighth_page_dict.get(key).get('empty_error'))
        self.eighth_pages_execution.choice_grid(int(0))

    def test_ninth_page_execution(self):
        """
        Vrify ninth page
        """
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
            print key
            self.utility_page.click_next_button()
            empty_field_error = self.utility_page.error_with_empty_and_wrong_fields(ind)
            self.assertEqual(empty_field_error, ninth_page_dict.get(key).get('empty_error'))
            self.utility_page.enter_some_wrong_values_in_fields(ind)
            self.utility_page.click_next_button()
            wrong_charac_error = self.utility_page.error_with_empty_and_wrong_fields(ind)
            self.assertEqual(wrong_charac_error, ninth_page_dict.get(key).get('wrong_pattern_error'))
            # correct_input = getattr(self.ninth_page_execution, ninth_page_dict.get(key).get('correct_input'))
            if key == 'Enter_Current_date':
                self.ninth_page_execution.enter_date(fist_value=current_month, second_value=current_day)
            else:
                self.ninth_page_execution.enter_time(fist_value=current_time_hour, second_value=current_time_minutes)
