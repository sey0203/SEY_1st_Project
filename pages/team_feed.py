import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = ws(driver, 10)

    def wait_for_element(self, by, selector):
        # """요소가 로드될 때까지 대기"""
        return self.wait.until(EC.presence_of_all_elements_located((by, selector)))

    def wait_for_url(self, keyword):
        # """URL이 특정 키워드를 포함할 때까지 대기"""
        return self.wait.until(EC.url_contains(keyword))


class TeamFeedPage(BasePage):
    URL = "https://kdt-pt-1-pj-2-team03.elicecoding.com/teams/1"
    GNB_SELECTOR = "div.fixed.bottom-0.w-full.z-50.max-w-\\[600px\\].border-t-\\[1px\\].bg-white.border-gray-200.p-3.h-16"
    TEAM_FEED_SELECTOR = "a[href='/teams/1']"
    COMBOBOX_SELECTOR = "button[role='combobox']"
    TEAM_STATS_IMAGE_SELECTOR = "span.font-bold.text-sub-2.text-title"
    FOOD_PREFERENCE_IMAGE_XPATH = "//span[text()='음식 성향']"
    PROFILE_EDIT_SELECTOR = "svg.cursor-pointer"

   
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = ws(driver, 10)

    def team_feed_click(self):
        # """팀 피드 페이지 클릭 후 URL 변경까지 자동 대기"""
        self.wait_for_element(By.CSS_SELECTOR, self.GNB_SELECTOR)
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.TEAM_FEED_SELECTOR)))
        self.driver.find_element(By.CSS_SELECTOR, self.TEAM_FEED_SELECTOR).click()
        self.wait_for_url("teams")

    def element_click(self, locator_type, locator):
        element = self.driver.find_element(locator_type, locator)
        element.click()

    def combobox_btn_click(self):
        self.element_click(By.CSS_SELECTOR, self.COMBOBOX_SELECTOR)

    def profile_edit_click(self):
        self.element_click(By.CLASS_NAME, self.PROFILE_EDIT_SELECTOR)