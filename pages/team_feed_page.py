import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from pages.team_feed_page_xpath import TeamFeedPageXPaths



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
        self.wait_for_element(By.CSS_SELECTOR, TeamFeedPageXPaths.GNB_SELECTOR)
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, TeamFeedPageXPaths.TEAM_FEED_SELECTOR)))
        self.driver.find_element(By.CSS_SELECTOR, TeamFeedPageXPaths.TEAM_FEED_SELECTOR).click()
        self.wait_for_url("teams")

    def combobox_team_select(self):
        #개발1팀 선택 후 URL 변경까지 자동 대기
        wait = ws(self.driver, 10)
        team_option = wait.until(EC.element_to_be_clickable((By.XPATH, TeamFeedPageXPaths.COMBOBOX_TEAM_XPATH)))
        ActionChains(self.driver).move_to_element(team_option).click().perform()
        self.wait_for_url("teams/1")

    def element_click(self, locator_type, locator):
        wait = ws(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        element.click()

    def combobox_btn_click(self):
        self.element_click(By.CSS_SELECTOR, TeamFeedPageXPaths.COMBOBOX_SELECTOR)

    def profile_edit_icon_click(self):
        self.element_click(By.CSS_SELECTOR, TeamFeedPageXPaths.PROFILE_EDIT_ICON_SELECTOR)

    def profile_edit_finish_btn_click(self):
        self.element_click(By.CSS_SELECTOR, TeamFeedPageXPaths.PROFILE_EDIT_FINISH_BTN_SELECTOR)

    def profile_edit_X_btn_click(self):       
        wait = ws(self.driver, 10)
        x_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, TeamFeedPageXPaths.PROFILE_EDIT_X_BTN_SELECTOR)))
        self.driver.execute_script("arguments[0].click();", x_button)

    def team_eaten_menu_add_btn_click(self):       
        wait = ws(self.driver, 10)
        add_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, TeamFeedPageXPaths.TEAM_EATEN_MENU_ADD_BTN_SELECTOR)))
        self.driver.execute_script("arguments[0].click();", add_button)

    def new_review_finish_btn_click(self):
        wait = ws(self.driver, 10)
        finish_button = wait.until(EC.element_to_be_clickable((By.XPATH, TeamFeedPageXPaths.NEW_REVIEW_FINISH_BTN_XPATH)))
        self.driver.execute_script("arguments[0].click();", finish_button)

    def eat_same_menu_btn_click(self):
        wait = ws(self.driver, 10)
        eat_same_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, TeamFeedPageXPaths.EAT_SAME_MENU_BTN_XPATH)))
        self.driver.execute_script("arguments[0].click();", eat_same_menu_button)

    def element_scroll(self, locator_type, locator):
        wait = ws(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def team_stats_scroll(self):
        self.element_scroll(By.XPATH, TeamFeedPageXPaths.TEAM_STATS_XPATH)

    def team_eaten_menu_scroll(self):
        self.element_scroll(By.XPATH, TeamFeedPageXPaths.TEAM_EATEN_MENU_XPATH)

    def navigate_to_profile_edit(self, driver):
        #팀 피드에서 프로필 편집 화면으로 이동하는 공통 함수, 대기까지
        team_feed_page = TeamFeedPage(driver)
        team_feed_page.team_feed_click()
        team_feed_page.combobox_btn_click()
        team_feed_page.combobox_team_select()
        team_feed_page.profile_edit_icon_click()
        wait = ws(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageXPaths.PROFILE_EDIT_XPATH)))

    def navigate_to_team_eaten_menu(self, driver):
        #팀 피드에서 팀이 먹은 메뉴로 이동하는 공통 함수, 대기까지
        team_feed_page = TeamFeedPage(driver)
        team_feed_page.team_feed_click()          
        team_feed_page.combobox_btn_click()
        team_feed_page.combobox_team_select()
        team_feed_page.team_eaten_menu_scroll()
        wait = ws(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageXPaths.TEAM_EATEN_MENU_XPATH)))

    def navigate_to_add_review(self, driver):
        #팀 피드에서 새로운 후기 등록하기로 이동하는 공통 함수, 대기까지
        team_feed_page = TeamFeedPage(driver)
        team_feed_page.navigate_to_team_eaten_menu(driver)
        team_feed_page.team_eaten_menu_add_btn_click()
        wait = ws(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageXPaths.ADD_REVIEW_TITLE_XPATH)))