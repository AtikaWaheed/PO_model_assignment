from utility_page import UtilityPage


class SeventhAndEighthPageExecution(UtilityPage):
    """
    Execute Seventh and Eighth Page together as its about 'Multiple Choice grids'
    """
    def choice_grid(self, id):
        """
        Fill the grid choices
        :param kwargs:* id is index which is fetched from question heading list
        """
        rows = self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            id].find_elements_by_css_selector('.freebirdFormviewerViewItemsGridRowGroup')
        # row contains all choices list
        rows[0].find_elements_by_css_selector('label')[2].click()
        rows[1].find_elements_by_css_selector('label')[2].click()
        rows[2].find_elements_by_css_selector('label')[2].click()
