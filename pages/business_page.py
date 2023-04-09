from selenium.webdriver.common.by import By
import base_page
from base_page import BasePage as base


class Constants:
    search_button = By.XPATH, "//a[@class='ember-view bm-btn no-reverse main md ember-view']"
    card_azrieli = By.XPATH, "//a[@title='AZRIELI GIFTCARD']"
    card_value = By.XPATH, '//input[@placeholder="הכנס סכום"]'
    card_submit = By.XPATH, '//button[@type="submit"]'

    card = By.XPATH, "//div[@class='bottom'][contains(text(), 'TEL AVIV')]"
    box_text = By.XPATH, '555'


class Business(base):

    def __init__(self, driver):
        base.__init__(self, driver)
        self.driver = base_page.driver

    def click_on_add_giftcard(self):
        # base.wait_and_click_element_text(self, Constants.search_text)
        base.wait_and_click_on_element(self, Constants.search_button)
        base.verify_link(self, "https://buyme.co.il/search")
        base.scroll_search_and_click_element(self, Constants.card, 5)
        # base.wait_and_click_on_element(self, Constants.card)
        base.wait_and_enter_text(self,Constants.card_value, "555")
        base.wait_and_click_on_element(self, Constants.card_submit)

