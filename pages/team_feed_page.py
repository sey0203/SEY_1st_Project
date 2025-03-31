import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from pages.team_feed_page_locators import TeamFeedPageLocators



class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = ws(driver, 10)

    def wait_for_element(self, by, selector):
        # 요소가 로드될 때까지 대기
        return self.wait.until(EC.presence_of_all_elements_located((by, selector)))

    def wait_for_url(self, keyword):
        # URL이 특정 키워드를 포함할 때까지 대기
        return self.wait.until(EC.url_contains(keyword))


class TeamFeedPage(BasePage):
    URL = "https://kdt-pt-1-pj-2-team03.elicecoding.com/teams/1"


    def team_feed_click(self):
        #팀 피드 페이지 클릭 후 URL 변경까지 자동 대기
        self.wait_for_element(By.CSS_SELECTOR, TeamFeedPageLocators.GNB_SELECTOR)
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_FEED_SELECTOR)))
        self.driver.find_element(By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_FEED_SELECTOR).click()
        self.wait_for_url("teams")

    def combobox_team1_select(self):
        #개발1팀 선택 후 URL 변경까지 자동 대기
        wait = ws(self.driver, 10)
        team1_option = wait.until(EC.element_to_be_clickable((By.XPATH, TeamFeedPageLocators.COMBOBOX_TEAM1_XPATH)))
        ActionChains(self.driver).move_to_element(team1_option).click().perform()
        self.wait_for_url("teams/1")

    def combobox_team2_select(self):
        #개발2팀 선택 후 URL 변경까지 자동 대기
        wait = ws(self.driver, 10)
        team2_option = wait.until(EC.element_to_be_clickable((By.XPATH, TeamFeedPageLocators.COMBOBOX_TEAM2_XPATH)))
        ActionChains(self.driver).move_to_element(team2_option).click().perform()
        self.wait_for_url("teams/2")

    def combobox_team3_select(self):
        #디자인1팀 선택 후 URL 변경까지 자동 대기
        wait = ws(self.driver, 10)
        team3_option = wait.until(EC.element_to_be_clickable((By.XPATH, TeamFeedPageLocators.COMBOBOX_TEAM3_XPATH)))
        ActionChains(self.driver).move_to_element(team3_option).click().perform()
        self.wait_for_url("teams/3")

    def combobox_team4_select(self):
        #디자인2팀 선택 후 URL 변경까지 자동 대기
        wait = ws(self.driver, 10)
        team4_option = wait.until(EC.element_to_be_clickable((By.XPATH, TeamFeedPageLocators.COMBOBOX_TEAM4_XPATH)))
        ActionChains(self.driver).move_to_element(team4_option).click().perform()
        self.wait_for_url("teams/4")

    # 클릭 함수
    def element_click(self, locator_type, locator):
        wait = ws(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        element.click()

    #드롭다운 클릭
    def combobox_btn_click(self):
        self.element_click(By.CSS_SELECTOR, TeamFeedPageLocators.COMBOBOX_SELECTOR)

    #프로필 수정 버튼 클릭
    def profile_edit_icon_click(self):
        self.element_click(By.CSS_SELECTOR, TeamFeedPageLocators.PROFILE_EDIT_ICON_SELECTOR)

    #프로필 수정 완료 버튼 클릭
    def profile_edit_finish_btn_click(self):
        self.element_click(By.CSS_SELECTOR, TeamFeedPageLocators.PROFILE_EDIT_FINISH_BTN_SELECTOR)

    #프로필 수정 화면 x 버튼 클릭
    def profile_edit_X_btn_click(self):       
        wait = ws(self.driver, 10)
        x_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, TeamFeedPageLocators.PROFILE_EDIT_X_BTN_SELECTOR)))
        self.driver.execute_script("arguments[0].click();", x_button)

    #새로운 후기 등록 버튼 클릭
    def add_review_btn_click(self):       
        wait = ws(self.driver, 10)
        add_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_EATEN_MENU_ADD_BTN_SELECTOR)))
        self.driver.execute_script("arguments[0].click();", add_button)

    #새로운 후기 등록 완료 버튼 클릭
    def new_review_finish_btn_click(self):
        wait = ws(self.driver, 10)
        finish_button = wait.until(EC.element_to_be_clickable((By.XPATH, TeamFeedPageLocators.NEW_REVIEW_FINISH_BTN_XPATH)))
        self.driver.execute_script("arguments[0].click();", finish_button)

    #같은 메뉴 먹기 버튼 클릭
    def eat_same_menu_btn_click(self):
        wait = ws(self.driver, 10)
        eat_same_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, TeamFeedPageLocators.EAT_SAME_MENU_BTN_XPATH)))
        self.driver.execute_script("arguments[0].click();", eat_same_menu_button)

    # 스크롤 함수
    def element_scroll(self, locator_type, locator):
        wait = ws(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # 팀 통계까지 스크롤 함수
    def team_stats_scroll(self):
        self.element_scroll(By.XPATH, TeamFeedPageLocators.TEAM_STATS_XPATH)

    # 팀이 먹은 메뉴 목록까지 스크롤 함수
    def team_eaten_menu_scroll(self):
        self.element_scroll(By.XPATH, TeamFeedPageLocators.TEAM_EATEN_MENU_XPATH)

    def navigate_to_profile_edit(self, driver):
        #팀 피드에서 프로필 편집 화면으로 이동하는 공통 함수, 대기까지
        team_feed_page = TeamFeedPage(driver)
        team_feed_page.team_feed_click()
        team_feed_page.combobox_btn_click()
        team_feed_page.combobox_team1_select()
        team_feed_page.profile_edit_icon_click()
        wait = ws(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.PROFILE_EDIT_XPATH)))

    def navigate_to_team_eaten_menu(self, driver):
        #팀 피드에서 팀이 먹은 메뉴로 이동하는 공통 함수, 대기까지
        team_feed_page = TeamFeedPage(driver)
        team_feed_page.team_feed_click()          
        team_feed_page.combobox_btn_click()
        team_feed_page.combobox_team1_select()
        team_feed_page.team_eaten_menu_scroll()
        wait = ws(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_EATEN_MENU_XPATH)))

    def navigate_to_add_review(self, driver):
        #팀 피드에서 새로운 후기 등록하기로 이동하는 공통 함수, 대기까지
        team_feed_page = TeamFeedPage(driver)
        team_feed_page.navigate_to_team_eaten_menu(driver)
        team_feed_page.add_review_btn_click()
        wait = ws(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.ADD_REVIEW_TITLE_XPATH)))


    def change_slider_value(self, driver, slider, change):
        """
        슬라이더 값 1.0씩 증가,감소하는 함수
        :param driver: WebDriver 인스턴스
        :param slider: 슬라이더 요소
        :param change: 변경할 값
        """
        try:
            # 오버레이 숨기기
            overlay = driver.find_element(By.XPATH, "//span[contains(@class, 'text-title')]")
            driver.execute_script("arguments[0].style.display='none';", overlay)

            # 슬라이더가 화면에 보이도록 스크롤
            driver.execute_script("arguments[0].scrollIntoView(true);", slider)

            # JavaScript로 슬라이더 값 변경
            driver.execute_script("""
                var slider = arguments[0];
                var currentValue = parseFloat(slider.getAttribute('aria-valuenow'));
                var newValue = currentValue + arguments[1];
                slider.setAttribute('aria-valuenow', newValue);
            """, slider, change)

        except Exception as e:
            print(f"❌ 슬라이더 값 조정 실패: {e}")


    def update_slider_value(self, driver, slider, change):
        """
        슬라이더 값을 1.0 미만/이상으로 조정하는 함수
        
        :param driver: WebDriver 인스턴스
        :param slider: 슬라이더 요소
        :param change: 변경할 값
        """
        try:
            # 오버레이 숨기기
            overlay = driver.find_element(By.XPATH, "//span[contains(@class, 'text-title')]")
            driver.execute_script("arguments[0].style.display='none';", overlay)

            # 슬라이더가 화면에 보이도록 스크롤
            driver.execute_script("arguments[0].scrollIntoView(true);", slider)

            # JavaScript로 슬라이더 값 변경
            driver.execute_script("""
                var slider = arguments[0];
                var currentValue = parseFloat(slider.getAttribute('aria-valuenow'));
                var newValue = Math.max(0, Math.min(currentValue + arguments[1], 5.0));  // 값 범위: 0~5
                slider.setAttribute('aria-valuenow', newValue);
            """, slider, change)

        except Exception as e:
            print(f"❌ 슬라이더 값 조정 실패: {e}")