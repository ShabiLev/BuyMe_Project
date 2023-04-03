import time
from unittest import TestCase
import base_page
from base_page import BasePage as base, driver
from pages.home_page import HomePage


class TestBuyme(TestCase):

    def __init__(self, methodname: str = ...):
        super().__init__(methodname)

    def setUp(self):
        self.home_page = HomePage(base_page.driver)
        base.goto_link(driver, "https://buyme.co.il/")

    def test_login_button(self):
        self.home_page.click_on_login()
        self.home_page.click_on_register()

        time.sleep(10)

    def tearDown(self):
        driver.quit()

# if __name__ == '__main__':
#     unittest.main()
