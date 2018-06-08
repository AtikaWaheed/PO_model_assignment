from ..tests.test_utility_page import BaseTest
from ..pages import fifth_page_execution

fifth_page_dict = {
        'Upload_pdf_file': {'empty_error': 'This is a required question'},
        'Upload_Image_File': {'empty_error': 'This is a required question'}
}


class FifthPage(BaseTest):

    def setUp(self):
        super(FifthPage, self).setUp()
        self.fifth_page_execution = fifth_page_execution.FifthPageExecution(self.driver)

    def test_fifth_page_execution(self):
        """
        Verify fifth page
        """
        status = self.utility_page.status_of_page()
        self.assertEqual(status, 'Page 5 of 9')
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
