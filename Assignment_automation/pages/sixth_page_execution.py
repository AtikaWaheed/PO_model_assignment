from utility_page import UtilityPage


class SixthPageExecution(UtilityPage):
    """
    Execute sixth page which is about 'Scale'
    """
    def scale_ranking(self):
        """
        Rank the assignment
        :param kwargs:* id is index which is fetched from question heading list
        """
        self.driver.find_elements_by_css_selector('.quantumWizTogglePaperradioOffRadio.exportOuterCircle')[2].click()
