#history_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random

class HistoryPage:
    URL = "http://kdt-pt-1-pj-2-team03.elicecoding.com/"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def history_btn(self):
        return self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[3]/a')
    
    def back_btn(self):
        return self.driver.find_element(By.CLASS_NAME,'cursor-pointer')
    
    def GNB_name(self):
        return self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/header/div/span').text
    
    def menus(self):
        menu_list = []
        
        boxes = self.driver.find_elements(By.XPATH, "//div[@class='flex w-full gap-6 p-4 shadow-md rounded-2xl']")
        for box in boxes:
            menu_name = box.find_element(By.XPATH, ".//div[@class='font-bold']").text
            scores = box.find_elements(By.XPATH,".//div[@class='text-subbody']")
            for score in scores:
                menu_list.append(score.text)
            menu_list.append(menu_name)
        return menu_list


