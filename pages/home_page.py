# Chrome 브라우저를 제어하기 위한 import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# 페이지 요소를 찾거나 입력 동작을 구현하기 위한 import
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 특정 요소가 로드될 때 까지 기다리기 위한 import
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 테스트 구조와 실행을 관리하기 위한 라이브러리
import pytest

@pytest.mark.usefixtures("login_driver")

# HomePage 클래스 정의
class HomePage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.base_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/"
        self.alone_page_url = self.base_url + "electoptions/alone"

    def load(self):
        """홈 페이지를 로드"""
        self.driver.get(self.base_URL)

    def load_alone_page(self):
        """혼자 먹기 페이지 로드"""
        self.driver.get(self.alone_page_url)

    def is_home_loaded(self):
        """홈 페이지가 로드 되었는지 확인"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[1]/button[1]')
                )
            )
            return True
        except Exception:
            return False
        
    def click_solo_button(self):
        """'혼자 먹기' 버튼 클릭"""
        solo_button_xpath = '//*[@id="root"]/div[1]/main/section/div/div[1]/button[1]'
        solo_button = self.driver.find_element(By.XPATH, solo_button_xpath)
        solo_button.click()
        
    def select_categoty(self, category):
        """음식 카테고리를 선택"""
        dropdown_xpath = '//button[@role="combobox"]'
        dropdown = self.driver.find_element(By.XPATH, dropdown_xpath)
        dropdown.click()

        #카테고리 클릭 (한식 선택)
        category_xpath = '//*[@id="root"]/div[1]/main/section/div/div[1]/button/span'
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_xpath))
        )
        category_option = self.driver.find_element(By.XPATH, category_xpath)
        category_option.click()

    def click_compltet_button(self):
        """선택 완료 버튼 클릭"""


# 테스트 케이스 정의
@pytest.fixture(scope="module")
def driver():
    """WebDriver 설정 및 초기화"""
    service = Service() # ChromeDriver 자동 설정 생략
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

# 혼자 먹기 버튼 클릭 > 페이지 이동 확인 
def test_click_solo_button(driver):
    """'혼자 먹기' 버튼 테스트"""
    home_page = HomePage(driver)

    # 1. 홈 페이지 로드
    home_page.load()
    assert home_page.is_loaded(), "홈페이지 로드 실패"
    
    # 2. '혼자 먹기' 버튼 클릭
    try:
        home_page.click_solo_button()
        print("'혼자 먹기' 버튼 클릭 성공")
        
        # 3. 페이지 이동 확인
        WebDriverWait(Driver, 10).until(
            EC.url_to_be("https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone")
        )
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone", \
            "URL이 올바르지 않습니다."
        print("혼자 먹기 페이지로 이동 성공!")
    except Exception as e:
        print(f"'혼자 먹기' 버튼 클릭 혹은 페이지 이동 실패!: {e}")
        assert False, f"테스트 실패: {e}"
