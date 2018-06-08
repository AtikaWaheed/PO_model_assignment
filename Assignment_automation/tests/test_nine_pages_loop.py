import csv
from test_utility_page import BaseTest
from ..pages.utility_page import UtilityPage
from ..pages.all_written_inputs_in_csv import CorrectWrittenInputsInCsv
from ..pages.read_and_enter_correct_answers import ReadAndWriteCorrectInput
from ..pages.resubmitting_test_scenario import ResubmitForm


dict = {
        'CNIC': {'correct_input': 'enter_correct_values', 'wrong_pattern_error': 'Must match pattern',
                 'empty_error': 'This is a required question', 'func_to_call_for_wrong_character': 'error_with_wrong_value',
                 'func_to_call_for_empty_field': 'error_with_empty_field',
                 'value_as_an_argument': '3333333333333'},
        'Phone_Number': {'correct_input': 'enter_correct_values', 'wrong_pattern_error': 'Must match pattern',
                         'func_to_call_for_wrong_character': 'error_with_wrong_value',
                         'empty_error': 'This is a required question',
                         'func_to_call_for_empty_field': 'error_with_empty_field', 'value_as_an_argument': '33333333333'},
        'Name': {'correct_input': 'enter_correct_values', 'empty_error': 'This is a required question',
                 'func_to_call_for_empty_field': 'error_with_empty_field',
                 'value_as_an_argument': 'Atika'},
        'Email': {'correct_input': 'enter_correct_values', 'wrong_pattern_error': 'Must be a valid email address',
                  'empty_error': 'This is a required question', 'func_to_call_for_wrong_character': 'error_with_wrong_value',
                  'func_to_call_for_empty_field': 'error_with_empty_field', 'value_as_an_argument': 'a@a.com'},
        'Select_the_name_which_is_NOT_a_type_of_the_locater': {'func_to_call_for_empty_field': 'error_with_empty_field',
                                                               'empty_error': 'This is a required question',
                                                               'correct_input': 'locator_and_firebug',
                                                               'value_as_an_argument': 'ID'},
        'Use_of_Firebug_in_Selenium': {'func_to_call_for_empty_field': 'error_with_empty_field',
                                       'empty_error': 'This is a required question',
                                       'correct_input': 'locator_and_firebug',
                                       'value_as_an_argument': 'Programming'},
        'Select_the_correct_answers': {'func_to_call_for_empty_field': 'error_with_empty_field',
                                       'empty_error': 'This is a required question',
                                       'correct_input': 'choose_answers'},
        'Select_the_two_numbers_that_are_not_prime.': {'func_to_call_for_empty_field': 'error_with_empty_field',
                                                       'empty_error': 'This is a required question',
                                                       'correct_input': 'choose_answers'},
        'Capital_of_Pakistan': {'func_to_call_for_empty_field': 'error_with_empty_field',
                                'empty_error': 'This is a required question',
                                'correct_input': 'capital_answers'},
        'Capital_of_Punjab': {'func_to_call_for_empty_field': 'error_with_empty_field',
                              'empty_error': 'This is a required question',
                              'correct_input': 'capital_answers'},
        'Upload_pdf_file': {'func_to_call_for_empty_field': 'error_with_empty_field',
                            'empty_error': 'This is a required question',
                            'correct_input': 'upload_files'},
        'Upload_Image_File': {'func_to_call_for_empty_field': 'error_with_empty_field',
                              'empty_error': 'This is a required question',
                              'correct_input': 'upload_files'},
        'On_a_scale_of_1_to_five_how_hard_this_assignment_is': {'func_to_call_for_empty_field': 'error_with_empty_field',
                                                                'empty_error': 'This is a required question',
                                                                'correct_input': 'scale_ranking'},
        'How_satisfied_are_you_with_the_following': {'func_to_call_for_empty_field': 'error_with_empty_field',
                                                     'empty_error': 'This question requires one response per row',
                                                     'correct_input': 'choice_grid'},
        'Select_your_proficiency_in_following': {'func_to_call_for_empty_field': 'error_with_empty_field',
                                                 'empty_error': 'This question requires at least one response per row',
                                                 'correct_input': 'choice_grid'},
        'Enter_Current_time': {'func_to_call_for_empty_field': 'error_with_empty_field',
                               'empty_error': 'This is a required question',
                               'correct_input': 'enter_time', 'value_as_an_argument': '05', 'value_as_an_argument1': '45',
                               'func_to_call_for_wrong_character': 'error_with_wrong_value',
                               'wrong_pattern_error': 'Invalid time'},
        'Enter_Current_date': {'func_to_call_for_empty_field': 'error_with_empty_field',
                               'empty_error': 'This is a required question',
                               'correct_input': 'enter_date', 'value_as_an_argument': '03', 'value_as_an_argument1': '25',
                               'func_to_call_for_wrong_character': 'error_with_wrong_value',
                               'wrong_pattern_error': 'Invalid date'}
        }


class NinePagesLoop(BaseTest):
    """
    This test class contains all test cases related all nine pages
    """
    def setUp(self):
        super(NinePagesLoop, self).setUp()
        self.utility_page = UtilityPage(self.driver)
        self.all_written_inputs_in_csv = CorrectWrittenInputsInCsv(self.driver)
        self.read_and_enter_correct_answers = ReadAndWriteCorrectInput(self.driver)
        self.resubmitting_test_scenario = ResubmitForm(self.driver)

    def test01_execution_for_pages(self):
        for count in range(9):
            """
            This loop iterate all nine pages
            """
            all_headings = self.utility_page.questions_headings()
            # all_headings contains a list of all questions per page
            count = count + 1
            number = "Page " + str(count) + " of 9"
            status = self.utility_page.status_of_page()
            self.assertEqual(status, number)
            for ind, heading in enumerate(all_headings):
                """
                This loop iterate single page
                * 'ind' describes index, in the all questions list 
                * heading is question title
                """
                heading = heading.text.replace(' *', '')
                key = heading.replace(' ', '_')
                key = key.replace('?', '')
                self.utility_page.click_next_button()
                empty_field_error = getattr(self.utility_page, dict.get(key).get('func_to_call_for_empty_field'))(ind)
                self.assertEqual(empty_field_error, dict.get(key).get('empty_error'))
                if dict.get(key). has_key('func_to_call_for_wrong_character'):
                    getattr(self.utility_page, dict.get(key).get('func_to_call_for_wrong_character'))(ind)
                correct_input_for_each_question = getattr(self.google_page, dict.get(key).get('correct_input'))
                correct_input_for_each_question(id=ind, values=dict.get(key).get('value_as_an_argument'), value1=dict.get(key).get('value_as_an_argument1'))
            self.google_page.click_next_button()
        confirm_message = self.google_page.confirmation_message()
        self.assertEqual(confirm_message, 'Your response has been recorded.')
        """
        View submitted form's score
        """
        self.google_page.view_score()
        """
        Note down how many scores get
        """
        total_score_get = self.google_page.total_score()
        total_score_get.split()
        print "Got " + total_score_get[0] + total_score_get[1] + " points out of 40"
        self.all_written_inputs_in_csv()
        #self.write_all_correct_inputs_in_csv()
        self.read_and_enter_correct_answers()
        #self.read_and_put_correct_answers()
        self.resubmitting_test_scenario()


"""def write_all_correct_inputs_in_csv(self):
        my_file = open("output.csv", "w")
        for number in range(1, 4):
            for index in range(2):
                title = self.google_page.grading_question_list(number, index)
                answer_list = self.google_page.correct_answers(number, index)
                if len(answer_list):
                    my_file.write('Q: ' + str(title) + "\n")
                    for item in answer_list:
                        my_file.write(str(item.text) + "\n")
        self.google_page.edit_response()
        self.google_page.click_next_button()

    def read_and_put_correct_answers(self):
        my_file = 'output.csv'
        with open(my_file, 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if row[0].startswith('Q:'):
                    question = row[0].replace('Q: ', '')
                    question_found = False
                    for number in range(2):
                        headings = self.google_page.questions_headings()
                        for ind, title in enumerate(headings):
                            if title.text == question:
                                next_answer = next(csv_reader)
                                self.google_page.first_uncheck_all_options(ind)
                                self.google_page.correct_input_from_csv(ind, next_answer[0])
                                question_found = True
                                break
                        if question_found:
                            break
                        else:
                            self.google_page.click_next_button()
                else:
                    self.google_page.multiple_inputs_from_csv(row[0])

    def resubmit_form_with_correct_inputs(self):
        [self.google_page.click_next_button() for _ in range(7)]
        self.google_page.view_submitted_form()
        if self.google_page.total_score() == "40/40":
            print "Finally you did it"""



