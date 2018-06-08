from ..pages.utility_page import UtilityPage


class ResubmitForm(UtilityPage):

    def resubmit_form_with_correct_inputs(self):
        """
        Click next until you reach last page to resubmit form
        """
        [self.click_next_button() for _ in range(7)]
        self.view_submitted_form()

