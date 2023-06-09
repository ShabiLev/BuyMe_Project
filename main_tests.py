import time
import unittest

from selenium.webdriver.common.by import By

import base_page
from PIL import Image
from base_page import BasePage as base, driver
from pages.home_page import HomePage
from pages.register_page import Register
from pages.business_page import Business_page
from pages.gift_cards_page import giftcardsPage
from pages.acquire_present_page import acquirePage


class TestLoginRegister(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.home_page = HomePage(base_page.driver)
        self.register_page = Register(base_page.driver)
        self.business_page = Business_page(base_page.driver)
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
        base.goto_link(driver, base_page.datajson['urls']['buymehome'])
        self.home_page.click_on_login()
        self.home_page.click_on_register()
        self.home_page.verify_title_Registration()
        self.register_page.register_fail_password()

    # @classmethod
    # def tearDownClass(self):
    #     driver.quit()


class TestFindGifts(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.home_page = HomePage(base_page.driver)
        self.gift_card_page = giftcardsPage(base_page.driver)
        self.acquire_present_page = acquirePage(base_page.driver)
        driver.maximize_window()

    def test_g_search_for_present(self):
        base.goto_link(driver, base_page.datajson['urls']['buymehome'])
        self.home_page.search_for_present()

    def test_h_select_cards(self):
        base.goto_link(driver, "https://buyme.co.il/search?budget=4&category=16&region=2835")
        self.gift_card_page.click_on_gift_card()

    def test_j_acquire_gift(self):
        base.goto_link(driver, "https://buyme.co.il/money/752649?price=666")
        self.acquire_present_page.select_reciver()
        self.acquire_present_page.upload_image()
        self.acquire_present_page.enter_order_details()
        # time.sleep(200)


class TestGen(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.home_page = HomePage(base_page.driver)
        self.acquire_page = acquirePage(base_page.driver)
        driver.maximize_window()

    def test_r_get_element_characteristics(self):
        base.goto_link(driver, "https://buyme.co.il/money/13438757?price=777")
        self.acquire_page.element_characteristics()

    def test_x_get_spinner_size(self):
        # base.goto_link(driver, base_page.datajson['urls']['buymehome'])
        self.home_page.get_spinner_size()

    def test_y_scroll_to_bottom(self):
        base.goto_link(driver, base_page.datajson['urls']['buymehome'])
        self.home_page.scroll_to_bottom_screen()


    # @classmethod
    # def tearDownClass(self):
    #     driver.quit()

    def tearDown(self):
        driver.quit()

