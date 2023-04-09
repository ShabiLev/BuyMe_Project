from selenium.webdriver.common.by import By
import base_page
from base_page import BasePage as base


class Constants:
    login_register = By.CLASS_NAME, "notSigned"
    register = By.CSS_SELECTOR, "h1[class=bm-h1]"
    register_type = By.TAG_NAME
    register_value = 'span'
    register_title = By.CLASS_NAME, "lightbox-head"
    drop_price = By.XPATH, "//div[@class='dropdown'][@role='listbox'][@aria-label='סכום']"
    drop_erea = By.XPATH, '//input[@placeholder="הכנס סכום"]' # '.selected-text[title="amount"]'
    drop_category = By.XPATH, "//option[text()='קטגוריה']"
    button_search = By.XPATH, "//option[text()='חיפוש']"

class HomePage(base):

    def __init__(self, driver):
        base.__init__(self, driver)
        self.driver = base_page.driver

    def click_on_login(self):
        base.wait_and_click_on_element(self, Constants.login_register)

    def click_on_register(self):
        base.wait_and_click_on_below_element(self, Constants.register, Constants.register_type, Constants.register_value)

    def verify_title_Registration(self):
        base.wait_and_verify_text(self, Constants.register_title, "הרשמה")

    def search_for_present(self):
        # base.wait_and_select_from_dropdown_by_text(self, Constants.drop_price, "סכום")
        base.wait_and_click_on_element(self, Constants.drop_price)

    def scroll_to_bottom_screen(self):
        # Scroll to the bottom of the page
        base.scroll_webpage(self, "down")
