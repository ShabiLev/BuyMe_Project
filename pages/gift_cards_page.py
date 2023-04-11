from selenium.webdriver.common.by import By
import base_page
from base_page import BasePage as base


class Constants:
    card_chef = By.XPATH, "//span[contains(text(), 'BUYME CHEF')]"
    input_amount = By.XPATH, "//input[contains(@placeholder, 'הכנס סכום')]"
    button_select = By.XPATH, "//button[contains(@gtm, 'בחירה')]"

class giftcardsPage(base):

    def __init__(self, driver):
        base.__init__(self, driver)
        self.driver = base_page.driver

    def click_on_gift_card(self):
        base.wait_and_click_on_element(self, Constants.card_chef)
        base.wait_and_enter_text(self,Constants.input_amount, "666")
        base.wait_and_click_on_element(self, Constants.button_select)
