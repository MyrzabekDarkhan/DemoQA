from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CheckboxPage(BasePage):
    HOME_TOGGLE = (By.XPATH, '//button[@title="Toggle"]//*[name()="svg"]')
    DOWNLOADS_TOGGLE = (By.XPATH, '//span[text()="Downloads"]/parent::*/preceding-sibling::button')
    WORD_FILE_CHECKBOX = (By.XPATH, '//span[text()="Word File.doc"]')
    RESULT = (By.ID, "result")

    def __init__(self, driver):
        super().__init__(driver)

    def expand_home_directory(self):
        self.wait_for_element_to_be_clickable(self.HOME_TOGGLE).click()

    def expand_downloads_directory(self):
        self.wait_for_element_to_be_clickable(self.DOWNLOADS_TOGGLE).click()

    def select_word_file(self):
        self.wait_for_element_to_be_clickable(self.WORD_FILE_CHECKBOX).click()

    def get_result_text(self):
        return self.wait_for_element_to_be_clickable(self.RESULT).text
