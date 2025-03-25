from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random

class LoginPage:
    URL = "http://kdt-pt-1-pj-2-team03.elicecoding.com/"
    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def open_page(self, url : str):
        self.driver.get(url)
    
    def input_userinfo(self, username, password):
        """사용자 이름과 비밀번호를 입력하는 함수"""
        try:
            #로그인 텍스트 인풋의 ID는 username 회원가입 텍스트 인풋의 아이디는 emaill이라 이방법을 사용 By.ID "username" By.ID "email"
            username_field = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'input c59b33b40')]")) 
            )
            username_field.send_keys(username)
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(password)
            #password_field.send_keys(password + Keys.ENTER) 
            return True  
        except NoSuchElementException:
            print("입력 필드를 찾을 수 없습니다.")
            return False  
        except TimeoutException:
            print("입력 필드 로딩 시간 초과.")
            return False
        except Exception as e:
            print(f"입력 중 오류 발생: {e}")
            return False  
    
    def login(self, username, password):
        try:
            url = self.driver.current_url
            if not self.input_userinfo(username, password):  # 입력 실패 시 False 반환
                return False

           
            try:
                error_element = WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located((By.ID, "error-element-password"))  
                )
                print(f"로그인 실패: {error_element.text}")
                return False
            except TimeoutException:
                # 오류 메시지 요소가 없으면 로그인 성공으로 판단
                try:
                    WebDriverWait(self.driver, 1).until(
                        EC.url_changes(url))
                    print("로그인 성공")
                    return True
                except TimeoutException:
                    print("로그인 실패: 페이지 변경 없음")
                    return False
                
        except Exception as e:
            print(f"로그인 중 오류 발생: {e}")
            return False
        
    def check_password_length_color(driver):
        try:
            length_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.cac336714"))
            )
            color = length_element.value_of_css_property("color")
            return color
        except Exception as e:
            print(f"오류 발생: {e}")
            return None
