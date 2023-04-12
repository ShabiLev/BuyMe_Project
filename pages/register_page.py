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
    email_required_error = By.ID, "parsley-id-27" #"//input[@data-parsley-id='23']" #By.CLASS_NAME, "parsley-required"
    password_mismach_error = By.CLASS_NAME, "parsley-equalto"


class Register(base):

    def __init__(self, driver):
        base.__init__(self, driver)
        self.driver = base_page.driver

    def register_fail_email(self):
        base.wait_and_enter_text(self, Constants.register_first_name, "register_fail_email")
        base.wait_and_enter_text(self, Constants.register_email, "")
        base.wait_and_click_on_element(self, Constants.submit)
        base.wait_and_verify_text(self, Constants.register_email, "ערך זה דרוש")

    def register_fail_password(self):
        base.wait_and_enter_text(self, Constants.register_first_name, "register_fail_password")
        base.wait_and_enter_text(self, Constants.register_password, "")
        base.wait_and_enter_text(self, Constants.register_password_conf, "")
        base.wait_and_click_on_element(self, Constants.submit)
        base.wait_and_verify_text(self, Constants.register_password, "ערך זה דרוש.")
        base.wait_and_verify_text(self, Constants.register_password_conf, "ערך זה דרוש.")
        base.save_screenshot(self)
        base.wait_and_enter_text(self, Constants.register_password, "123456")
        base.wait_and_enter_text(self, Constants.register_password_conf, "12345")
        base.wait_and_click_on_element(self, Constants.submit)
        base.wait_and_verify_text(self, Constants.password_mismach_error, "הסיסמאות לא זהות, אולי זה מהתרגשות :)")

    def register_success(self):
        base.wait_and_enter_text(self, Constants.register_first_name, "register_success")
        base.wait_and_enter_text(self, Constants.register_email, "test@email.com")
        base.wait_and_enter_text(self, Constants.register_password, "Password")
        base.wait_and_enter_text(self, Constants.register_password_conf, "Password2")
        base.wait_and_click_on_element(self, Constants.agree_radio)
        # base.wait_and_click_on_element(self, Constants.submit)
