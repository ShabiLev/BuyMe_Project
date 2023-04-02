import time
import unittest
from unittest import TestCase
from base_page import BasePage as base, driver
from home_page import HomePage


class TestBuyme(TestCase):

    def __init__(self, methodname: str = ...):
        super().__init__(methodname)


    def setUp(self):
        driver = base.driver
        self.home_page = HomePage(base.driver)
        base.goto_link(driver, "https://buyme.co.il/")

    def test_login_button(self):
        self.home_page.click_on_login()

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()
