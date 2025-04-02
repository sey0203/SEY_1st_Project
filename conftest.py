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
from user_info import LOGIN_INFO
import tempfile

user_agents = [
    # Add your list of user agents here
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
]

@pytest.fixture(scope="function")
def driver():
    # 크롬 옵션 설정
    user_agent = random.choice(user_agents)
    user_data_dir = tempfile.mkdtemp()
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.delete_all_cookies()
    #  대기시간 설정
    driver.implicitly_wait(3)
    yield driver
    import shutil
    driver.quit()
    shutil.rmtree(user_data_dir)

@pytest.fixture
def login_driver(driver):

    url = "http://kdt-pt-1-pj-2-team03.elicecoding.com/"
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//button[text()='로그인하기']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "username").send_keys(LOGIN_INFO["user_id"])
    driver.find_element(By.ID, "password").send_keys(LOGIN_INFO["user_password"] + Keys.ENTER)
    WebDriverWait(driver,3).until_not(EC.url_contains("signin")) #signin이 url에 없어질때까지 명시적 대기
    yield driver

def generate_random_user_id():
    """랜덤한 사용자 ID를 생성합니다."""
    
    return "qwer"+str(random.randint(1,3))+"@qwer.qwer"

@pytest.fixture
def Rlogin_driver(driver):
    login_info = generate_random_user_id()

    url = "http://kdt-pt-1-pj-2-team03.elicecoding.com/"
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//button[text()='로그인하기']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "username").send_keys(login_info)
    driver.find_element(By.ID, "password").send_keys("qwerQWER1!" + Keys.ENTER)
    WebDriverWait(driver,3).until_not(EC.url_contains("signin")) #signin이 url에 없어질때까지 명시적 대기
    yield driver