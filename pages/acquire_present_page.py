import time

from selenium.webdriver.common.by import By
import base_page
from base_page import BasePage as base


class Constants:
    for_who = By.XPATH, "//div[@gtm='למישהו אחר']"
    receiver_name = By.XPATH, "//input[contains(@title, 'שם מקבל המתנה')]"
    event_type = By.XPATH, "//span[contains(@title, 'לאיזה אירוע')]"
    event_value = By.XPATH, "//li[@value='11']"
    grace_text = By.XPATH, "//textarea[@data-parsley-group='voucher-greeting']"
    upload_image = By.XPATH, "//input[@type='file']"
    continue_button = By.XPATH, "//button[@type='submit']"

    select_now = By.XPATH, "//div[@class='ember-view button button-now selected']"
    method_sms = By.XPATH, "//svg[@gtm='method-sms']"
    all_circles = By.XPATH, "//path[@class='circle']"
    mobile = By.XPATH, "//input[@data-parsley-mobile='mobile']"
    sender_name = By.XPATH, "//input[@placeholder='שם שולח המתנה']"
    sender_mobile = By.XPATH, "//input[@placeholder='מספר נייד']"

    # whom = By.XPATH, "//div[@class='number'][contains(text(), '1')]"
    whom = By.CSS_SELECTOR, '.step.active .label'


class acquirePage(base):

    def __init__(self, driver):
        base.__init__(self, driver)
        self.driver = base_page.driver

    def select_reciver(self):
        self.driver.execute_script(f"window.scrollBy(0, 400);")
        base.wait_and_click_on_element(self, Constants.for_who)
        base.wait_and_enter_text(self, Constants.receiver_name, "MeMeMe")
        base.wait_and_click_on_element(self, Constants.event_type)
        base.wait_and_click_on_element(self, Constants.event_value)
        base.clear_text(self, Constants.grace_text)
        base.wait_and_enter_text(self, Constants.grace_text, "MeMeMe")

    def upload_image(self):
        base.wait_and_click_on_element(self, Constants.upload_image)
        base.upload_file(self, Constants.upload_image, "Superman_symbol.png")
        base.wait_and_click_on_element(self, Constants.continue_button)

    def enter_order_details(self):
        time.sleep(1)
        self.driver.execute_script(f"window.scrollBy(0, 350);")
        base.wait_and_click_on_element(self, Constants.select_now)
        base.wait_and_click_on_element(self, Constants.method_sms)
        base.wait_and_enter_text(self, Constants.mobile, "123456789")
        base.wait_and_enter_text(self, Constants.sender_name, "Sender Name")
        base.wait_and_enter_text(self, Constants.sender_mobile, "987654321")

    def element_characteristics(self):
        base.get_element_characteristics(self, Constants.whom)
