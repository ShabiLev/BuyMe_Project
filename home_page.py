from selenium.webdriver.common.by import By
from base_page import BasePage as base


class Constants:
    login_register = By.CLASS_NAME, "notSigned"  # class="notSigned" data-ember-action="1011"
    register = "text-link theme"  # data-ember-action="1895" class="text-link theme"
    login_email = "ember1900"  # id="ember1900" type="email"
    login_password = "ember1907"  # id="ember1907" type="password"
    login_button = ""  # id="ember1916" required type="submit"
    register_first_name = ""  # id="ember1955" input#ember1878
    register_email = ""  # id="ember1962" required type="email"
    register_password = ""  # id="valPass"
    register_password_conf = ""  # id="ember1976"


class HomePage(base):

    def __init__(self, driver):
        base.__init__(self, driver)
        self.driver = base.driver

    def click_on_login(self):
        base.wait_and_click_on_element(self, Constants.login_register)
        print(self.driver.current_url)
