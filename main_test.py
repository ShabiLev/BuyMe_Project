import time
from unittest import TestCase
import base_page
from base_page import BasePage as base, driver
from pages.home_page import HomePage
from pages.register_page import Register


class TestBuyme(TestCase):

    def __init__(self, methodname: str = ...):
        super().__init__(methodname)

    def setUp(self):
        self.home_page = HomePage(base_page.driver)
        self.register_page = Register(base_page.driver)
        # base.goto_link(driver, "https://buyme.co.il/")
        driver.maximize_window()

    def test_success_register(self):
        base.goto_link(driver, "https://buyme.co.il/")
        self.home_page.click_on_login()
        self.home_page.click_on_register()
        self.home_page.verify_title_Registration()
        self.register_page.register_success()

    def tearDown(self):
        driver.quit()

# if __name__ == '__main__':
#     unittest.main()
