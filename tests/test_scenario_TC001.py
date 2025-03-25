import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from urllib import parse
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import Select
import random

@pytest.mark.usefixtures("driver")
class TestMainPage:

    def test_TC001(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)

            login_page.open()
            time.sleep(1)        
            wait = ws(driver, 10) 
            wait.until(EC.url_contains("signin"))
            assert "signin" in driver.current_url
            
            button=driver.find_element(By.XPATH, '//*[@id="root"]//button[contains(text(),"로그인")]')
            button.click()
            wait.until(EC.url_contains("login"))
            assert "login" in driver.current_url


            print(login_page.login("qwer1@qwer.qwer","qwerQWER1!"))
            time.sleep(3)
            
            driver.back()
            wait.until(EC.url_contains("signin"))

            button=driver.find_element(By.XPATH, '//*[@id="root"]//button[contains(text(),"회원가입")]')
            button.click()
            wait.until(EC.url_contains("u/signup"))
            assert "u/signup" in driver.current_url
            login_page.input_userinfo("qwer@qwer.qwer","qwerqwer")
            print(login_page.check_password_length_color())
            
            time.sleep(5)
        except NoSuchElementException as e:
            assert False

            