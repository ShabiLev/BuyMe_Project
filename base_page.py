import os
import time
from datetime import datetime

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import traceback
from PIL import ImageGrab

logfilePath = "C:\\Users\\" + os.getlogin() + "\\Downloads\\Python Automation Files\\BuyMe_Project\\Errors\\"
driver = webdriver.Chrome(service=Service("C:\\Users\\shabil\\Downloads\\Python Automation Files\\BuyMe_Project\\Drivers\\chromedriver_win32\\chromedriver.exe"))

timeout = 10


def get_current_time():
    now = datetime.now()
    cur_date_time = now.strftime("%d-%m-%Y_%H-%M-%S")
    return cur_date_time

class BasePage:
    # Configure logging to write to a file
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(
        filename=logfilePath + "BuyMe_log.txt",
        filemode='a',
        format="%(asctime)s, %(name)s %(levelname)s %(message)s \n",
        datefmt="%H:%M:%S",
        level=logging.ERROR)

    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self):
        screenshot = ImageGrab.grab()
        if os.path.exists(f"{logfilePath}{get_current_time()}_ScreenShot.png"):
            time.sleep(0.1)
            screenshot.save(f"{logfilePath}{get_current_time()}_ScreenShot.png")
        else:
            screenshot.save(f"{logfilePath}{get_current_time()}_ScreenShot.png")

    def goto_link(self, link):
        try:
            driver.get(link)
            WebDriverWait(driver, timeout).until(EC.url_to_be(link))
        except Exception as e:
            logging.exception(str(e))
            self.take_screenshot()

    def wait_and_click_on_element(self, locator):
        try:
            WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator)).click()
        except Exception as e:
            logging.exception(str(e))
            self.take_screenshot()

    def wait_and_click_on_above_element(self, relative, elem_type, elem_val):
        try:
            relative_element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(relative))
            driver.find_element(locate_with(elem_type, elem_val).above(relative_element)).click()
        except Exception as e:
            logging.exception(str(e))
            self.take_screenshot()

    def wait_and_click_on_below_element(self, relative, elem_type, elem_val):
        try:
            relative_element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(relative))
            driver.find_element(locate_with(elem_type, elem_val).below(relative_element)).click()
        except Exception as e:
            logging.exception(str(e))
            self.take_screenshot()

    def wait_and_enter_text(self, locator, text):
        try:
            WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator)).send_keys(text)
        except Exception as e:
            logging.exception(str(e))
            self.take_screenshot()

    def wait_and_verify_text(self, locator, expected_text):
        try:
            text1 = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
            text = text1.text
            if expected_text not in text:
                logging.error(f"String {expected_text} wasn't found in {text}")
                self.take_screenshot()
            else:
                logging.info(f"Found String {expected_text} in {text}")
                self.take_screenshot()
                return text
        except Exception as e:
            logging.exception(str(e))
            self.take_screenshot()
