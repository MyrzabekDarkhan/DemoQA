from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ElementsPage(BasePage):
    ELEMENTS_CARD = (By.XPATH, '//h5[text()="Elements"]')
    CHECKBOX_MENU_ITEM = (By.XPATH, '//span[text()="Check Box"]')

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_elements_section(self):
        self.wait_for_element_to_be_clickable(self.ELEMENTS_CARD).click()

    def navigate_to_checkbox_section(self):
        self.wait_for_element_to_be_clickable(self.CHECKBOX_MENU_ITEM).click()
