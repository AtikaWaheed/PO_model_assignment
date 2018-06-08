from ..tests.test_utility_page import BaseTest
from ..pages import sixth_page_execution

sixth_page_dict = {
    'On_a_scale_of_1_to_five_how_hard_this_assignment_is': {'empty_error': 'This is a required question'}
    }


class SixthPage(BaseTest):

    def setUp(self):
        super(SixthPage, self).setUp()
        self.sixth_page_execution = sixth_page_execution.SixthPageExecution(self.driver)

    def test_sixth_page_execution(self):
        """
        Verify sixth Page
        """
        status = self.utility_page.status_of_page()
        self.assertEqual(status, 'Page 6 of 9')
        sixth_page_scale_question = self.utility_page.questions_headings()
        sixth_page_scale_question = sixth_page_scale_question[0].text.replace(' *', '')
        key = sixth_page_scale_question.replace(' ', '_')
        key = key.replace('?', '')
        self.utility_page.click_next_button()
        empty_field_error = self.utility_page.error_with_empty_and_wrong_fields(int(0))
        self.assertEqual(empty_field_error, sixth_page_dict.get(key).get('empty_error'))
        self.sixth_page_execution.scale_ranking()
