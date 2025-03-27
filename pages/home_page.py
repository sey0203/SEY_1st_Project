# 1. selenium 구동 시 필요한 driver import하기
# import os (쓸 수도 있으니 일단 놔두고 주석 처리)
# import time (얘도 마찬가지)
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# 2. 테스트를 위한 로그인 단 만들기 (사실 여기는 스킾될거임)
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

# 3. 홈 탭으로 이동하기 (이전 과정이 로그인이라 아마 기본적으로 홈 탭으로 이동될 것으로 예상)
class HomePage:
    def __init__ (self, driver):
        self.driver = driver
        # 홈 탭 관련 속성
        self.home_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/" 
        # 혼자 먹기 관련 속성
        self.alone_button_xpath = "/html/body/div[1]/div[1]/main/section/div/div[1]/button[1]"
        self.alone_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone"
        # 같이 먹기 관련 속성
        self.together_button_xpath = "같이 먹기 Xpath 붙여넣기"
        self.together_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/together"
        # 팀 회식 관련 속성
        self.team_button_xpath = "팀 회식 Xpath 붙여넣기"
        self.team_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"
        # 추천 메뉴 페이지 관련 속성
        self.recommendation_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/recommendation"
        # 음식 메뉴 Xpath
        self.menu_xpath = {"한식" : '/html/body/div[3]/div/div/div/div[2]',
                           "중식" : '/html/body/div[3]/div/div/div/div[3]', 
                           "양식" : '/html/body/div[3]/div/div/div/div[4]',
                           "일식" : '/html/body/div[3]/div/div/div/div[5]',
                           "분식" : '/html/body/div[3]/div/div/div/div[6]',
                           "아시안" : '/html/body/div[3]/div/div/div/div[7]',
                           "패스트푸드" : '/html/body/div[3]/div/div/div/div[8]',
                           "기타" : '/html/body/div[3]/div/div/div/div[9]'}
        
####### 이 부분이 에러가 나면 통째로 날리거나 수정 필요함 #######
    def click_menu_category(self, category_xpath):
        """드롭다운 리스트에서 메뉴 선택하는 과정이 반복되어 만듦"""
        try:
            category = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, category_xpath))
            )
            category.click()
            print(f"'{category_xpath}' 카테고리 선택 : PASS")
        except NoSuchElementException as e:
            print(f"해당 카테고리를 찾을 수 없습니다 : {e}")
        except ElementNotInteractableException as e:
            print(f"선택한 카테고리 클릭 실패 : {e}")
            
####### 이 부분이 에러가 나면 통째로 날리거나 수정 필요함 #######

    def go_to_home(self):
        """홈 탭을 눌러 이동"""
        self.driver.get(self.home_url)

    def verify_home_page(self):
        """이동한 페이지의 url이 위의 주소와 동일한지 확인"""
        current_url = self.driver.current_url
        try:
            assert current_url == self.home_url
            print("홈 탭에 정상적으로 이동했습니다.")
        except AssertionError:
            print(f"홈 탭 이동 실패! 현재 URL: {current_url}")

####### 혼자 먹기 테스트 시작 #######

# 4. 혼자 먹기 클릭 하기
    def click_eat_alone_button(self):
        """혼자 먹기 버튼 클릭"""
        try:
            alone_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.alone_button_xpath))
            )
            alone_button.click()
            print("혼자 먹기 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            print(f"혼자 먹기 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            print(f"혼자 먹기 버튼 클릭 실패: {e}")

    def verify_eat_alone_page(self):
        """혼자 먹기 페이지 URL 확인"""
        current_url = self.driver.current_url
        try:
            assert current_url == self.alone_url
            print("혼자 먹기 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            print(f"혼자 먹기 페이지 이동 실패! 현재 URL: {current_url}")

# 5. 펼침 메뉴 > 한식 / 중식 / 양식 선택하기 (3 ~ 8 과정 반복 수행)
    def click_category(self):
        """메뉴 드롭다운 리스트 펼치기"""
        try:
            menu_category = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[1]/button')
            menu_category.click()
            print("드롭다운 메뉴 열기: PASS")
        except NoSuchElementException as e:
            print(f"드롭다운 메뉴를 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            print(f"메뉴 선택 드롭다운 리스트 펼치기 실패: {e}")

    def select_category(self, category_name):
        """카테고리 선택하기"""
        try:
            category_xpath = self.menu_xpath[category_name]
            category = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, category_xpath))
            )
            category.click()
            print(f"{category_name} 선택 : PASS")
        except ElementNotInteractableException as e:
            print(f"드롭다운 리스트에서 {category_name} 선택 실패!: {e}")

# 6. 선택 완료 버튼을 눌러 메뉴 추천 받기
    def click_complete_btn(self):
        """선택 완료 버튼을 눌러 한식 메뉴 추천 받기"""
        try:
            complete_btn_xpath = '/html/body/div[1]/div[1]/main/section/div/button'
            complete_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, complete_btn_xpath))
            )
            complete_btn.click()
            print("선택 완료 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            print(f"선택 완료 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            print(f"선택 완료 버튼 클릭 실패 : {e}")

# 7. 메뉴 추천 받은 후, 추천 수락하기
    def show_recommend(self):
        """추천 메뉴 확인"""
        current_url = self.driver.current_url
        try:
            assert current_url == self.recommendation_url
            print("추천 메뉴 확인 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            print(f"추천 메뉴 확인 페이지 이동 실패! 현재 URL: {current_url}")

    def accept_recommend(self):
        """추천 수락 버튼 클릭하기"""
        try:
            accept_btn_xpath = '/html/body/div[1]/div[1]/main/section/section/button[2]'
            accept_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, accept_btn_xpath))
            )
            accept_btn.click()
            print("추천 수락 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            print(f"추천 수락 버튼을 찾을 수 없음 : {e}")
        except ElementNotInteractableException as e:
            print(f"추천 수락 버튼 클릭 실패 : {e}")

# 8. 다시 홈 탭으로 돌아가기 
    def return_home(self):
        """추천 수락 후, 다음 테스트를 위해 홈 탭으로 이동"""
        self.go_to_home()
        self.verify_home_page()
        
# 위의 과정을 사용하여 한식 테스트 수행
    def test_korean_food(self):
        self.go_to_home()
        self.verify_home_page()
        self.click_eat_alone_button()
        self.verify_eat_alone_page()
        self.click_category()
        self.select_category("한식")
        self.click_complete_btn()
        self.show_recommend()
        self.accept_recommend()
        self.return_home()

# 위의 과정을 사용하여 중식 테스트 수행
    def test_chinese_food(self):
        self.go_to_home()
        self.verify_home_page()
        self.click_eat_alone_button()
        self.verify_eat_alone_page()
        self.click_category()
        self.select_category("중식")
        self.click_complete_btn()
        self.show_recommend()
        self.accept_recommend()
        self.return_home()

 # 위의 과정을 사용하여 양식 테스트 수행
    def test_western_food(self):
        self.go_to_home()
        self.verify_home_page()
        self.click_eat_alone_button()
        self.verify_eat_alone_page()
        self.click_category()
        self.select_category("양식")
        self.click_complete_btn()
        self.show_recommend()
        self.accept_recommend()
        self.return_home()

####### 혼자 먹기 테스트 완료 #######

####### 같이 먹기 테스트 시작 #######

# 9. 같이 먹기 클릭하기
    def click_eat_together_button(self):
        """같이 먹기 버튼 클릭"""
        try:
            together_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.together_button_xpath))
            )
            together_button.click()
            print("같이 먹기 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            print(f"같이 먹기 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            print(f"같이 먹기 버튼 클릭 실패: {e}")

    def verify_eat_together_page(self):
        """같이 먹기 페이지 URL 확인"""
        current_url = self.driver.current_url
        try:
            assert current_url == self.together_url
            print("같이 먹기 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            print(f"같이 먹기 페이지 이동 실패! 현재 URL: {current_url}")

# 10. 펼침 메뉴 > 일식 / 분식 / 아시안 선택하기 (9 ~ 14 과정 반복 수행)
    def click_category_together(self):
        self.click_category()
    def select_category_together(self, category_name):
        self.select_category(category_name)

# 11. 먹는 인원 선택하기 (첫번째 멤버 선택, 강호동은 검색해야할 듯...)
    def choice_member_one(self):
        """첫번째 멤버 선택하기"""
        try:
            member_one = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[2]/div[4]/div[1]/input'))
            )
            member_one.click()
            print("첫번째 멤버가 선택되었습니다.")
        except NoSuchElementException as e:
            print(f"해당 멤버를 찾지 못했습니다. : {e}")
        except ElementNotInteractableException as e:
            print(f"해당 멤버를 선택하지 못했습니다. : {e}")

    def choice_member_two(self):
        """강호동 검색해서 선택하기"""
        try:
            member_two = self.driver.find_element(By.CLASS_NAME, "placeholder") 
            member_two.send_keys("강호동")
            member_two.send_keys(Keys.RETURN)
            click_member_two = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[2]/div[3]/ul/li/div'))
            )
            click_member_two.click()
            print("멤버가 선택되었습니다.")
        except NoSuchElementException as e:
            print(f"해당 멤버를 찾지 못했습니다. : {e}")
        except ElementNotInteractableException as e:
            print(f"해당 멤버를 선택하지 못했습니다. : {e}")

# 12. 선택 완료 버튼을 눌러 메뉴 추천 받기
    def click_complete_btn_together(self):
        self.click_complete_btn()

# 13. 메뉴 추천 받은 후, 추천 수락하기
    def show_recommend_together(self):
        self.show_recommend()
    def accept_recommend_together(self):
        self.accept_recommend()

# 14. 다시 홈 탭으로 돌아가기
        self.return_home()

# 위의 과정을 사용하여 일식 테스트 수행
    def test_japanese_food(self):
        self.verify_home_page()
        self.click_eat_together_button()
        self.verify_eat_together_page()
        self.click_category_together()
        self.select_category_together("일식")
        self.choice_member_one()
        self.choice_member_two()
        self.click_complete_btn_together()
        self.show_recommend_together()
        self.accept_recommend_together()
        self.return_home()

# 위의 과정을 사용하여 분식 테스트 수행
    def test_street_food(self):
        self.verify_home_page()
        self.click_eat_together_button()
        self.verify_eat_together_page()
        self.click_category_together()
        self.select_category_together("분식")
        self.choice_member_one()
        self.choice_member_two()
        self.click_complete_btn_together()
        self.show_recommend_together()
        self.accept_recommend_together()
        self.return_home()
 # 위의 과정을 사용하여 아시안 테스트 수행
    def test_asian_food(self):
        self.verify_home_page()
        self.click_eat_together_button()
        self.verify_eat_together_page()
        self.click_category_together()
        self.select_category_together("아시안")
        self.choice_member_one()
        self.choice_member_two()
        self.click_complete_btn_together()
        self.show_recommend_together()
        self.accept_recommend_together()
        self.return_home()

####### 같이 먹기 테스트 완료 #######

####### 회식하기 테스트 시작 #######

# 15. 회식하기 클릭하기
    def click_eat_team_button(self):
        """회식하기 버튼 클릭"""
        try:
            team_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.team_button_xpath))
            )
            team_button.click()
            print("회식하기 버튼 클릭 : PASS")
        except NoSuchElementException as e:
            print(f"회식하기 버튼을 찾을 수 없음: {e}")
        except ElementNotInteractableException as e:
            print(f"회식하기 버튼 클릭 실패: {e}")

    def verify_eat_team_page(self):
        """회식하기 페이지 URL 확인"""
        current_url = self.driver.current_url
        try:
            assert current_url == self.team_url
            print("회식하기 페이지에 정상적으로 이동했습니다.")
        except AssertionError:
            print(f"회식하기 페이지 이동 실패! 현재 URL: {current_url}")

# 16. 펼침 메뉴 > 패스트 푸드 / 기타 선택하기 (15 ~ 20 과정 반복 수행)
    def click_category_team(self):
        self.click_category()
    def select_category_team(self, category_name):
        self.select_category(category_name)

# 17. 먹는 인원 확인하기 (개발 1팀 여부 확인)
    def join_team(self):
        try:
            team_name = self.driver.find_element(By.XPATH, "//span[@class='text-white']")
            assert "개발 1팀" in team_name.text
            print("'개발 1팀'이 정상적으로 선택되어 있습니다.")
        except NoSuchElementException as e: 
            print(f"'개발 1팀'을 찾을 수 없습니다. : {e}") 

# 18. 선택 완료 버튼을 눌러 메뉴 추천 받기
    def click_complete_btn_team(self):
        self.click_complete_btn()

# 19. 메뉴 추천 받은 후, 추천 수락하기
    def show_recommend_team(self):
        self.show_recommend()
    def accept_recommend_team(self):
        self.accept_recommend()

# 20. 다시 홈 탭으로 돌아가기 
        self.return_home()

# 위의 과정을 사용하여 패스트 푸드 테스트 수행
    def test_fast_food(self):
        self.go_to_home()
        self.verify_home_page()
        self.click_eat_team_button()
        self.verify_eat_team_page()
        self.click_category()
        self.select_category("패스트푸드")
        self.click_complete_btn()
        self.show_recommend()
        self.accept_recommend()
        self.return_home()

# 위의 과정을 사용하여 기타 테스트 수행
    def test_other_food(self):
        self.go_to_home()
        self.verify_home_page()
        self.click_eat_team_button()
        self.verify_eat_team_page()
        self.click_category()
        self.select_category("기타")
        self.click_complete_btn()
        self.show_recommend()
        self.accept_recommend()
        self.return_home()

####### 회식하기 테스트 완료 #######

# 21. 직원들이 선호하는 음식 종류 확인하기 (마우스 온 시 내용 노출 확인)



# 22. 메뉴 추천 확인하기 


