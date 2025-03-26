# 필요한 라이브러리 import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest

####### 로그인 된 상태에서 진행이 가능하므로 임의의 로그인 케이스 추가함#######
# 로그인 설정을 위한 Fixture 정의
@pytest.fixture(scope="module")
def login_driver():
    """로그인 설정"""
    service = Service()  # ChromeDriver 설정
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # 로그인 정보
    email = "qa1234@1234.com"
    password = "QA1234@1234.com"
    url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/"

    # 로그인 절차
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//button[text()='로그인하기']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password + Keys.ENTER)
    WebDriverWait(driver, 10).until_not(
        EC.url_contains("signin")  # 로그인 완료 시 URL에 signin이 없어짐
    )
    yield driver
    driver.quit()
    
####### 로그인 된 상태에서 진행이 가능하므로 임의의 로그인 케이스 추가함#######


# Home Page 진입 확인
class HomePage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.base_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/"

    def load_home(self):
        """홈 페이지를 로드"""
        self.driver.get(self.base_url)

    def is_home_loaded(self):
        """홈 페이지가 로드되었는지 확인"""
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.current_url == self.base_url
            )
            print(f"홈 페이지 로드 확인: PASS - URL: {self.driver.current_url}")
            return True
        except Exception as e:
            print(f"홈 페이지 로드 확인 실패: Fail - {e}")
            return False

# 혼자 먹기 (한식) 시도
class SoloKoreanFood:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def eat_solo(self):
        """'혼자 먹기' 버튼 클릭"""
        try:
            eat_solo_css = "button.cursor-pointer"
            solo_button = self.driver.find_element(By.CSS_SELECTOR, eat_solo_css)
            solo_button.click()
            print("'혼자 먹기' 버튼 클릭 : PASS")
        except Exception as e:
            print(f"'혼자 먹기' 버튼 클릭 실패: FAIL - {e}")
            raise

    def is_load_alone_page(self):
        """혼자 먹기 페이지가 로드되었는지 확인"""
        try:
            expected_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone"
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.current_url == expected_url
            )
            print("혼자 먹기 페이지 로드 확인: PASS")
            return True
        except Exception as e:
            print(f"혼자 먹기 페이지 로드 실패 : FAIL - {e}")
            return False
        
    # 드롭다운 메뉴 노출 > 한식 선택하기  
    def select_category(self, category):
        """음식 카테고리를 선택"""
        try:
            # 드롭다운 버튼 클릭
            dropdown_xpath = '//button[@role="combobox"]'
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
            )
            dropdown.click()
            print("드롭다운 메뉴 열기: PASS")

        # 드롭다운 열림 상태 확인
        if not self.is_dropdown_opened():
            raise Exception("드롭다운 메뉴 열림 확인 실패")
        
        # 카테고리 선택
        category_xpath = f'//span[text()="{category}"]/parent::button'
        category_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, category_xpath))
        )
        category_option.click()
        print(f"카테고리 '{category}' 선택: PASS")

    except Exception as e:
        print(f"카테고리 선택 실패: FAIL - {e}")
        raise

    # 드롭다운 메뉴 노출 상태 유지 여부 확인
    def is_menu_opened(self):
        """드롭다운 메뉴가 오픈되어 있는지 확인"""
        try:
            drop_menu_xpath = '//div[@data-radix-popper-content-wrapper]'
            drop_menu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, drop_menu_xpath))
            )
            #요소의 스타일 속성 확인
            style_attribute = drop_menu.get_attribute("style")
            if "transform" in style_attribute and "z-index: 50" in style_attribute:
                print("드롭다운 메뉴 열림 확인: PASS")
                return True
            else:
                print("드롭다운 열림 확인 실패: 스타일 속성 불일치")
                return False
        except Exception as e:
            print(f"드롭다운 메뉴 열림 확인 실패: FAIL - {e}")
            return False

    def click_complete_button(self):
        """선택 완료 버튼 클릭"""
        complete_button_xpath = '//*[@id="root"]/div[1]/main/section/div/button'
        complete_button = self.driver.find_element(By.XPATH, complete_button_xpath)
        complete_button.click()

# RecommendationPage 클래스 정의
class RecommendationPage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def is_menu_displayed(self):
        """추천 메뉴 태그 확인"""
        try:
            menu_tag_xpath = '//span[contains(text(), "오늘 메뉴는")]'
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, menu_tag_xpath))
            )
            print("추천 메뉴 확인: PASS")
            return True
        except Exception as e:
            print(f"추천 메뉴 확인 실패: FAIL - {e}")
            return False

    def accept_recommendation(self):
        """추천 수락 버튼 클릭"""
        try:
            accept_button_xpath = '//*[@id="root"]/div[1]/main/section/section/button[2]'
            accept_button = self.driver.find_element(By.XPATH, accept_button_xpath)
            accept_button.click()
            print("추천 수락 버튼 클릭: PASS")
        except Exception as e:
            print(f"추천 수락 버튼 클릭 실패: FAIL - {e}")
            raise

# HistoryPage 클래스 정의
class HistoryPage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def go_back(self):
        """뒤로 가기 버튼 클릭"""
        try:
            back_button_xpath = '//*[@id="root"]/div[1]/header/div/svg'
            back_button = self.driver.find_element(By.XPATH, back_button_xpath)
            back_button.click()
            print("뒤로 가기 버튼 클릭: PASS")
        except Exception as e:
            print(f"뒤로 가기 버튼 클릭 실패: FAIL - {e}")
            raise
