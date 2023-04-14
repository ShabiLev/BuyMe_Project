from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import base_page
from base_page import BasePage as base


class Constants:
    login_register = By.CLASS_NAME, "notSigned"
    register = By.CSS_SELECTOR, "h1[class=bm-h1]"
    register_type = By.TAG_NAME
    register_value = 'span'
    register_title = By.CLASS_NAME, "lightbox-head"

    drop_price = By.XPATH, "//span[@title='סכום']"
    drop_amount = By.XPATH, "//span[contains(text(), '300-499')]"
    drop_erea = By.XPATH, "//span[@title='אזור']"
    drop_suberea = By.XPATH, "//span[text()='השרון']"
    drop_category = By.XPATH, "//span[@title='קטגוריה']"
    drop_subcategory = By.XPATH, "//span[contains(text(), 'מסעדות שף')]"
    button_find_gift = By.XPATH, "//a[@rel='nofollow']"

    spinner_type = By.CLASS_NAME #By.XPATH
    spinner_value = "spinner" #'//div[@class="spinner"]'
    spinner = By.CLASS_NAME, 'spinner'#By.XPATH, '//div[@class="spinner"]' #"//*[@id='ember964']" #"//*[@id='app-loading-img']" # "spinner"xpath///*[@id="app-loading-img"]/div


class HomePage(base):

    def __init__(self, driver):
        base.__init__(self, driver)
        self.driver = base_page.driver

    def click_on_login(self):
        base.wait_and_click_on_element(self, Constants.login_register)

    def click_on_register(self):
        base.wait_and_click_on_below_element(self, Constants.register, Constants.register_type, Constants.register_value)

    def verify_title_Registration(self):
        base.wait_and_verify_text(self, Constants.register_title, "הרשמה")

    def search_for_present(self):
        self.driver.execute_script(f"window.scrollBy(0, 300);")
        base.wait_and_click_on_element(self, Constants.drop_price)
        base.wait_and_click_on_element(self, Constants.drop_amount)
        base.wait_and_click_on_element(self, Constants.drop_erea)
        base.wait_and_click_on_element(self, Constants.drop_suberea)
        base.wait_and_click_on_element(self, Constants.drop_category)
        base.wait_and_click_on_element(self, Constants.drop_subcategory)
        base.wait_and_click_on_element(self, Constants.button_find_gift)

    def scroll_to_bottom_screen(self):
        # Scroll to the bottom of the page
        base.scroll_webpage(self, "down")

    def get_spinner_size(self):
        base.goto_link(self, base_page.datajson['urls']['buymehome'])
        base.chrome_subtree_modifications(self)
        base_page.driver.refresh()
        base.get_element_size(self, Constants.spinner_type, Constants.spinner_value)

