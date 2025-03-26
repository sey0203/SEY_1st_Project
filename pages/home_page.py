# 필요한 라이브러리 import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest

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

# HomePage 클래스 정의
class HomePage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.base_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/"
        self.alone_page_url = self.base_url + "selectoptions/alone"

    def load_home(self):
        """홈 페이지를 로드"""
        self.driver.get(self.base_url)

    def load_alone_page(self):
        """혼자 먹기 페이지 로드"""
        self.driver.get(self.alone_page_url)

    def is_home_loaded(self):
        """홈 페이지가 로드되었는지 확인"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[1]/button[1]'))
            )
            return True
        except Exception:
            return False

    def click_solo_button(self):
        """'혼자 먹기' 버튼 클릭"""
        solo_button_xpath = '//button[.//p[contains(text(), "혼자 먹기")]]'
        solo_button = self.driver.find_element(By.XPATH, solo_button_xpath)
        solo_button.click()

    def select_category(self, category):
        """음식 카테고리를 선택"""
        dropdown_xpath = '//button[@role="combobox"]'
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
        )
        dropdown.click()

        # 카테고리 선택 (한식 선택을 안했기 때문에 문제 발생. 한식, 중식, 양식을 번갈아가며 선택할 수 있게 해야할 것 같음)
        category_xpath = f'//button[contains(text(), "{category}")]'
        category_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, category_xpath))
        )
        category_option.click()

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

# 테스트 케이스
@pytest.mark.parametrize("category", ["한식"]) # 중식, 양식은 아직 작성하지 않았으므로 넘기기
def test_food_category(login_driver, category):
    """로그인 후 음식 카테고리 선택 및 추천 과정 검증"""
    home_page = HomePage(login_driver)

    try:
        # 1. 혼자 먹기 페이지 로드
        home_page.load_alone_page()
        print("혼자 먹기 페이지 로드: PASS")
    except Exception as e:
        print(f"혼자 먹기 페이지 로드 실패: FAIL - {e}")
        raise

    try:
        # 2. 음식 카테고리 선택
        home_page.select_category(category)
        print(f"음식 카테고리 '{category}' 선택: PASS")
    except Exception as e:
        print(f"음식 카테고리 '{category}' 선택 실패: FAIL - {e}")
        raise

    try:
        # 3. 선택 완료 버튼 클릭
        home_page.click_complete_button()
        print("선택 완료 버튼 클릭: PASS")
    except Exception as e:
        print(f"선택 완료 버튼 클릭 실패: FAIL - {e}")
        raise

    try:
        # 4. 추천 페이지 확인
        recommendation_page = RecommendationPage(login_driver)
        if recommendation_page.is_menu_displayed():
            print("추천 페이지 확인: PASS")
        else:
            print("추천 페이지 확인 실패: FAIL")
            raise AssertionError("추천 메뉴 표시 확인 실패")
    except Exception as e:
        print(f"추천 페이지 확인 중 오류 발생: FAIL - {e}")
        raise

    try:
        # 5. 추천 수락
        recommendation_page.accept_recommendation()
        print("추천 수락 버튼 클릭: PASS")
    except Exception as e:
        print(f"추천 수락 버튼 클릭 실패: FAIL - {e}")
        raise

    try:
        # 6. 추천 히스토리 페이지 확인
        history_page = HistoryPage(login_driver)
        history_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/history"
        assert login_driver.current_url == history_url, "추천 히스토리 페이지로 이동 실패"
        print("추천 히스토리 페이지 확인: PASS")
    except AssertionError as e:
        print(f"추천 히스토리 페이지 확인 실패: FAIL - {e}")
        raise

    try:
        # 7. 뒤로 가기 버튼 클릭하여 다시 혼자 먹기 페이지로 이동
        history_page.go_back()
        assert login_driver.current_url == home_page.alone_page_url, "혼자 먹기 페이지로 복귀 실패"
        print("혼자 먹기 페이지 복귀 확인: PASS")
    except AssertionError as e:
        print(f"혼자 먹기 페이지 복귀 실패: FAIL - {e}")
        raise
