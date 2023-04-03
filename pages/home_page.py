from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import RelativeBy

import base_page
from base_page import BasePage as base


class Constants:
    login_register = By.CLASS_NAME, "notSigned"
    register = By.CSS_SELECTOR, "h1[class=bm-h1]"
    register_type = By.TAG_NAME
    register_value = 'span'

    # login_email = By.ID, "ember1974"
    # login_password = By.ID, "ember1981"
    # login_button =
    #
    # register_first_name = By.ID, "ember1932"
    # register_email =
    # register_password =
    # register_password_conf =


class HomePage(base):

    def __init__(self, driver):
        base.__init__(self, driver)
        self.driver = base_page.driver

    def click_on_login(self):
        base.wait_and_click_on_element(self, Constants.login_register)
        print(self.driver.current_url)

    def click_on_register(self):
        base.wait_and_click_on_below_element(self, Constants.register, Constants.register_type, Constants.register_value)

    def enter_first_name(self):
        base.wait_and_enter_text(self, Constants.register_first_name, 'firstName')

    def login_success(self):
        base.wait_and_enter_text(self, Constants.login_email, "test@email.com")
        base.wait_and_enter_text(self, Constants.login_password, "Password")
