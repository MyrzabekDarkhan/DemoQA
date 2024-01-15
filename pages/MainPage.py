from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.ElementsPage import ElementsPage


class MainPage(BasePage):
    ELEMENTS_BUTTON = (By.XPATH, '//span[text()="Elements"]')

    def go_to_elements_page(self):
        elements_button = self.driver.find_element(*self.ELEMENTS_BUTTON)
        elements_button.click()
        return ElementsPage(self.driver)
