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
