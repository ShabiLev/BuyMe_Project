import json
from unittest import TestCase
import base_page
from base_page import BasePage as base, driver
from pages.home_page import HomePage
from pages.register_page import Register


class TestBuyme(TestCase):

    def __init__(self, methodname: str = ...):
        super().__init__(methodname)

    @classmethod
    def setUpClass(self):
        self.home_page = HomePage(base_page.driver)
        self.register_page = Register(base_page.driver)
        driver.maximize_window()

    def test_a_success_register(self):
        base.goto_link(driver, base_page.datajson['urls']['buymehome'])
        self.home_page.click_on_login()
        self.home_page.click_on_register()
        self.home_page.verify_title_Registration()
        self.register_page.register_success()

    def test_b_fail_register(self):
        base.goto_link(driver, base_page.datajson['urls']['buymehome'])
        self.home_page.click_on_login()
        self.home_page.click_on_register()
        self.home_page.verify_title_Registration()
        self.register_page.register_fail_email()

    def test_c_fail_password(self):
        base.goto_link(driver, "https://buyme.co.il/")
        self.home_page.click_on_login()
        self.home_page.click_on_register()
        self.home_page.verify_title_Registration()
        self.register_page.register_fail_password()

    @classmethod
    def tearDownClass(self):
        driver.quit()
