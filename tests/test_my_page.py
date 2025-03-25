#test_my_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random
import pytest
from pages.my_page import MyPage



@pytest.mark.usefixtures("login_driver")
class TestMyPage:
    @pytest.mark.skip()
    def test_001(self, driver:WebDriver):
        try:
            driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[4]/a').click() # 개인피드 클릭 임시
            WebDriverWait(driver,3).until(EC.url_contains("my"))
        except TimeoutException:
            print("URL에 'my'가 포함되지 않았습니다. ")
            assert False
    @pytest.mark.skip()
    def test_002(self,driver:WebDriver):
        try:            
            driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[3]/a').click() #히스토리 클릭 임시
            WebDriverWait(driver,3).until(EC.url_contains("history"))        
        except TimeoutException:
            print("URL에 'history'가 포함되지 않았습니다. ")
            assert False