from selenium import webdriver
from pages.ElementsPage import ElementsPage
from pages.CheckboxPage import CheckboxPage


def run_test(browser_name):
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported.")

    driver.maximize_window()
    driver.get("https://demoqa.com/")

    try:
        elements_page = ElementsPage(driver)
        elements_page.navigate_to_elements_section()
        elements_page.navigate_to_checkbox_section()
        checkbox_page = CheckboxPage(driver)
        checkbox_page.expand_home_directory()
        checkbox_page.expand_downloads_directory()
        checkbox_page.select_word_file()
        result_text = checkbox_page.get_result_text()
        print(result_text)
        assert "You have selected :" in result_text
        assert "wordFile" in result_text

        print(f"Test passed on {browser_name}: The correct message is displayed.")

    except Exception as e:
        print(f"An exception occurred in {browser_name}: {e}")
    finally:
        driver.quit()


run_test("chrome")
run_test("firefox")
