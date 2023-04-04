from selenium.webdriver.common.by import By
import base_page
from base_page import BasePage as base


class Constants:
    login_register = By.CLASS_NAME, "notSigned"
    register = By.CSS_SELECTOR, "h1[class=bm-h1]"
    register_type = By.TAG_NAME
    register_value = 'span'
    register_title = By.CLASS_NAME, "lightbox-head" # By.CSS_SELECTOR, "h1[class=bm-h1]"


class HomePage(base):

    def __init__(self, driver):
        base.__init__(self, driver)
        self.driver = base_page.driver

    def click_on_login(self):
        base.wait_and_click_on_element(self, Constants.login_register)
        print(self.driver.current_url)

    def click_on_register(self):
        base.wait_and_click_on_below_element(self, Constants.register, Constants.register_type, Constants.register_value)

    def verify_title_Registration(self):
        base.wait_and_get_elem_text(self,Constants.register_title, "הרשמה")
