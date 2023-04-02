import os
import datetime
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v111.animation import get_current_time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logfilePath = "C:\\Users\\" + os.getlogin() + "\\OneDrive - Ofakim Group\\Desktop\\BuyMe_log.txt"
driver = webdriver.Chrome(service=Service("C:\\Users\\shabil\\Downloads\\chromedriver_win32\\chromedriver.exe"))
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

timeout = 10


def get_current_time():
    now = datetime.datetime.now()
    cur_date_time = now.strftime("%d-%m-%Y %H:%M:%S")
    return str(cur_date_time)


def open_log():
    os.system('notepad.exe ' + logfilePath)


def clear_log():
    open(logfilePath, 'w').close()


def log_to_file(what_to_log):
    logFile = open(logfilePath, 'a')
    logFile.write('\n' + get_current_time() + ' - ' + what_to_log)
    logFile.close()

class BasePage:
    driver = webdriver.Chrome(service=Service("C:\\Users\\shabil\\Downloads\\chromedriver_win32\\chromedriver.exe"))

    def __init__(self, driver):
        self.driver = driver

    def goto_link(self, link):
        try:
            driver.get(link)
            WebDriverWait(driver, timeout).until(EC.url_to_be(link))
        except TimeoutException:
            log_to_file(f'Timed out waiting for page {link} to load')

    def wait_and_click_on_element(self, locator):
        try:
            WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator)).click()
        except TimeoutException:
            log_to_file(f'Timed out waiting for element {locator}')

    def enter_text(self, locator):
        try:
            WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locatore)).send_keys(text)
        except TimeoutException:
            log_to_file(f'Timed out waiting for element {locator}')

    def wait_and_get_elem_text(self, locator):
        try:
            text1 = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
            text = text1.text
            return text
        except TimeoutException:
            log_to_file(f'Timed out waiting for element {locator}')
