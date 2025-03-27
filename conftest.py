# conftest.py
import random
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    # 크롬 옵션 설정
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.delete_all_cookies()
    #  대기시간 설정
    driver.implicitly_wait(1)
    yield driver
    # 테스트가 끝나면 드라이버 종료
    driver.quit()

@pytest.fixture
def login_driver(driver):
    #이메일과 비밀번호 입력
    email = "gogo@gmail.com"
    password = "!Q2w3e4r"

    url = "http://kdt-pt-1-pj-2-team03.elicecoding.com/"
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//button[text()='로그인하기']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password + Keys.ENTER)
    WebDriverWait(driver,3).until_not(EC.url_contains("signin")) #signin이 url에 없어질때까지 명시적 대기
    yield driver