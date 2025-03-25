import time
import pytest
import random
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from pages.login_page import LoginPage
from pages.signup_page import SinupPage

@pytest.mark.usefixtures("driver")
class TestSignupPage:
    
    def test_signup_TC001(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            login_page.open()
            #페이지 로딩
            wait = ws(driver, 10) 
            wait.until(EC.url_contains("signin"))
            assert "signin" in driver.current_url
            #로그인 버튼 클릭
            button=driver.find_element(By.XPATH, '//*[@id="root"]//button[contains(text(),"로그인")]')
            button.click()
            
            wait.until(EC.url_contains("login"))
            assert "login" in driver.current_url
            login_page.login("qwer1@qwer.qwer","qwerQWER1!")
            
            driver.find_element(By.NAME, "name").send_keys("1234")
            

            option = driver.find_element(By.XPATH, '//*[@id="root"]//select')
            select_element = Select(option)
            # 옵션 개수 확인 및 품절 여부 확인 후 선택
            target_option = select_element.options[random.randint(1, len(select_element.options) - 1)]
            select_element.select_by_visible_text(target_option.text)
            
            time.sleep(5)
        except NoSuchElementException as e:
            print("")
            assert False#
