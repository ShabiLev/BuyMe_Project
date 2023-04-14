import os
import time
import json
from datetime import datetime

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys, DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from PIL import ImageGrab

# Get the username of the current user
username = os.getlogin()
tmp_folder = "OneDrive - Ofakim Group"
file_path = "C:\\Users\\" + username + "\\" + tmp_folder + "\\Desktop\\BuyMe_Project\\"
json_file = open(f"{file_path}Data.json", 'r')
datajson = json.load(json_file)
chrome_options = Options()

# --- Headless = window does not come up ---
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(service=Service(datajson['explorer_drivers']['chrome']), options=chrome_options)

# --- Run on saucelabs ---
# options = Options()
# options.browser_version = 'latest'
# options.platform_name = 'Windows 11'
# sauce_options = {'username': "oauth-shabi231-5667f",
#                  'browserName': 'Chrome',
#                  'build': 'BuyMe testing',
#                  'name': 'Remote Cloud testing',
#                  'accessKey': 'e0f64cf3-daf1-46ad-8da4-e85eba76f940',
#                  'version': '105'}
#
# options.set_capability('sauce:options', sauce_options)
# sauce_url = "https://oauth-shabi231-5667f:e0f64cf3-daf1-46ad-8da4-e85eba76f940@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
# driver = webdriver.Remote(command_executor=sauce_url, options=options)

driver = webdriver.Chrome(service=Service(datajson['explorer_drivers']['chrome']))
ErrorsFilePath = datajson['locations']['Errors']
timeout = datajson["variables"]['timeout']


def get_current_time():
    """
    Returns the current Time in the format of dd-mm-YYYY_H-M-S
    For example: 31-06-2023_18-25-48
    06-04-2023_18-26-14.
    """
    now = datetime.now()
    cur_date_time = now.strftime("%d-%m-%Y_%H-%M-%S")
    return cur_date_time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    chrome_options = Options()

    # Configure logging to write to a file
    logger = logging.getLogger()
    # logger.setLevel(logging.INFO)
    logging.basicConfig(
        filename=ErrorsFilePath + "BuyMe_log.txt",
        filemode='a',
        format="%(asctime)s, %(name)s %(levelname)s %(message)s \n",
        datefmt="%H:%M:%S",
        level=logging.INFO)

    def save_screenshot(self, comment=None):
        """
        Capturing a screenshot by using the "ImageGrab" library from PIL.

        :param comment: NOT Mandatory, the extra text String to add to the image File Name.

        It automatically saves the screenshots to a pre-define logfilePath with

        the current Time in the format of dd-mm-YYYY_H-M-S.
        """
        screenshot = ImageGrab.grab()
        if os.path.exists(f"{ErrorsFilePath}{get_current_time()}_{comment}_ScreenShot.png"):
            time.sleep(0.1)
            screenshot.save(f"{ErrorsFilePath}{get_current_time()}_{comment}_ScreenShot.png")
        else:
            screenshot.save(f"{ErrorsFilePath}{get_current_time()}_{comment}_ScreenShot.png")

    def goto_link(self, link):
        """
        This function open a provided url
        then waits for the URL of the current page to match the provided link.

        If the link does not match the URL after the provided timeout,
        an exception is raised and a screenshot is taken.

        :param link: the required url to be validated.
        """
        try:
            driver.get(link)
            WebDriverWait(driver, timeout).until(EC.url_to_be(link))
            time.sleep(0.5)
        except Exception as e:
            logging.exception(str(e))
            self.save_screenshot("goto_link-Failed")

    def verify_link(self, link):
        """
        This function waits for the URL of the current page to match the provided link.
        If the link does not match the URL after the provided timeout,
        an exception is raised and a screenshot is taken.

        :param link: the required url to be validated.
        """
        try:
            WebDriverWait(driver, timeout).until(EC.url_to_be(link))
        except Exception as e:
            logging.exception(str(e))
            self.save_screenshot("verify_link-Failed")

    def wait_and_click_on_element(self, locator):
        """
        This function waits for an element located by the provided locator to be clickable,
        and then clicks on it. If the element cannot be clicked within the provided timeout,
        an exception is raised and a screenshot is taken.

        :param locator: The Element to wait for.

        exampe: locator = By.CLASS_NAME, "value"
        """
        try:
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator)).click()
            time.sleep(0.1)
        except Exception as e:
            logging.exception(str(e))
            self.save_screenshot("wait_and_click_on_element-Failed")

    def wait_and_click_element_text(self, text):
        """
        This function searching for an Element by it's Text then Click it.

        :param text: The Element's to search for.
        """
        try:
            self.driver.find_element_by_link_text(text).click()
        except Exception as e:
            logging.exception(str(e))
            self.save_screenshot("wait_and_click_element_text-Failed")

    def wait_and_click_on_above_element(self, relative, elem_type, elem_val):
        try:
            relative_element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(relative))
            driver.find_element(locate_with(elem_type, elem_val).above(relative_element)).click()
        except Exception as e:
            logging.exception(str(e))
            self.save_screenshot("wait_and_click_on_above_element-Failed")

    def wait_and_click_on_below_element(self, relative, elem_type, elem_val):
        try:
            relative_element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(relative))
            driver.find_element(locate_with(elem_type, elem_val).below(relative_element)).click()
        except Exception as e:
            logging.exception(str(e))
            self.save_screenshot("wait_and_click_on_below_element-Failed")

    def wait_and_enter_text(self, locator, text):
        """
        This function wait for an Element and input required text to it.

        :param locator: the Element to look for.
        :param text: The Element's text to enter.
        """
        try:
            WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator)).send_keys(text)
        except Exception as e:
            logging.exception(str(e))
            self.save_screenshot("wait_and_enter_text-Failed")

    def wait_and_verify_text(self, locator, expected_text):
        try:
            text1 = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
            text = text1.text
            if expected_text not in text:
                logging.debug(f"String {expected_text} wasn't found in {text}")
                self.save_screenshot(f"String_{expected_text}_wasn't_found")
            else:
                logging.info(f"Found String {expected_text} in {text}")
                # self.save_screenshot("String_was_found")
                return text
        except Exception as e:
            logging.exception(str(e))
            self.save_screenshot("wait_and_verify_text-Failed")

    def wait_and_select_from_dropdown_by_text(self, locator, text):
        try:
            selector = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
            selection = Select(selector)
            selection.select_by_visible_text(text)
        except Exception as e:
            logging.exception(str(e))
            self.save_screenshot("wait_and_select_from_dropdown_by_text-Failed")

    def scroll_webpage(self, direction: str) -> None:
        """
        Scroll the webpage up or down based on the provided direction.

        :param direction: The direction to scroll the webpage.

        Use 'up' to scroll to the top, and 'down' to scroll to the bottom.
        """
        try:
            if direction == "up":
                # Scroll to the top of the page
                driver.execute_script("window.scrollTo(0, 0);")
                self.save_screenshot("Scroll-Top")
            elif direction == "down":
                # Scroll to the bottom of the page
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                self.save_screenshot("Scroll-Bottom")
        except Exception as e:
            # Invalid direction parameter
            logging.exception(str(e))
            self.save_screenshot("scroll_webpage-Failed")

    def scroll_search_and_click_element(self, locator, times):
        """
        Scrolls to the top of the page, then searches for an element repeatedly.
        If the element is found, clicks it. If not found after a specified number of attempts,
        logs an error.

        :param locator: The locator for the element to search for.
        :param times: The maximum number of times to scroll and search before logging an error.
        """
        time.sleep(0.5)
        scroll_amount = 300
        # driver.execute_script("window.scrollTo(0, 0)")
        for i in range(times):
            try:
                WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
                ActionChains(driver).move_to_element(locator).click().perform()
                return
            except Exception as e:
                self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
                logging.exception(str(e))
        logging.error(f"Element {locator} wasn't found after {times} times")
        self.save_screenshot("scroll_and_search_element-Failed")

    def find_and_click_text_in_elements(self, locator_type, locator_value, element_text: str):
        """
        List all the elements based on the locator_type and locator_value
        then check for every one if it's text value equals to the expected text.

        :param locator_type: The element type to search for.
        :param locator_value: The element value to search for.
        :param element_text: The expected text.
        """
        try:
            elements = driver.find_elements(locator_type, locator_value)
            time.sleep(0.1)
            for element in elements:
                if element_text in element.text:
                    element.click()
                    break
        except Exception as e:
            logging.exception(str(e))
            self.save_screenshot("find_and_click_text_in_elements-Failed")

    def clear_text(self, locator):
        """
        Locate an element then select all text in it and delete it by {Ctrl + "a" + Delete}
        :param locator: The locator for the element to search for.
        """
        try:
            WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator)).send_keys(Keys.CONTROL + "a")
            WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator)).send_keys(Keys.DELETE)
        except Exception as e:
            logging.exception(str(e))
            self.save_screenshot("clear_text-Failed")

    def upload_file(self, locator, file):
        """
        Locate an element then "send" it a file
        :param locator: The locator for the element to search for.
        :param file: Enter FULL path of a file Or the file name under 'BuyMe_Project\\Samples\'
        """
        relativePath = "c:"
        try:
            # base.upload_file(self, Constants.upload_image, logical + "\\Superman_symbol.png")
            if relativePath in file:
                WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator)).send_keys(file)
            else:
                WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator)).send_keys(datajson['locations']['Samples'] + file)
        except Exception as e:
            logging.exception(str(e))
            self.save_screenshot("upload_file-Failed")

    def get_element_size(self, locator_type, locator_value):
        """
        This function search for an element and get it's size

        :param locator:
        """
        try:
            # WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located(locator))
            element = driver.find_element(locator_type, locator_value)
            element_size = element.size
            print(element_size)
            logging.info(f"Element {locator_type, locator_value} size is {element_size}")
            logging.info("test")
        except Exception as e:
            logging.exception(str(e))
            self.save_screenshot("get_element_size-Failed")

    def chrome_subtree_modifications(self):
        chrome_options.add_argument("--remote-debugging-port=9222")

        # Define the desired capabilities
        caps = DesiredCapabilities.CHROME.copy()
        caps['goog:loggingPrefs'] = {'browser': 'ALL', 'performance': 'ALL'}
        caps['goog:chromeOptions'] = {'w3c': True, 'args': ['--disable-extensions']}
        caps['pageLoadStrategy'] = 'none'
        caps['unexpectedAlertBehaviour'] = 'dismiss'
        caps['loggingPrefs'] = {'performance': 'ALL'}

        # Start the ChromeDriver service
        chrome_service = Service(executable_path=datajson['explorer_drivers']['chrome'])

        # Start the ChromeDriver instance with the defined options and capabilities
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options, desired_capabilities=caps)

        # Connect to the DevTools instance
        driver.execute_cdp_cmd('Page.enable', {})
        driver.execute_cdp_cmd('Network.setRequestInterception', {
            'patterns': [
                {
                    'urlPattern': '*',
                    'resourceType': 'Document',
                    'interceptionStage': 'HeadersReceived'
                }
            ]
        })
        driver.execute_cdp_cmd('Debugger.enable', {})
        driver.execute_cdp_cmd('Debugger.setBreakpointsActive', {'active': True})

    def click_on_location(self, loc_x, loc_y):
        pyautogui.click(loc_x, loc_y)

