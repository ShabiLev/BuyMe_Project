import os
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

logfilePath = "C:\\Users\\" + os.getlogin() + "\\OneDrive - Ofakim Group\\Desktop\\BuyMe_Files\\"
driver = webdriver.Chrome(service=Service("C:\\Users\\shabil\\Downloads\\chromedriver_win32\\chromedriver.exe"))
timeout = 10


def get_current_time():
    now = datetime.now()
    cur_date_time = now.strftime("%d-%m-%Y %H:%M:%S")
    return cur_date_time

class BasePage:
    # Configure logging to write to a file
    logging.basicConfig(
        filename=logfilePath + "BuyMe_log.txt",
        filemode='a',
        format="%(asctime)s, %(name)s %(levelname)s %(message)s \n",
        datefmt="%H:%M:%S",
        level=logging.ERROR)

    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self):
        count = 1
        screenshot = ImageGrab.grab()
        # if os.path.exists(logfilePath + 'error in ' + str(count) + '.png'):
        if os.path.exists(f"{logfilePath} {get_current_time()} error.png"):
            count += 1
            screenshot.save(f"{logfilePath} {get_current_time()} error.png")
        else:
            screenshot.save(f"{logfilePath} {get_current_time()} error.png")



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

    def wait_and_get_elem_text(self, locator):
        try:
            text1 = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
            text = text1.text
            return text
        except Exception as e:
            logging.exception(str(e))
            self.take_screenshot()
