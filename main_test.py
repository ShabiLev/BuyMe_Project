import unittest
import base_page
from base_page import BasePage as base, driver
from pages.home_page import HomePage
from pages.register_page import Register
from pages.business_page import Business


class TestBuyme(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.home_page = HomePage(base_page.driver)
        self.register_page = Register(base_page.driver)
        self.business_page = Business(base_page.driver)
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

    # def test_d_select_gift(self):
    #     base.goto_link(driver, base_page.datajson['urls']['buymehome'])
    #     base.click_on_location(driver, 1100, 510)
    #     # driver.get("https://buyme.co.il/search")
    #     # driver.find_element(By.ID, "ember4547").click()
    #     # # self.home_page.search_for_present()
    #     # # self.business_page.click_on_add_giftcard()
    #     time.sleep(30)

    # @classmethod
    # def tearDownClass(self):
    #     driver.quit()


class TestGen(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.home_page = HomePage(base_page.driver)
        # driver.maximize_window()

    def test_x_scroll_to_bottom(self):
        base.goto_link(driver, base_page.datajson['urls']['buymehome'])
        self.home_page.scroll_to_bottom_screen()

    # @classmethod
    # def tearDownClass(self):
    #     driver.quit()

    def tearDown(self):
        driver.quit()

