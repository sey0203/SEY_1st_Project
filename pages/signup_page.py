import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SinupPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def open(self):
        self.driver.get(self.URL)

    def open_page(self, url : str):
        self.driver.get(url)
    
    # def set_slider(self, value : float):
    #     flavor_section = ws(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, flavor_section_xpath))
    #         )
    #     thumb_element = flavor_section.find_element(By.XPATH, ".//span[@role='slider']")



    # 10 0.2
    # 100 2.0
    # 200 4.0
    # 250 5.0
    # 5 250
    # 4 200
    # 1 *50