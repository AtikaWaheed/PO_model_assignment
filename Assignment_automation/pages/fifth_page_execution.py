import time
from utility_page import UtilityPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FifthPageExecution(UtilityPage):
    """
    Execute Fifth page which is about 'File Uploading'
    """
    def upload_files(self, id):
        """
        Upload pdf and image files
        :param kwargs:* id is index which is fetched from question heading list
        :return:
        """
        self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            id].find_element_by_css_selector('.quantumWizButtonPaperbuttonLabel').click()
        time.sleep(5)
        if id == 0:
            frame = self.driver.find_element_by_css_selector('iframe.picker-frame')
            self.driver.switch_to.frame(frame)
        else:
            frame = self.driver.find_element_by_css_selector('.picker.modal-dialog.picker-dialog:nth-last-child(2) .picker-frame')
            time.sleep(5)
            self.driver.switch_to.frame(frame)
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#\:6 > div'))
        ).click()
        #time.sleep(4)
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Files and folders list view."] > div'))
        ).click()
        #time.sleep(4)
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#picker\:ap\:2'))
        ).click()
        # time.sleep(4)
        self.driver.switch_to.default_content()
