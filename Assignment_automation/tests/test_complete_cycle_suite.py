from ..tests.test_utility_page import TestMainClass
from ..pages import note_down_scores_get
from ..pages import all_written_inputs_in_csv
from ..pages import read_and_enter_correct_answers
from ..pages import resubmitting_test_scenario


class TestCompleteCycleSuite(TestMainClass):

    def setUp(self):
        super(TestCompleteCycleSuite, self).setUp()
        self.note_down_scores_get = note_down_scores_get.NoteDownScoresGet(self.driver)
        self.all_written_inputs_in_csv = all_written_inputs_in_csv.CorrectWrittenInputsInCsv(self.driver)
        self.read_and_enter_correct_answers = read_and_enter_correct_answers.ReadAndWriteCorrectInput(self.driver)
        self.resubmitting_test_scenario = resubmitting_test_scenario.ResubmitForm(self.driver)

    def test_complete_cycle_suite(self):
        """
        verify a complete cycle runs
        """
        # #from nose.tools import set_trace;
        # set_trace()
        self.test_login_scenarios()
        ist_pg_status = self.utility_page.status_of_page()
        self.assertEqual(ist_pg_status, 'Page 1 of 9')
        self.test_first_page_execution()
        self.utility_page.click_next_button()
        sec_pg_status = self.utility_page.status_of_page()
        self.assertEqual(sec_pg_status, 'Page 2 of 9')
        self.test_second_page_execution()
        self.utility_page.click_next_button()
        third_pg_status = self.utility_page.status_of_page()
        self.assertEqual(third_pg_status, 'Page 3 of 9')
        self.test_third_page_execution()
        self.utility_page.click_next_button()
        fourth_pg_status = self.utility_page.status_of_page()
        self.assertEqual(fourth_pg_status, 'Page 4 of 9')
        self.test_fourth_page_execution()
        self.utility_page.click_next_button()
        fifth_pg_status = self.utility_page.status_of_page()
        self.assertEqual(fifth_pg_status, 'Page 5 of 9')
        self.test_fifth_page_execution()
        self.utility_page.click_next_button()
        sixth_pg_status = self.utility_page.status_of_page()
        self.assertEqual(sixth_pg_status, 'Page 6 of 9')
        self.test_sixth_page_execution()
        self.utility_page.click_next_button()
        seventh_pg_status = self.utility_page.status_of_page()
        self.assertEqual(seventh_pg_status, 'Page 7 of 9')
        self.test_seventh_page_execution()
        self.utility_page.click_next_button()
        eighth_pg_status = self.utility_page.status_of_page()
        self.assertEqual(eighth_pg_status, 'Page 8 of 9')
        self.test_eighth_page_execution()
        self.utility_page.click_next_button()
        ninth_pg_status = self.utility_page.status_of_page()
        self.assertEqual(ninth_pg_status, 'Page 9 of 9')
        self.test_ninth_page_execution()
        self.utility_page.click_next_button()
        confirm_message = self.note_down_scores_get.confirmation_message()
        self.assertEqual(confirm_message, 'Your response has been recorded.')
        self.note_down_scores_get.view_score()
        """
        Note down how many scores you get
        """
        total_score_get = self.note_down_scores_get.total_score()
        total_score_get.split()
        print "Got " + total_score_get[0] + total_score_get[1] + " points out of 40"
        self.all_written_inputs_in_csv.write_all_correct_inputs_in_csv()
        self.utility_page.edit_response()
        self.utility_page.click_next_button()
        # from nose.tools import set_trace;set_trace()
        self.read_and_enter_correct_answers.read_and_enter_correct_answers()
        self.resubmitting_test_scenario.resubmit_form_with_correct_inputs()
        if self.note_down_scores_get.total_score() == "40/40":
            from nose.tools import set_trace;
            set_trace()
            print "Finally you did it"










