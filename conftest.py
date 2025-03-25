# conftest.py
import random
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    
    
    # 크롬 옵션 설정
    chrome_options = Options()
    
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    #도커 젠킨스 실행용 코드
    # chrome_options .add_argument("--headless")
    # chrome_options .add_argument("--no-sandbox")
    # chrome_options .add_argument("--disable-dev-shm-usage")

    # chrome_options.add_argument('--disable-dev-shm-usage')  # shared memory 문제 방지
    # chrome_options.add_argument('--disable-gpu')  # 가상환경에서 GPU 기능 비활성화
   
    # 드라이버 객체 생성
    
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
        # instantiate a Chrome browser and add the options



    driver.delete_all_cookies()
    #  대기시간 설정
    driver.implicitly_wait(5)
    
    yield driver 

    # 테스트가 끝나면 드라이버 종료
    driver.quit()


@pytest.fixture
def login():
    print("임시 기능입니다..")
    #로그인 픽스쳐를 만드는 공간