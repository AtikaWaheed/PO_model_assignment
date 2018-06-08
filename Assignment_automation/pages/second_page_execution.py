from utility_page import UtilityPage


class SecondPageExecution(UtilityPage):
    """
    Execute second page which is 'Multiple type Questions'
    """
    def locator_and_firebug(self, **kwargs):
        """
        Page #2 all questions
        * id is index which is fetched from question heading list
        * values are fetched from dictionary as an argument
        """
        self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            kwargs.get('id')].find_element_by_css_selector('[data-value="{key_word}"]'.
                                                           format(key_word=kwargs.get('select_option'))).click()
