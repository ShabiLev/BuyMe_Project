import time

from selenium.webdriver.common.by import By
import base_page
from base_page import BasePage as base


class Constants:
    register_first_name = By.XPATH, "//input[@placeholder='שם פרטי']"
    register_email = By.XPATH, "//input[@placeholder='מייל']"
    register_password = By.ID, "valPass"
    register_password_conf = By.XPATH, "//input[@placeholder='אימות סיסמה']"
    agree_radio = By.XPATH, "//span[@class='circle']"
    submit = By.XPATH, "//button[@type='submit']"


class Register(base):

    def __init__(self, driver):
        base.__init__(self, driver)
        self.driver = base_page.driver

    def register_fail(self):
        base.wait_and_enter_text(self, Constants.register_first_name, "register_fail")
        base.wait_and_enter_text(self, Constants.register_email, "test")
        base.wait_and_enter_text(self, Constants.register_password, "Password")
        base.wait_and_enter_text(self, Constants.register_password_conf, "Password2")
        base.wait_and_click_on_element(self, Constants.agree_radio)
        base.wait_and_click_on_element(self,Constants.submit)

    def register_success(self):
        base.wait_and_enter_text(self, Constants.register_first_name, "register_success")
        base.wait_and_enter_text(self, Constants.register_email, "test@email.com")
        base.wait_and_enter_text(self, Constants.register_password, "Password")
        base.wait_and_enter_text(self, Constants.register_password_conf, "Password2")
        base.wait_and_click_on_element(self, Constants.agree_radio)
