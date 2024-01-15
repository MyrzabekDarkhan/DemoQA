from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_clickable(self, by_locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(by_locator)
        )
