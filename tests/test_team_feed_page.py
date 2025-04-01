import time
import pytest
import sys
import os
from utils.image_is_similar import is_similar
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from pages.team_feed_page import TeamFeedPage
from selenium.webdriver.common.action_chains import ActionChains
from pages.team_feed_page_locators import TeamFeedPageLocators
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("login_driver")
class TestTeamFeedPage:
    
    #@pytest.mark.skip()
    def test_teamfeed_001(self, driver: WebDriver):
        try:
            wait = ws(driver, 10)
            home_gnb = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.GNB_SELECTOR)))
            
            assert home_gnb.is_displayed(), "❌ 홈 GNB 찾지못함"
            print("✅ 홈 GNB 노출")
            
            team_feed_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_FEED_ICON_SELECTOR)))
            
            assert team_feed_icon.is_displayed(), "❌ 팀 피드 아이콘 노출 안됨"
            print("✅ 팀 피드 아이콘 표시")
            driver.save_screenshot("✅ 팀 피드 아이콘-성공.png")
        
        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드 아이콘-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드 아이콘-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드 아이콘-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_002(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()

            assert "teams" in driver.current_url, f"❌ 현재 url: {driver.current_url}"
            print("✅ 팀 피드 페이지 오픈 성공")
            driver.save_screenshot("✅ 팀 피드 페이지-오픈-성공.png")
        
        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드 페이지-오픈-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드 페이지-오픈-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드 페이지-오픈-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_003(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()

            wait = ws(driver, 10)
            title = wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FEED_TITLE_XPATH)))

            assert title.is_displayed(), f"❌ 팀 피드 title 노출 안됨, 실제: {title.text}"
            print("✅ 팀 피드 title 노출 성공")
            driver.save_screenshot("✅ 팀 피드 title 노출-성공.png")
        
        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드 title 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드 title 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드 title 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_004(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          
            team_feed_page.combobox_btn_click()

            # "개발 1팀" 선택           
            wait = ws(driver, 10)
            team_option = wait.until(EC.element_to_be_clickable((By.XPATH, TeamFeedPageLocators.COMBOBOX_TEAM1_XPATH)))
            ActionChains(driver).move_to_element(team_option).click().perform()

            assert "teams/1" in driver.current_url, f"❌ 개발 1팀 선택 실패, 현재 url: {driver.current_url}"
            print(f"✅ 개발 1팀 선택 성공")
            driver.save_screenshot(f"✅ 팀 피드-콤보박스-개발 1팀-선택-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-콤보박스-개발1팀 선택-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-콤보박스-개발1팀 선택-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-콤보박스-개발1팀 선택-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_005(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team1_select()

            wait = ws(driver, 10)
            food_tendency = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            assert food_tendency.is_displayed(), f"❌ 개발1팀-음식 성향 노출 안됨, 실제: {food_tendency.text}"
            print("✅ 개발1팀-음식 성향 노출 성공")
            driver.save_screenshot("✅ 팀 피드-개발1팀-음식 성향 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-개발1팀-음식 성향 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-개발1팀-음식 성향 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-개발1팀-음식 성향 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_006(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team1_select()

            team_feed_page.team_stats_scroll()
            team_stats = driver.find_element(By.XPATH, TeamFeedPageLocators.TEAM_STATS_XPATH)

            assert team_stats.is_displayed(), f"❌ 개발1팀-팀 통계 노출 안됨, 실제: {team_stats.text}"
            time.sleep(1)            
            print("✅ 개발1팀-팀 통계 노출 성공")
            driver.save_screenshot("✅ 개발1팀-팀 통계 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-개발1팀-팀 통계 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-개발1팀-팀 통계 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-개발1팀-팀 통계 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_007(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team1_select()

            team_feed_page.team_eaten_menu_scroll()
            team_eaten_menu = driver.find_element(By.XPATH, TeamFeedPageLocators.TEAM_EATEN_MENU_XPATH)

            assert team_eaten_menu.is_displayed(), f"❌ 개발1팀-팀이 먹은 메뉴 노출 안됨, 실제: {team_eaten_menu.text}"
            time.sleep(1)
            print("✅ 개발1팀-팀이 먹은 메뉴 노출 성공")
            driver.save_screenshot("✅ 개발1팀-팀이 먹은 메뉴 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-개발1팀-팀이 먹은 메뉴 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-개발1팀-팀이 먹은 메뉴 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-개발1팀-팀이 먹은 메뉴-실패 (알 수 없는 오류) : {e}"

    #@pytest.mark.skip()
    def test_teamfeed_008(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          
            team_feed_page.combobox_btn_click()

            # "개발 2팀" 선택           
            wait = ws(driver, 10)
            team_option = wait.until(EC.element_to_be_clickable((By.XPATH, TeamFeedPageLocators.COMBOBOX_TEAM2_XPATH)))
            ActionChains(driver).move_to_element(team_option).click().perform()

            assert "teams/2" in driver.current_url, f"❌ 개발 2팀 선택 실패, 현재 url: {driver.current_url}"
            print(f"✅ 개발 2팀 선택 성공")
            driver.save_screenshot(f"✅ 팀 피드-콤보박스-개발 2팀-선택-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-콤보박스-개발2팀 선택-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-콤보박스-개발2팀 선택-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-콤보박스-개발2팀 선택-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_009(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team2_select()

            wait = ws(driver, 10)
            food_tendency = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            assert food_tendency.is_displayed(), f"❌ 개발2팀-음식 성향 노출 안됨, 실제: {food_tendency.text}"
            print("✅ 개발2팀-음식 성향 노출 성공")
            driver.save_screenshot("✅ 팀 피드-개발2팀-음식 성향 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-개발2팀-음식 성향 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-개발2팀-음식 성향 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-개발2팀-음식 성향 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_010(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team2_select()

            team_feed_page.team_stats_scroll()
            team_stats = driver.find_element(By.XPATH, TeamFeedPageLocators.TEAM_STATS_XPATH)

            assert team_stats.is_displayed(), f"❌ 개발2팀-팀 통계 노출 안됨, 실제: {team_stats.text}"
            print("✅ 개발2팀-팀 통계 노출 성공")
            time.sleep(1)
            driver.save_screenshot("✅ 개발2팀-팀 통계 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-개발2팀-팀 통계 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-개발2팀-팀 통계 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-개발2팀-팀 통계 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_011(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team2_select()

            team_feed_page.team_eaten_menu_scroll()
            team_eaten_menu = driver.find_element(By.XPATH, TeamFeedPageLocators.TEAM_EATEN_MENU_XPATH)

            assert team_eaten_menu.is_displayed(), f"❌ 개발2팀-팀이 먹은 메뉴 노출 안됨, 실제: {team_eaten_menu.text}"
            print("✅ 개발2팀-팀이 먹은 메뉴 노출 성공")
            time.sleep(1)            
            driver.save_screenshot("✅ 개발2팀-팀이 먹은 메뉴 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-개발2팀-팀이 먹은 메뉴 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-개발2팀-팀이 먹은 메뉴 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-개발2팀-팀이 먹은 메뉴-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_012(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          
            team_feed_page.combobox_btn_click()

            # "디자인 1팀" 선택           
            wait = ws(driver, 10)
            team_option = wait.until(EC.element_to_be_clickable((By.XPATH, TeamFeedPageLocators.COMBOBOX_TEAM3_XPATH)))
            ActionChains(driver).move_to_element(team_option).click().perform()

            assert "teams/3" in driver.current_url, f"❌ 디자인1팀 선택 실패, 현재 url: {driver.current_url}"
            print(f"✅ 디자인1팀 선택 성공")
            driver.save_screenshot(f"✅ 팀 피드-콤보박스-디자인1팀-선택-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-콤보박스-디자인1팀 선택-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-콤보박스-디자인1팀 선택-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-콤보박스-디자인1팀 선택-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_013(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team3_select()

            wait = ws(driver, 10)
            food_tendency = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            assert food_tendency.is_displayed(), f"❌ 디자인1팀-음식 성향 노출 안됨, 실제: {food_tendency.text}"
            print("✅ 디자인1팀-음식 성향 노출 성공")
            driver.save_screenshot("✅ 팀 피드-디자인1팀-음식 성향 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-디자인1팀-음식 성향 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-디자인1팀-음식 성향 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-디자인1팀-음식 성향 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_014(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team3_select()

            team_feed_page.team_stats_scroll()
            team_stats = driver.find_element(By.XPATH, TeamFeedPageLocators.TEAM_STATS_XPATH)

            assert team_stats.is_displayed(), f"❌ 디자인1팀-팀 통계 노출 안됨, 실제: {team_stats.text}"
            print("✅ 디자인1팀-팀 통계 노출 성공")
            time.sleep(1)
            driver.save_screenshot("✅ 디자인1팀-팀 통계 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-디자인1팀-팀 통계 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-디자인1팀-팀 통계 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-디자인1팀-팀 통계 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_015(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team3_select()

            team_feed_page.team_eaten_menu_scroll()
            team_eaten_menu = driver.find_element(By.XPATH, TeamFeedPageLocators.TEAM_EATEN_MENU_XPATH)

            assert team_eaten_menu.is_displayed(), f"❌ 디자인1팀-팀이 먹은 메뉴 노출 안됨, 실제: {team_eaten_menu.text}"
            print("✅ 디자인1팀-팀이 먹은 메뉴 노출 성공")
            time.sleep(1)            
            driver.save_screenshot("✅ 디자인1팀-팀이 먹은 메뉴 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-디자인1팀-팀이 먹은 메뉴 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-디자인1팀-팀이 먹은 메뉴 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-디자인1팀-팀이 먹은 메뉴-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_016(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          
            team_feed_page.combobox_btn_click()

            # "디자인 2팀" 선택           
            wait = ws(driver, 10)
            team_option = wait.until(EC.element_to_be_clickable((By.XPATH, TeamFeedPageLocators.COMBOBOX_TEAM4_XPATH)))
            ActionChains(driver).move_to_element(team_option).click().perform()

            assert "teams/4" in driver.current_url, f"❌ 디자인2팀 선택 실패, 현재 url: {driver.current_url}"
            print(f"✅ 디자인2팀 선택 성공")
            driver.save_screenshot(f"✅ 팀 피드-콤보박스-디자인2팀-선택-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-콤보박스-디자인2팀 선택-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-콤보박스-디자인2팀 선택-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-콤보박스-디자인2팀 선택-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_017(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team4_select()

            wait = ws(driver, 10)
            food_tendency = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            assert food_tendency.is_displayed(), f"❌ 디자인2팀-음식 성향 노출 안됨, 실제: {food_tendency.text}"
            print("✅ 디자인2팀-음식 성향 노출 성공")
            driver.save_screenshot("✅ 팀 피드-디자인2팀-음식 성향 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-디자인2팀-음식 성향 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-디자인2팀-음식 성향 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-디자인2팀-음식 성향 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_018(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team4_select()

            team_feed_page.team_stats_scroll()
            team_stats = driver.find_element(By.XPATH, TeamFeedPageLocators.TEAM_STATS_XPATH)

            assert team_stats.is_displayed(), f"❌ 디자인2팀-팀 통계 노출 안됨, 실제: {team_stats.text}"
            print("✅ 디자인2팀-팀 통계 노출 성공")
            time.sleep(1)
            driver.save_screenshot("✅ 디자인2팀-팀 통계 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-디자인2팀-팀 통계 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-디자인2팀-팀 통계 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-디자인2팀-팀 통계 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_019(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team4_select()

            team_feed_page.team_eaten_menu_scroll()
            team_eaten_menu = driver.find_element(By.XPATH, TeamFeedPageLocators.TEAM_EATEN_MENU_XPATH)

            assert team_eaten_menu.is_displayed(), f"❌ 디자인2팀-팀이 먹은 메뉴 노출 안됨, 실제: {team_eaten_menu.text}"
            print("✅ 디자인2팀-팀이 먹은 메뉴 노출 성공")
            time.sleep(1)            
            driver.save_screenshot("✅ 디자인2팀-팀이 먹은 메뉴 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-디자인2팀-팀이 먹은 메뉴 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-디자인2팀-팀이 먹은 메뉴 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-디자인2팀-팀이 먹은 메뉴-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_020(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team1_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_name =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_NAME_SELECTOR)))

            assert team_name.text == "개발 1팀", f"❌ 음식성향-'개발 1팀' 텍스트 불일치, 실제: {team_name.text}"
            print("✅ 음식성향-'개발 1팀' 텍스트 확인 성공")  
            driver.save_screenshot("✅ 음식성향-'개발 1팀' 텍스트-성공.png")                

        except NoSuchElementException as e:
            assert False, f"❌ 음식성향-'개발 1팀' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 음식성향-'개발 1팀' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 음식성향-'개발 1팀' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_021(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team1_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_sweet_flavor =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_SWEET_FLAVOR_TITLE_SELECTOR)))

            assert team_sweet_flavor.text == "단 맛", f"❌ 개발1팀-음식성향-'단 맛' 텍스트 불일치, 실제: {team_sweet_flavor.text}"
            print("✅ 개발1팀-음식성향-'단 맛' 텍스트 확인 성공")  

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-'단 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-'단 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-'단 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_022(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team1_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_salty_flavor =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_SALTY_FLAVOR_TITLE_SELECTOR)))

            assert team_salty_flavor.text == "짠 맛", f"❌ 개발1팀-음식성향-'짠 맛' 텍스트 불일치, 실제: {team_salty_flavor.text}"
            print("✅ 개발1팀-음식성향-'짠 맛' 텍스트 확인 성공")  

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-'짠 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-성향-'짠 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 음식성향-'짠 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_023(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team1_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_spicy_flavor =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_SPICY_FLAVOR_TITLE_SELECTOR)))

            assert team_spicy_flavor.text == "매운 맛", f"❌ 개발1팀-음식성향-'매운 맛' 텍스트 불일치, 실제: {team_spicy_flavor.text}"
            print("✅ 개발1팀-음식성향-'매운 맛' 텍스트 확인 성공")  

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-성향-'매운 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-'매운 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-'매운 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_024(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team1_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_favorite_food =  wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FAVORITE_FOOD_XPATH)))

            assert len(team_favorite_food.text) > 0 , f"❌ 개발1팀-음식성향-좋아하는 음식 텍스트 존재하지 않음"
            print("✅ 개발1팀-음식성향-좋아하는 음식 텍스트 존재")  

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-좋아하는 음식 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-좋아하는 음식 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-좋아하는 음식 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_025(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team1_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_hate_food =  wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_HATE_FOOD_XPATH)))

            assert len(team_hate_food.text) > 0 , f"❌ 개발1팀-음식성향-싫어하는 음식 텍스트 존재하지 않음"
            print("✅ 개발1팀-음식성향-싫어하는 음식 텍스트 존재")  

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-싫어하는 음식 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-싫어하는 음식 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-싫어하는 음식 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_026(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team2_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_name =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_NAME_SELECTOR)))

            assert team_name.text == "개발 2팀", f"❌ 음식성향-'개발 2팀' 텍스트 불일치, 실제: {team_name.text}"
            print("✅ 음식성향-'개발 2팀' 텍스트 확인 성공")  

        except NoSuchElementException as e:
            assert False, f"❌ 음식성향-'개발2팀' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 음식성향-'개발2팀' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 음식성향-'개발2팀' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_027(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team2_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_sweet_flavor =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_SWEET_FLAVOR_TITLE_SELECTOR)))

            assert team_sweet_flavor.text == "단 맛", f"❌ 개발2팀-음식성향-'단 맛' 텍스트 불일치, 실제: {team_sweet_flavor.text}"
            print("✅ 개발2팀-음식성향-'단 맛' 텍스트 확인 성공")  

        except NoSuchElementException as e:
            assert False, f"❌ 개발2팀-음식성향-'단 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발2팀-음식성향-'단 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발2팀-음식성향-'단 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_028(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team2_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_salty_flavor =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_SALTY_FLAVOR_TITLE_SELECTOR)))

            assert team_salty_flavor.text == "짠 맛", f"❌ 개발2팀-음식성향-'짠 맛' 텍스트 불일치, 실제: {team_salty_flavor.text}"
            print("✅ 개발2팀-음식성향-'짠 맛' 텍스트 확인 성공")  

        except NoSuchElementException as e:
            assert False, f"❌ 개발2팀-음식성향-'짠 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발2팀-성향-'짠 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 음식성향-'짠 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_029(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team2_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_spicy_flavor =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_SPICY_FLAVOR_TITLE_SELECTOR)))

            assert team_spicy_flavor.text == "매운 맛", f"❌ 개발2팀-음식성향-'매운 맛' 텍스트 불일치, 실제: {team_spicy_flavor.text}"
            print("✅ 개발2팀-음식성향-'매운 맛' 텍스트 확인 성공")  

        except NoSuchElementException as e:
            assert False, f"❌ 개발2팀-성향-'매운 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발2팀-음식성향-'매운 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발2팀-음식성향-'매운 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_030(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team2_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_favorite_food =  wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FAVORITE_FOOD_XPATH)))

            assert len(team_favorite_food.text) > 0 , f"❌ 개발2팀-음식성향-좋아하는 음식 텍스트 존재하지 않음"
            print("✅ 개발2팀-음식성향-좋아하는 음식 텍스트 존재")  

        except NoSuchElementException as e:
            assert False, f"❌ 개발2팀-음식성향-좋아하는 음식 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발2팀-음식성향-좋아하는 음식 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발2팀-음식성향-좋아하는 음식 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_031(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team2_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_hate_food =  wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_HATE_FOOD_XPATH)))

            assert len(team_hate_food.text) > 0 , f"❌ 개발2팀-음식성향-싫어하는 음식 텍스트 존재하지 않음"
            print("✅ 개발2팀-음식성향-싫어하는 음식 텍스트 존재")  

        except NoSuchElementException as e:
            assert False, f"❌ 개발2팀-음식성향-싫어하는 음식 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발2팀-음식성향-싫어하는 음식 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발2팀-음식성향-싫어하는 음식 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_032(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team3_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_name =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_NAME_SELECTOR)))

            assert team_name.text == "디자인 1팀", f"❌ 음식성향-'디자인 1팀' 텍스트 불일치, 실제: {team_name.text}"
            print("✅ 음식성향-'디자인 1팀' 텍스트 확인 성공")  
            driver.save_screenshot("✅ 음식성향-'디자인 1팀' 텍스트-성공.png")                

        except NoSuchElementException as e:
            assert False, f"❌ 음식성향-'디자인1팀' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 음식성향-'디자인1팀' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 음식성향-'디자인1팀' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_033(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team3_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_sweet_flavor =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_SWEET_FLAVOR_TITLE_SELECTOR)))

            assert team_sweet_flavor.text == "단 맛", f"❌ 디자인1팀-음식성향-'단 맛' 텍스트 불일치, 실제: {team_sweet_flavor.text}"
            print("✅ 디자인1팀-음식성향-'단 맛' 텍스트 확인 성공")  

        except NoSuchElementException as e:
            assert False, f"❌ 디자인1팀-음식성향-'단 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 디자인1팀-음식성향-'단 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 디자인1팀-음식성향-'단 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_034(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team3_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_salty_flavor =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_SALTY_FLAVOR_TITLE_SELECTOR)))

            assert team_salty_flavor.text == "짠 맛", f"❌ 디자인1팀-음식성향-'짠 맛' 텍스트 불일치, 실제: {team_salty_flavor.text}"
            print("✅ 디자인1팀-음식성향-'짠 맛' 텍스트 확인 성공")  

        except NoSuchElementException as e:
            assert False, f"❌ 디자인1팀-음식성향-'짠 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 디자인1팀-성향-'짠 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 음식성향-'짠 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_035(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team3_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_spicy_flavor =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_SPICY_FLAVOR_TITLE_SELECTOR)))

            assert team_spicy_flavor.text == "매운 맛", f"❌ 디자인1팀-음식성향-'매운 맛' 텍스트 불일치, 실제: {team_spicy_flavor.text}"
            print("✅ 디자인1팀-음식성향-'매운 맛' 텍스트 확인 성공")  

        except NoSuchElementException as e:
            assert False, f"❌ 디자인1팀-성향-'매운 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 디자인1팀-음식성향-'매운 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 디자인1팀-음식성향-'매운 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_036(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team3_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_favorite_food =  wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FAVORITE_FOOD_XPATH)))

            assert len(team_favorite_food.text) > 0 , f"❌ 디자인1팀-음식성향-좋아하는 음식 텍스트 존재하지 않음"
            print("✅ 디자인1팀-음식성향-좋아하는 음식 텍스트 존재")  

        except NoSuchElementException as e:
            assert False, f"❌ 디자인1팀-음식성향-좋아하는 음식 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 디자인1팀-음식성향-좋아하는 음식 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 디자인1팀-음식성향-좋아하는 음식 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_037(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team3_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_hate_food =  wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_HATE_FOOD_XPATH)))

            assert len(team_hate_food.text) > 0 , f"❌ 디자인1팀-음식성향-싫어하는 음식 텍스트 존재하지 않음"
            print("✅ 디자인1팀-음식성향-싫어하는 음식 텍스트 존재")  

        except NoSuchElementException as e:
            assert False, f"❌ 디자인1팀-음식성향-싫어하는 음식 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 디자인1팀-음식성향-싫어하는 음식 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 디자인1팀-음식성향-싫어하는 음식 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_038(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team4_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_name =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_NAME_SELECTOR)))

            assert team_name.text == "디자인 2팀", f"❌ 음식성향-'디자인 2팀' 텍스트 불일치, 실제: {team_name.text}"
            print("✅ 음식성향-'디자인 2팀' 텍스트 확인 성공")  
            driver.save_screenshot("✅ 음식성향-'디자인 2팀' 텍스트-성공.png")                

        except NoSuchElementException as e:
            assert False, f"❌ 음식성향-'디자인2팀' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 음식성향-'디자인2팀' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 음식성향-'디자인2팀' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_039(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team4_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_sweet_flavor =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_SWEET_FLAVOR_TITLE_SELECTOR)))

            assert team_sweet_flavor.text == "단 맛", f"❌ 디자인2팀-음식성향-'단 맛' 텍스트 불일치, 실제: {team_sweet_flavor.text}"
            print("✅ 디자인2팀-음식성향-'단 맛' 텍스트 확인 성공")  

        except NoSuchElementException as e:
            assert False, f"❌ 디자인2팀-음식성향-'단 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 디자인2팀-음식성향-'단 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 디자인2팀-음식성향-'단 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_040(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team4_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_salty_flavor =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_SALTY_FLAVOR_TITLE_SELECTOR)))

            assert team_salty_flavor.text == "짠 맛", f"❌ 디자인2팀-음식성향-'짠 맛' 텍스트 불일치, 실제: {team_salty_flavor.text}"
            print("✅ 디자인2팀-음식성향-'짠 맛' 텍스트 확인 성공")  

        except NoSuchElementException as e:
            assert False, f"❌ 디자인2팀-음식성향-'짠 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 디자인2팀-성향-'짠 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 음식성향-'짠 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_041(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team4_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_spicy_flavor =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.TEAM_SPICY_FLAVOR_TITLE_SELECTOR)))

            assert team_spicy_flavor.text == "매운 맛", f"❌ 디자인2팀-음식성향-'매운 맛' 텍스트 불일치, 실제: {team_spicy_flavor.text}"
            print("✅ 디자인2팀-음식성향-'매운 맛' 텍스트 확인 성공")  

        except NoSuchElementException as e:
            assert False, f"❌ 디자인2팀-성향-'매운 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 디자인2팀-음식성향-'매운 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 디자인2팀-음식성향-'매운 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_042(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team4_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_favorite_food =  wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FAVORITE_FOOD_XPATH)))

            assert len(team_favorite_food.text) > 0 , f"❌ 디자인2팀-음식성향-좋아하는 음식 텍스트 존재하지 않음"
            print("✅ 디자인2팀-음식성향-좋아하는 음식 텍스트 존재")  

        except NoSuchElementException as e:
            assert False, f"❌ 디자인2팀-음식성향-좋아하는 음식 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 디자인2팀-음식성향-좋아하는 음식 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 디자인2팀-음식성향-좋아하는 음식 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_043(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team4_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FOOD_TENDENCY_XPATH)))

            team_hate_food =  wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_HATE_FOOD_XPATH)))

            assert len(team_hate_food.text) > 0 , f"❌ 디자인2팀-음식성향-싫어하는 음식 텍스트 존재하지 않음"
            print("✅ 디자인2팀-음식성향-싫어하는 음식 텍스트 존재")  

        except NoSuchElementException as e:
            assert False, f"❌ 디자인2팀-음식성향-싫어하는 음식 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 디자인2팀-음식성향-싫어하는 음식 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 디자인2팀-음식성향-싫어하는 음식 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_044(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team1_select()

            team_feed_page.profile_edit_icon_click()

            wait = ws(driver, 10)
            edit_title = wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.PROFILE_EDIT_XPATH)))

            #너무 빨리 닫혀서 스크린샷이 겹치게 찍혀 타임슬립
            time.sleep(1)
            assert edit_title.is_displayed(), f"❌ 프로필 정보 수정화면 진입 실패"
            print("✅ 프로필 정보 수정화면 진입 성공")  
            driver.save_screenshot("✅ 팀 피드-프로필 정보 수정화면-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-프로필 정보 수정화면-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-프로필 정보 수정화면-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-프로필 정보 수정화면-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_045(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)

            team_feed_page.profile_edit_finish_btn_click()

            wait = ws(driver, 10)
            title = wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FEED_TITLE_XPATH)))

            assert title.is_displayed(), f"❌ 프로필 수정 완료 클릭-팀 피드 화면으로 돌아오기 실패"
            print("✅ 프로필 정보 수정 완료 클릭-팀 피드 화면으로 돌아오기 성공")              
            driver.save_screenshot("✅ 프로필 수정 완료 클릭-팀 피드 화면으로 돌아오기-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 프로필 정보 수정화면-프로필 수정 완료 클릭-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 프로필 정보 수정화면-프로필 수정 완료 클릭-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 프로필 정보 수정화면-프로필 수정 완료 클릭-실패 (알 수 없는 오류) : {e}"
        

    #@pytest.mark.skip()
    def test_teamfeed_046(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)

            team_feed_page.profile_edit_X_btn_click()

            wait = ws(driver, 10)
            title = wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FEED_TITLE_XPATH)))

            time.sleep(1)
            assert title.is_displayed(), f"❌ 'X' 버튼 클릭-팀 피드 화면으로 돌아오기 실패"
            print("✅ 프로필 정보 수정화면 'X' 버튼 클릭-팀 피드 화면으로 돌아오기 성공")              
            driver.save_screenshot("✅ 'X' 버튼 클릭-팀 피드 화면으로 돌아오기-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 프로필 정보 수정화면-'X' 버튼 클릭-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 프로필 정보 수정화면-'X' 버튼 클릭-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 프로필 정보 수정화면-'X' 버튼 클릭-실패 (알 수 없는 오류) : {e}"

    
    #@pytest.mark.skip()
    def test_teamfeed_047(self, driver):
        #실제로 슬라이더를 옮기는건 못해서 자동화 실패...
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)
            wait = ws(driver, 10)
            
            # 슬라이더 요소 찾기 (단 맛 슬라이더)
            slider = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SWEET_FLAVOR_XPATH)))
            
            # 현재 값 가져오기
            initial_value = float(slider.get_attribute("aria-valuenow"))
            
            team_feed_page.change_slider_value(driver, slider, change=-1.0)
            
            # 값 변경 후 다시 가져오기
            new_value = float(slider.get_attribute("aria-valuenow"))
            
            # 소수점 3자리로 반올림
            initial_value_rounded = round(initial_value, 3)
            new_value_rounded = round(new_value, 3)
            
            # 검증: 기존 값에서 1.0 감소했는지 확인
            assert new_value_rounded == round(initial_value - 1.0, 3), f"❌ 단맛 슬라이더 값 변경 실패 (기대값: {round(initial_value - 1.0, 3)}, 실제값: {new_value_rounded})"
            print(f"✅ 단맛 슬라이더 값 감소 성공: {initial_value_rounded} -> {new_value_rounded}")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-단맛 슬라이더 감소-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-단맛 슬라이더 감소-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-단맛 슬라이더 감소-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_048(self, driver):
        #실제로 슬라이더를 옮기는건 못해서 자동화 실패...
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)
            wait = ws(driver, 10)
            
            # 슬라이더 요소 찾기 (단 맛 슬라이더)
            slider = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SWEET_FLAVOR_XPATH)))
            
            # 현재 값 가져오기
            initial_value = float(slider.get_attribute("aria-valuenow"))
            
            team_feed_page.change_slider_value(driver, slider, change=1.0)
            
            # 값 변경 후 다시 가져오기
            new_value = float(slider.get_attribute("aria-valuenow"))
            
            # 소수점 3자리로 반올림
            initial_value_rounded = round(initial_value, 3)
            new_value_rounded = round(new_value, 3)
            
            # 검증: 기존 값에서 1.0 증가했는지 확인
            assert new_value_rounded == round(initial_value + 1.0, 3), f"❌ 단맛 슬라이더 값 변경 실패 (기대값: {round(initial_value + 1.0, 3)}, 실제값: {new_value_rounded})"
            print(f"✅ 단맛 슬라이더 값 증가 성공: {initial_value_rounded} -> {new_value_rounded}")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-단맛 슬라이더 증가-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-단맛 슬라이더 증가-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-단맛 슬라이더 증가-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_049(self, driver: WebDriver):
    #슬라이더를 실제로 1.0 미만으로 조절하지 못해서 자동화는 실패...
        try:
            # 프로필 수정 페이지로 이동
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)

            # 슬라이더 요소 찾기 (단 맛 슬라이더)
            wait = ws(driver, 10)
            slider = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SWEET_FLAVOR_XPATH)))
            
            # 현재 값 가져오기
            float(slider.get_attribute("aria-valuenow"))
            
            team_feed_page.update_slider_value(driver, slider, change=-5.0)
           
            # 값 변경 후 다시 가져오기
            new_value = float(slider.get_attribute("aria-valuenow"))

            # 슬라이더 값 1.0 미만 검증
            assert float(new_value) < 1.0, f"❌ 단맛 슬라이더 값이 1.0 미만이 아님, 현재 값: {new_value}"

            # 프로필 수정 완료 버튼 클릭
            team_feed_page.profile_edit_finish_btn_click()

            # 오류 메시지 기다리기
            error_message = wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FLAVOR_REQUIRED_MESSAGE_XPATH)))

            # 오류 메시지가 표시되는지 확인
            assert error_message.is_displayed(), f"❌ 단맛-'맛에 대한 성향은 최소 1 이상 설정해주세요' 오류 메시지가 표시되지 않음"
            print("✅ 단맛-오류 메시지: '맛에 대한 성향은 최소 1 이상 설정해주세요' 표시")
            driver.save_screenshot("개발1팀-음식성향-단맛 슬라이더-1.0 미만 오류메시지-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-단맛 슬라이더-1.0 미만 오류메시지-실패 (요소를 찾을 수 없음) : {e}"

        #실제로 슬라이더가 조정되지 않아서 TimeoutException 발생
        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-단맛 슬라이더-1.0 미만 오류메시지-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-단맛 슬라이더-1.0 미만 오류메시지-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_050(self, driver: WebDriver):
        #슬라이더를 실제로 1.0 이상으로 조절하지 못해서 자동화는 실패...
        try:
            # 프로필 수정 페이지로 이동
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)

            # 슬라이더 요소 찾기 (단 맛 슬라이더)
            wait = ws(driver, 10)
            slider = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SWEET_FLAVOR_XPATH)))
            
            # 현재 슬라이더 값 가져오기 (슬라이더 값을 증가시키기 전 값)
            initial_value = float(slider.get_attribute("aria-valuenow"))

            team_feed_page.update_slider_value(driver, slider, change=1.0)

            # 변경된 값 확인
            new_value = float(slider.get_attribute("aria-valuenow"))

            # 프로필 수정 완료 버튼 클릭하여 팀 피드 화면으로 이동
            team_feed_page.profile_edit_finish_btn_click()

            # 팀 피드 화면으로 돌아오기 기다리기
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FEED_TITLE_XPATH)))
            
            slider_team_feed = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SWEET_FLAVOR_XPATH)))
            slider_value_team_feed = float(slider_team_feed.get_attribute("aria-valuenow"))

            # 팀 피드 화면에서 단맛 슬라이더 값이 변경된 값대로 확인
            assert new_value == slider_value_team_feed, f"❌ 팀 피드에서 단맛 슬라이더 값이 변경되지 않음, 변경된 값: {new_value}, 팀 피드 값: {slider_value_team_feed}"

            print(f"✅ 단맛 슬라이더 값이 {initial_value} -> {new_value}로 성공적으로 변경되고 팀 피드 화면에서도 확인됨")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-단맛 슬라이더-1.0 미만 오류메시지-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-단맛 슬라이더-1.0 미만 오류메시지-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-단맛 슬라이더-1.0 미만 오류메시지-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_051(self, driver):
        #실제로 슬라이더를 옮기는건 못해서 자동화 실패...
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)
            wait = ws(driver, 10)
            
            # 슬라이더 요소 찾기 (짠 맛 슬라이더)
            slider = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SALTY_FLAVOR_XPATH)))
            
            # 현재 값 가져오기
            initial_value = float(slider.get_attribute("aria-valuenow"))
            
            team_feed_page.change_slider_value(driver, slider, change=-1.0)
            
            # 값 변경 후 다시 가져오기
            new_value = float(slider.get_attribute("aria-valuenow"))
            
            # 소수점 3자리로 반올림
            initial_value_rounded = round(initial_value, 3)
            new_value_rounded = round(new_value, 3)
            
            # 검증: 기존 값에서 1.0 감소했는지 확인
            assert new_value_rounded == round(initial_value - 1.0, 3), f"❌ 짠맛 슬라이더 값 변경 실패 (기대값: {round(initial_value - 1.0, 3)}, 실제값: {new_value_rounded})"
            print(f"✅ 짠맛 슬라이더 값 감소 성공: {initial_value_rounded} -> {new_value_rounded}")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-짠맛 슬라이더 감소-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-짠맛 슬라이더 감소-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-짠맛 슬라이더 감소-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_052(self, driver):
        #실제로 슬라이더를 옮기는건 못해서 자동화 실패...
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)
            wait = ws(driver, 10)
            
            # 슬라이더 요소 찾기 (짠 맛 슬라이더)
            slider = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SALTY_FLAVOR_XPATH)))
            
            # 현재 값 가져오기
            initial_value = float(slider.get_attribute("aria-valuenow"))
            
            team_feed_page.change_slider_value(driver, slider, change=1.0)
            
            # 값 변경 후 다시 가져오기
            new_value = float(slider.get_attribute("aria-valuenow"))
            
            # 소수점 3자리로 반올림
            initial_value_rounded = round(initial_value, 3)
            new_value_rounded = round(new_value, 3)
            
            # 검증: 기존 값에서 1.0 증가했는지 확인
            assert new_value_rounded == round(initial_value + 1.0, 3), f"❌ 짠맛 슬라이더 값 변경 실패 (기대값: {round(initial_value + 1.0, 3)}, 실제값: {new_value_rounded})"
            print(f"✅ 짠맛 슬라이더 값 증가 성공: {initial_value_rounded} -> {new_value_rounded}")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-짠맛 슬라이더 증가-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-짠맛 슬라이더 증가-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-짠맛 슬라이더 증가-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_053(self, driver: WebDriver):
    #슬라이더를 실제로 1.0 미만으로 조절하지 못해서 자동화는 실패...
        try:
            # 프로필 수정 페이지로 이동
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)

            # 슬라이더 요소 찾기 (짠 맛 슬라이더)
            wait = ws(driver, 10)
            slider = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SALTY_FLAVOR_XPATH)))
            
            # 현재 값 가져오기
            float(slider.get_attribute("aria-valuenow"))
            
            team_feed_page.update_slider_value(driver, slider, change=-5.0)
           
            # 값 변경 후 다시 가져오기
            new_value = float(slider.get_attribute("aria-valuenow"))

            # 슬라이더 값 1.0 미만 검증
            assert float(new_value) < 1.0, f"❌ 짠맛 슬라이더 값이 1.0 미만이 아님, 현재 값: {new_value}"

            # 프로필 수정 완료 버튼 클릭
            team_feed_page.profile_edit_finish_btn_click()

            # 오류 메시지 기다리기
            error_message = wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FLAVOR_REQUIRED_MESSAGE_XPATH)))

            # 오류 메시지가 표시되는지 확인
            assert error_message.is_displayed(), f"❌ 짠맛-'맛에 대한 성향은 최소 1 이상 설정해주세요' 오류 메시지가 표시되지 않음"
            print("✅ 짠맛-오류 메시지: '맛에 대한 성향은 최소 1 이상 설정해주세요' 표시")
            driver.save_screenshot("개발1팀-음식성향-짠맛 슬라이더-1.0 미만 오류메시지-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-짠맛 슬라이더-1.0 미만 오류메시지-실패 (요소를 찾을 수 없음) : {e}"

        #실제로 슬라이더가 조정되지 않아서 TimeoutException 발생
        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-짠맛 슬라이더-1.0 미만 오류메시지-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-짠맛 슬라이더-1.0 미만 오류메시지-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_054(self, driver: WebDriver):
        #슬라이더를 실제로 1.0 이상으로 조절하지 못해서 자동화는 실패...
        try:
            # 프로필 수정 페이지로 이동
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)

            # 슬라이더 요소 찾기 (짠 맛 슬라이더)
            wait = ws(driver, 10)
            slider = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SALTY_FLAVOR_XPATH)))
            
            # 현재 슬라이더 값 가져오기 (슬라이더 값을 증가시키기 전 값)
            initial_value = float(slider.get_attribute("aria-valuenow"))

            team_feed_page.update_slider_value(driver, slider, change=1.0)

            # 변경된 값 확인
            new_value = float(slider.get_attribute("aria-valuenow"))

            # 프로필 수정 완료 버튼 클릭하여 팀 피드 화면으로 이동
            team_feed_page.profile_edit_finish_btn_click()

            # 팀 피드 화면으로 돌아오기 기다리기
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FEED_TITLE_XPATH)))
            
            slider_team_feed = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SALTY_FLAVOR_XPATH)))
            slider_value_team_feed = float(slider_team_feed.get_attribute("aria-valuenow"))

            # 팀 피드 화면에서 짠맛 슬라이더 값이 변경된 값대로 확인
            assert new_value == slider_value_team_feed, f"❌ 팀 피드에서 짠맛 슬라이더 값이 변경되지 않음, 변경된 값: {new_value}, 팀 피드 값: {slider_value_team_feed}"

            print(f"✅ 짠맛 슬라이더 값이 {initial_value} -> {new_value}로 성공적으로 변경되고 팀 피드 화면에서도 확인됨")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-짠맛 슬라이더-1.0 미만 오류메시지-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-짠맛 슬라이더-1.0 미만 오류메시지-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-짠맛 슬라이더-1.0 미만 오류메시지-실패 (알 수 없는 오류) : {e}"


        ##@pytest.mark.skip()
    def test_teamfeed_055(self, driver):
        #실제로 슬라이더를 옮기는건 못해서 자동화 실패...
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)
            wait = ws(driver, 10)
            
            # 슬라이더 요소 찾기 (매운 맛 슬라이더)
            slider = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SPICY_FLAVOR_XPATH)))
            
            # 현재 값 가져오기
            initial_value = float(slider.get_attribute("aria-valuenow"))
            
            team_feed_page.change_slider_value(driver, slider, change=-1.0)
            
            # 값 변경 후 다시 가져오기
            new_value = float(slider.get_attribute("aria-valuenow"))
            
            # 소수점 3자리로 반올림
            initial_value_rounded = round(initial_value, 3)
            new_value_rounded = round(new_value, 3)
            
            # 검증: 기존 값에서 1.0 감소했는지 확인
            assert new_value_rounded == round(initial_value - 1.0, 3), f"❌ 매운맛 슬라이더 값 변경 실패 (기대값: {round(initial_value - 1.0, 3)}, 실제값: {new_value_rounded})"
            print(f"✅ 매운맛 슬라이더 값 감소 성공: {initial_value_rounded} -> {new_value_rounded}")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-매운맛 슬라이더 감소-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-매운맛 슬라이더 감소-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-매운맛 슬라이더 감소-실패 (알 수 없는 오류) : {e}"


    ##@pytest.mark.skip()
    def test_teamfeed_056(self, driver):
        #실제로 슬라이더를 옮기는건 못해서 자동화 실패...
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)
            wait = ws(driver, 10)
            
            # 슬라이더 요소 찾기 (매운 맛 슬라이더)
            slider = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SPICY_FLAVOR_XPATH)))
            
            # 현재 값 가져오기
            initial_value = float(slider.get_attribute("aria-valuenow"))
            
            team_feed_page.change_slider_value(driver, slider, change=1.0)
            
            # 값 변경 후 다시 가져오기
            new_value = float(slider.get_attribute("aria-valuenow"))
            
            # 소수점 3자리로 반올림
            initial_value_rounded = round(initial_value, 3)
            new_value_rounded = round(new_value, 3)
            
            # 검증: 기존 값에서 1.0 증가했는지 확인
            assert new_value_rounded == round(initial_value + 1.0, 3), f"❌ 매운맛 슬라이더 값 변경 실패 (기대값: {round(initial_value + 1.0, 3)}, 실제값: {new_value_rounded})"
            print(f"✅ 매운맛 슬라이더 값 증가 성공: {initial_value_rounded} -> {new_value_rounded}")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-매운맛 슬라이더 증가-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-매운맛 슬라이더 증가-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-매운맛 슬라이더 증가-실패 (알 수 없는 오류) : {e}"


    ##@pytest.mark.skip()
    def test_teamfeed_057(self, driver: WebDriver):
    #슬라이더를 실제로 1.0 미만으로 조절하지 못해서 자동화는 실패...
        try:
            # 프로필 수정 페이지로 이동
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)

            # 슬라이더 요소 찾기 (매운 맛 슬라이더)
            wait = ws(driver, 10)
            slider = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SPICY_FLAVOR_XPATH)))
            
            # 현재 값 가져오기
            float(slider.get_attribute("aria-valuenow"))
            
            team_feed_page.update_slider_value(driver, slider, change=-5.0)
           
            # 값 변경 후 다시 가져오기
            new_value = float(slider.get_attribute("aria-valuenow"))

            # 슬라이더 값 1.0 미만 검증
            assert float(new_value) < 1.0, f"❌ 매운맛 슬라이더 값이 1.0 미만이 아님, 현재 값: {new_value}"

            # 프로필 수정 완료 버튼 클릭
            team_feed_page.profile_edit_finish_btn_click()

            # 오류 메시지 기다리기
            error_message = wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FLAVOR_REQUIRED_MESSAGE_XPATH)))

            # 오류 메시지가 표시되는지 확인
            assert error_message.is_displayed(), f"❌ 매운맛-'맛에 대한 성향은 최소 1 이상 설정해주세요' 오류 메시지가 표시되지 않음"
            print("✅ 매운맛-오류 메시지: '맛에 대한 성향은 최소 1 이상 설정해주세요' 표시")
            driver.save_screenshot("개발1팀-음식성향-매운맛 슬라이더-1.0 미만 오류메시지-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-매운맛 슬라이더-1.0 미만 오류메시지-실패 (요소를 찾을 수 없음) : {e}"

        #실제로 슬라이더가 조정되지 않아서 TimeoutException 발생
        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-매운맛 슬라이더-1.0 미만 오류메시지-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-매운맛 슬라이더-1.0 미만 오류메시지-실패 (알 수 없는 오류) : {e}"


    ##@pytest.mark.skip()
    def test_teamfeed_058(self, driver: WebDriver):
        #슬라이더를 실제로 1.0 이상으로 조절하지 못해서 자동화는 실패...
        try:
            # 프로필 수정 페이지로 이동
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)

            # 슬라이더 요소 찾기 (매운 맛 슬라이더)
            wait = ws(driver, 10)
            slider = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SPICY_FLAVOR_XPATH)))
            
            # 현재 슬라이더 값 가져오기 (슬라이더 값을 증가시키기 전 값)
            initial_value = float(slider.get_attribute("aria-valuenow"))

            team_feed_page.update_slider_value(driver, slider, change=1.0)

            # 변경된 값 확인
            new_value = float(slider.get_attribute("aria-valuenow"))

            # 프로필 수정 완료 버튼 클릭하여 팀 피드 화면으로 이동
            team_feed_page.profile_edit_finish_btn_click()

            # 팀 피드 화면으로 돌아오기 기다리기
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FEED_TITLE_XPATH)))
            
            slider_team_feed = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_SPICY_FLAVOR_XPATH)))
            slider_value_team_feed = float(slider_team_feed.get_attribute("aria-valuenow"))

            # 팀 피드 화면에서 매운맛 슬라이더 값이 변경된 값대로 확인
            assert new_value == slider_value_team_feed, f"❌ 팀 피드에서 매운맛 슬라이더 값이 변경되지 않음, 변경된 값: {new_value}, 팀 피드 값: {slider_value_team_feed}"

            print(f"✅ 매운맛 슬라이더 값이 {initial_value} -> {new_value}로 성공적으로 변경되고 팀 피드 화면에서도 확인됨")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-매운맛 슬라이더-1.0 미만 오류메시지-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-매운맛 슬라이더-1.0 미만 오류메시지-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-매운맛 슬라이더-1.0 미만 오류메시지-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_059(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)

            wait = ws(driver, 10)
            favorite_food_input = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FAVORITE_FOOD_INPUT_XPATH)))
            favorite_food_input.clear()
            favorite_food_input.send_keys("123456789")
            time.sleep(1)
            team_feed_page.profile_edit_finish_btn_click()

            review_10more_required_message = wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.REVIEW_10MORE_REQUIRED_MESSAGE_XPATH)))

            assert review_10more_required_message.is_displayed(), f"❌ 좋아하는 음식-'10자 이상 입력해주세요' 빨간색 오류 메시지 노출안됨"
            print("✅ 좋아하는 음식-'10자 이상 입력해주세요' 빨간색 오류 메시지 노출")
            driver.save_screenshot("개발1팀-음식성향-좋아하는 음식 10자 미만 텍스트-오류메시지-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-좋아하는 음식 10자 미만 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-좋아하는 음식 10자 미만 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-좋아하는 음식 10자 미만 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_060(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)
            favorite_food_input_message = "한식에서 매콤한 음식을 좋아합니다."

            wait = ws(driver, 10)
            favorite_food_input = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.FAVORITE_FOOD_INPUT_XPATH)))
            favorite_food_input.clear()
            favorite_food_input.send_keys(favorite_food_input_message)
            team_feed_page.profile_edit_finish_btn_click()

            confirm_favorite_food_input_message = wait.until(EC.visibility_of_element_located((By.XPATH, f"//p[contains(text(), '{favorite_food_input_message}')]")))

            assert confirm_favorite_food_input_message.is_displayed(), "❌ 이런 음식은 좋아요! 텍스트 박스에 입력한 내용이 그대로 노출안됨"
            print("✅ 이런 음식은 좋아요! 텍스트 박스에 입력한 내용이 그대로 노출")
            driver.save_screenshot("개발1팀-음식성향-좋아하는 음식에 입력한 내용 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-좋아하는 음식에 입력한 내용 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-좋아하는 음식에 입력한 내용 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-좋아하는 음식에 입력한 내용 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_061(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)

            wait = ws(driver, 10)
            hate_food_input = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.HATE_FOOD_INPUT_XPATH)))
            hate_food_input.clear()
            hate_food_input.send_keys("123456789")
            team_feed_page.profile_edit_finish_btn_click()

            review_10more_required_message = wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.REVIEW_10MORE_REQUIRED_MESSAGE_XPATH)))

            assert review_10more_required_message.is_displayed(), f"❌ 싫어하는 음식-'10자 이상 입력해주세요' 빨간색 오류 메시지 노출안됨"
            print("✅ 싫어하는 음식-'10자 이상 입력해주세요' 빨간색 오류 메시지 노출")
            driver.save_screenshot("개발1팀-음식성향-싫어하는 음식 10자 미만 텍스트-오류메시지-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-싫어하는 음식 10자 미만 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-싫어하는 음식 10자 미만 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-싫어하는 음식 10자 미만 텍스트-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_062(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)
            hate_food_input_message = "중식에서 느끼한 음식을 싫어합니다."

            wait = ws(driver, 10)
            hate_food_input = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.HATE_FOOD_INPUT_XPATH)))
            hate_food_input.clear()
            hate_food_input.send_keys(hate_food_input_message)
            team_feed_page.profile_edit_finish_btn_click()

            confirm_hate_food_input_message = wait.until(EC.presence_of_element_located((By.XPATH, f"//p[contains(text(), '{hate_food_input_message}')]")))

            assert confirm_hate_food_input_message.is_displayed(), "❌ 이런 음식은 싫어요! 텍스트 박스에 입력한 내용이 그대로 노출안됨"
            print("✅ 이런 음식은 싫어요! 텍스트 박스에 입력한 내용이 그대로 노출")
            driver.save_screenshot("개발1팀-음식성향-싫어하는 음식에 입력한 내용 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-음식성향-싫어하는 음식에 입력한 내용 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-음식성향-싫어하는 음식에 입력한 내용 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-음식성향-싫어하는 음식에 입력한 내용 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()   
    def test_teamfeed_063(self, driver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()
 
            wait = ws(driver, 10) 
            # Stale Element 방지를 위한 재시도 로직
            for _ in range(3):  # 최대 3번 재시도
                try:
                    # canvas 요소 찾기
                    canvas_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "canvas")))

                    # 캔버스가 표시되는지 확인
                    assert canvas_element.is_displayed(), "❌ 파이차트가 보이지 않음 (display: none 또는 숨김 처리됨)"

                    # 크기 확인 (height 또는 width가 0이면 실패)
                    width = int(canvas_element.get_attribute("width"))
                    height = int(canvas_element.get_attribute("height"))

                    assert width > 0 and height > 0, f"❌ 파이차트 크기가 비정상적 (width: {width}, height: {height})"

                    print("✅ 파이차트가 정상적으로 노출됨!")
                    return  # 성공하면 함수 종료

                except StaleElementReferenceException:
                    print("⚠️ StaleElementReferenceException 발생 - 요소 다시 찾기")
                    continue  # 요소를 다시 찾도록 재시도

            assert False, "❌ 파이차트 요소가 Stale 상태로 계속 유지됨"

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-파이차트 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-파이차트 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-파이차트 노출-실패: {e}"


    #@pytest.mark.skip()   
    def test_teamfeed_064(self, driver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()
            wait = ws(driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FEED_TITLE_XPATH)))

            # canvas 요소 찾기
            bar_chart = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.BARCHART_XPATH)))

            # 캔버스가 표시되는지 확인
            assert bar_chart.is_displayed(), "❌ 개발1팀-TOP5 음식 막대그래프가 보이지 않음 (display: none 또는 숨김 처리됨)"
            
            # 크기 확인 (height 또는 width가 0이면 실패)
            width = int(bar_chart.get_attribute("width"))
            height = int(bar_chart.get_attribute("height"))

            assert width > 0 and height > 0, f"❌ 개발1팀-TOP5 음식 막대그래프 크기가 비정상적 (width: {width}, height: {height})"
            print("✅ 개발1팀-TOP5 음식 막대그래프가 정상적으로 노출됨!")

        except NoSuchElementException as e:
            assert False, f"❌ 개발1팀-TOP5 음식 막대그래프 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 개발1팀-TOP5 음식 막대그래프 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 개발1팀-TOP5 음식 막대그래프 노출-실패: {e}"



    #@pytest.mark.skip()
    def test_teamfeed_065(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)

            #후기 컨테이너 선택
            wait = ws(driver, 10)
            review_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.REVIEW_CONTAINER_CSS)))

            #후기 아이템 선택
            review_items = review_container.find_elements(By.TAG_NAME, "p")

            assert len(review_items) > 0, "❌ 팀이 먹은 메뉴 후기가 1개 이상 존재해야 합니다."
            print("✅ 팀이 먹은 메뉴 후기가 1개 이상 존재합니다.")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴목록-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴목록-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴목록-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_066(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)

            solo_dinner = driver.find_elements(By.XPATH, TeamFeedPageLocators.SOLO_DINNER_XPATH)

            # 혼밥 태그가 없어야 정상 (이전 테스트 케이스에서 FAIL이 났으므로)
            assert len(solo_dinner) == 0, f"❌ 혼밥 태그가 표시됨 (버그 존재 가능)"
            print("✅ 기능명세서대로 혼밥태그 존재하지 않음")

        except NoSuchElementException as e:
            pass # 요소가 없으면 정상적으로 테스트 통과

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-혼밥태그-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-혼밥태그-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_067(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)

            group_dinner = driver.find_elements(By.XPATH, TeamFeedPageLocators.GROUP_DINNER_XPATH)

            assert len(group_dinner) > 0, f"❌ 팀이 먹은 메뉴-그룹태그 존재하지 않음"
            print("✅ 팀이 먹은 메뉴-그룹태그 확인")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-그룹태그-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-그룹태그-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-그룹태그-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_068(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)

            team_dinner = driver.find_elements(By.XPATH, TeamFeedPageLocators.TEAM_DINNER_XPATH)

            assert len(team_dinner) > 0, f"❌ 팀이 먹은 메뉴-회식태그 존재하지 않음"
            print("✅ 팀이 먹은 메뉴-회식태그 확인")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-회식태그-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-회식태그-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-회식태그-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_069(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)

            team_feed_page.add_review_btn_click()

            wait = ws(driver, 10)
            add_review_title = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.ADD_REVIEW_TITLE_XPATH)))

            time.sleep(1)
            assert add_review_title.is_displayed(), f"❌ 새로운 후기 등록하기 화면 진입 실패"
            print("✅ 새로운 후기 등록하기 화면 진입 성공")
            driver.save_screenshot("✅ 팀 피드-새로운 후기 등록하기 화면-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-새로운 후기 등록하기 화면-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-새로운 후기 등록하기 화면-실패 (시간 초과) : {e}"

        except Exception as e:
           assert False, f"❌ 팀 피드-새로운 후기 등록하기 화면-실패 (알 수 없는 오류) : {e}"
            

    #@pytest.mark.skip()
    def test_teamfeed_070(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_add_review(driver)

            # "혼밥" 라디오 버튼 찾기
            radio_button = driver.find_element(By.ID, "혼밥")

            # aria-checked 속성값 가져오기
            is_checked = radio_button.get_attribute("aria-checked")

            # 혼밥이 선택된 상태인지 검증
            assert is_checked == "true", "❌ 혼밥 라디오 버튼이 선택되지 않았음!"
            print("✅ 혼밥 라디오 버튼이 선택된 상태로 노출")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-새로운 후기 등록하기-혼밥라디오버튼-실패 (요소를 찾을 수 없음): {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-새로운 후기 등록하기-혼밥라디오버튼-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-새로운 후기 등록하기-혼밥라디오버튼-실패 (알 수 없는 오류): {e}"

   
    #@pytest.mark.skip()
    def test_teamfeed_071(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_add_review(driver)

            team_feed_page.new_review_finish_btn_click()

            wait = ws(driver, 10)
            add_review_title = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.ADD_REVIEW_TITLE_XPATH)))

            time.sleep(1)
            assert add_review_title.is_displayed(), f"❌ 새로운 후기 등록하기 탭 종료"
            print("✅ 새로운 후기 등록하기 화면 탭 종료되지 않음")
            driver.save_screenshot("✅ 필수항목누락-후기작성완료-새로운 후기 등록하기 화면-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 필수항목누락-후기작성완료-새로운 후기 등록하기 화면-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 필수항목누락-후기작성완료-새로운 후기 등록하기 화면-실패 (시간 초과) : {e}"

        except Exception as e:
           assert False, f"❌ 필수항목누락-후기작성완료-새로운 후기 등록하기 화면-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_072(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_add_review(driver)
            team_feed_page.new_review_finish_btn_click()

            wait = ws(driver, 10)
            image_required_message = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.IMAGE_REQUIRED_MESSAGE_XPATH)))

            time.sleep(1)
            assert image_required_message.is_displayed(), f"❌ '리뷰 이미지는 필수입니다' 오류메시지 노출안됨"
            print("✅ '리뷰 이미지는 필수입니다' 오류메시지 노출")

        except NoSuchElementException as e:
            assert False, f"❌ 리뷰이미지누락-후기작성완료 클릭-오류메시지 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 리뷰이미지누락-후기작성완료 클릭-오류메시지 노출-실패 (시간 초과) : {e}"

        except Exception as e:
           assert False, f"❌ 리뷰이미지누락-후기작성완료 클릭-오류메시지 노출-실패 (알 수 없는 오류) : {e}"

    #@pytest.mark.skip()
    def test_teamfeed_073(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_add_review(driver)
            team_feed_page.new_review_finish_btn_click()

            wait = ws(driver, 10)
            menu_required_message = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.MENU_REQUIRED_MESSAGE_XPATH)))

            time.sleep(1)
            assert menu_required_message.is_displayed(), f"❌ '메뉴 명은 필수입니다' 오류메시지 노출안됨"
            print("✅ '메뉴 명은 필수입니다' 오류메시지 노출")

        except NoSuchElementException as e:
            assert False, f"❌ 메뉴명누락-후기작성완료 클릭-오류메시지 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 메뉴명누락-후기작성완료 클릭-오류메시지 노출-실패 (시간 초과) : {e}"

        except Exception as e:
           assert False, f"❌ 메뉴명누락-후기작성완료 클릭-오류메시지 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_074(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_add_review(driver)
            team_feed_page.new_review_finish_btn_click()

            wait = ws(driver, 10)
            category_required_message = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.CATEGORY_REQUIRED_MESSAGE_XPATH)))

            time.sleep(1)
            assert category_required_message.is_displayed(), f"❌ '카테고리는 필수입니다' 오류메시지 노출안됨"
            print("✅ '카테고리는 필수입니다' 오류메시지 노출")

        except NoSuchElementException as e:
            assert False, f"❌ 카테고리누락-후기작성완료 클릭-오류메시지 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 카테고리누락-후기작성완료 클릭-오류메시지 노출-실패 (시간 초과) : {e}"

        except Exception as e:
           assert False, f"❌ 카테고리누락-후기작성완료 클릭-오류메시지 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_075(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_add_review(driver)
            team_feed_page.new_review_finish_btn_click()

            wait = ws(driver, 10)
            review_required_message = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.REVIEW_REQUIRED_MESSAGE_XPATH)))

            time.sleep(1)
            assert review_required_message.is_displayed(), f"❌ '후기는 필수입니다' 오류메시지 노출안됨"
            print("✅ '후기는 필수입니다' 오류메시지 노출")

        except NoSuchElementException as e:
            assert False, f"❌ 후기누락-후기작성완료 클릭-오류메시지 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 후기누락-후기작성완료 클릭-오류메시지 노출-실패 (시간 초과) : {e}"

        except Exception as e:
           assert False, f"❌ 후기누락-후기작성완료 클릭-오류메시지 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_076(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_add_review(driver)
            team_feed_page.new_review_finish_btn_click()

            wait = ws(driver, 10)
            star_required_message = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.STAR_REQUIRED_MESSAGE_XPATH)))

            time.sleep(1)
            assert star_required_message.is_displayed(), f"❌ '별점은 최소 1점 이상이어야 합니다' 오류메시지 노출안됨"
            print("✅ '별점은 최소 1점 이상이어야 합니다' 오류메시지 노출")

        except NoSuchElementException as e:
            assert False, f"❌ 별점누락-후기작성완료 클릭-오류메시지 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 별점누락-후기작성완료 클릭-오류메시지 노출-실패 (시간 초과) : {e}"

        except Exception as e:
           assert False, f"❌ 별점누락-후기작성완료 클릭-오류메시지 노출-실패 (알 수 없는 오류) : {e}"


    #@pytest.mark.skip()
    def test_teamfeed_077(self,driver:WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)            
            team_feed_page.navigate_to_add_review(driver)

            # "회식" 라디오 버튼 찾기
            wait = ws(driver, 10)
            radio_button = wait.until(EC.presence_of_element_located((By.ID, "회식")))
            driver.execute_script("arguments[0].click();", radio_button)
            print("✅ '회식' 라디오 버튼 선택 완료")

            # 이미지 파일 경로 설정 (utils 폴더 내 '깜자.png')
            image_path = TeamFeedPageLocators.IMAGE_PATH  # 절대 경로 변환

            # 파일 업로드 input 요소 찾기
            file_input = driver.find_element(By.NAME, "reviewImg")

            # 파일 경로 입력 (자동으로 파일 업로드됨)
            file_input.send_keys(image_path)
            print("✅ 이미지 업로드 완료")

            wait = ws(driver, 10)
            menu_name = wait.until(EC.presence_of_element_located((By.NAME, 'menu')))
            menu_name.send_keys("팀피드실시간테스트")
            print("✅ 메뉴 명 업로드 완료")

            # 'select' 요소 찾기
            select_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "select")))

            # Select 객체 생성
            select = Select(select_element)

            # '기타' 옵션 선택 (value 기준)
            select.select_by_value("기타")
            print("✅ 카테고리 선택 완료")

            review = wait.until(EC.presence_of_element_located((By.NAME, 'comment')))
            review.send_keys("가"*30)
            print("✅ 후기 업로드 완료")

            star = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.review_stars_3)))
            star.click()
            actual_star = driver.find_elements(By.XPATH, TeamFeedPageLocators.review_star_yellow)
            result = len(actual_star)
            assert result == 3, "별점이 3개가 아님"
            print("✅ 별점 3개 선택 완료")

            #후기 작성 완료 클릭
            team_feed_page.new_review_finish_btn_click()

            title = wait.until(EC.visibility_of_element_located((By.XPATH, TeamFeedPageLocators.TEAM_FEED_TITLE_XPATH)))

            assert title.is_displayed(), f"❌ 후기 작성 완료 클릭-팀 피드 화면으로 돌아오기 실패"
            print("✅ 후기 작성 완료 클릭-팀 피드 화면으로 돌아오기 성공")

        except NoSuchElementException as e:
            assert False, f"❌ 필수항목 모두 작성-새로 등록한 후기 작성완료 클릭-실패 (요소를 찾을 수 없음): {e}"

        except TimeoutException as e:
            assert False, f"❌ 필수항목 모두 작성-새로 등록한 후기 작성완료 클릭-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 필수항목 모두 작성-새로 등록한 후기 작성완료 클릭-실패 (알 수 없는 오류): {e}"


    # #@pytest.mark.skip()
    def test_teamfeed_078(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()

            wait = ws(driver, 10)
            new_review_element = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEST_REVIEW_XPATH)))            
            
            assert new_review_element.text == "팀피드실시간테스트", "❌ 팀 피드에 새로 등록한 후기가 반영 안됨"
            print("✅ 팀 피드에 새로 등록한 후기가 반영")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 확인-실패 (요소를 찾을 수 없음): {e}"

        # 예상대로 팀 피드에 후기가 표시되지 않아 TimeoutException 발생
        except TimeoutException as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 확인-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 확인-실패 (알 수 없는 오류): {e}"


# #@pytest.mark.skip()
    def test_teamfeed_079(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()
            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEST_REVIEW_XPATH)))

            team_dinner = driver.find_elements(By.XPATH, TeamFeedPageLocators.TEST_REVIEW_TAG_XPATH)

            assert team_dinner.text == "회식", f"❌ 회식태그 불일치"
            print("✅ 회식태그 일치")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 식사유형확인-실패 (요소를 찾을 수 없음): {e}"

        # 예상대로 팀 피드에 후기가 표시되지 않아 TimeoutException 발생
        except TimeoutException as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 식사유형확인-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 식사유형확인-실패 (알 수 없는 오류): {e}"


    #@pytest.mark.skip()
    def test_teamfeed_080(self,driver:WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()
            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEST_REVIEW_XPATH)))

            team_feed_page.send_keys(TeamFeedPageLocators.review_img_input, TeamFeedPageLocators.IMAGE_PATH)
            src = team_feed_page.get_attribute(TeamFeedPageLocators.review_img, "src")
            result = is_similar(src, TeamFeedPageLocators.IMAGE_PATH)
            assert result > 0.9, "이미지가 다름"

        # 예상대로 팀 피드에 후기가 표시되지 않아 Exception 발생
        except Exception as e:
            print("이미지 비교 실패")
            assert False


    #@pytest.mark.skip()
    def test_teamfeed_081(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()
            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEST_REVIEW_XPATH)))

            new_review_menu = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEST_REVIEW_MENU_XPATH)))            
            
            assert new_review_menu.text == "팀피드실시간테스트", "❌ 메뉴명 불일치"
            print("✅ 메뉴명 일치")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 메뉴명확인-실패 (요소를 찾을 수 없음): {e}"

        # 예상대로 팀 피드에 후기가 표시되지 않아 TimeoutException 발생
        except TimeoutException as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 메뉴명확인-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 메뉴명확인-실패 (알 수 없는 오류): {e}"


    #@pytest.mark.skip()
    def test_teamfeed_082(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()
            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEST_REVIEW_XPATH)))

            selected_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select option[selected]")))
            selected_value = selected_option.text
            
            # 카테고리 일치하는지 검증
            assert selected_value == "기타", f"❌ 카테고리 불일치"
            print("✅ 카테고리 일치")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 카테고리확인-실패 (요소를 찾을 수 없음): {e}"

        # 예상대로 팀 피드에 후기가 표시되지 않아 TimeoutException 발생
        except TimeoutException as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 카테고리확인-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 카테고리확인-실패 (알 수 없는 오류): {e}"


    #@pytest.mark.skip()
    def test_teamfeed_083(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()
            wait = ws(driver, 10)
            review_input_area = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEST_REVIEW_XPATH)))

            expected_review_text = TeamFeedPageLocators.NEW_REVIEW_TEXT

            actual_text = review_input_area.get_attribute("value")
            
            assert actual_text == expected_review_text, f"❌ 후기내용 불일치, 실제: '{actual_text}"
            print("✅ 후기내용 일치")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 내용확인-실패 (요소를 찾을 수 없음): {e}"

        # 예상대로 팀 피드에 후기가 표시되지 않아 TimeoutException 발생
        except TimeoutException as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 내용확인-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 내용확인-실패 (알 수 없는 오류): {e}"


    #@pytest.mark.skip()
    def test_teamfeed_084(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.TEST_REVIEW_XPATH)))            
 
            actual_star = driver.find_elements(By.XPATH, TeamFeedPageLocators.review_star_yellow)
            result = len(actual_star)
            assert result == 3, "별점이 3개가 아님"
            print("✅ 별점 3개 검증 완료")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 별점확인-실패 (요소를 찾을 수 없음): {e}"

        # 예상대로 팀 피드에 후기가 표시되지 않아 TimeoutException 발생
        except TimeoutException as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 별점확인-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-새로 등록한 후기 별점확인-실패 (알 수 없는 오류): {e}"


    #@pytest.mark.skip()
    def test_teamfeed_085(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)

            # 팀이 먹은 메뉴 목록 중 첫번째 사천해물탕 후기의 '같은 메뉴 먹기' 클릭
            team_feed_page.eat_same_menu_btn_click()

            wait = ws(driver, 10)
            same_menu_review_title = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.SAME_MENU_REVIEW_TITLE_XPATH)))

            time.sleep(1)
            assert same_menu_review_title.is_displayed(), f"❌ 또 먹은 후기 등록하기 화면 진입 실패"
            print("✅ 또 먹은 후기 등록하기 화면 진입 성공")
            driver.save_screenshot("✅ 같은메뉴먹기 클릭-또 먹은 후기 등록하기 화면-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 같은메뉴먹기 클릭-또 먹은 후기 등록하기 화면-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 같은메뉴먹기 클릭-또 먹은 후기 등록하기 화면-실패 (시간 초과) : {e}"

        except Exception as e:
           assert False, f"❌ 같은메뉴먹기 클릭-또 먹은 후기 등록하기 화면-실패 (알 수 없는 오류) : {e}"

        
    #@pytest.mark.skip()
    def test_teamfeed_086(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)

            # 팀이 먹은 메뉴 목록 중 첫번째 사천해물탕 후기의 '같은 메뉴 먹기' 클릭
            team_feed_page.eat_same_menu_btn_click()

            # 식사유형 "회식" 자동 적용 검증
            team_dinner_button = driver.find_element(By.ID, "회식")

            # aria-checked 속성값 가져오기
            is_checked = team_dinner_button.get_attribute("aria-checked")

            # 회식이 선택된 상태인지 검증
            assert is_checked == "true", "❌ 회식 라디오 버튼이 자동적용 실패!"
            print("✅ 회식 라디오 버튼 자동적용 성공")

        except NoSuchElementException as e:
            assert False, f"❌ 또 먹은 후기 등록하기-식사유형 자동 적용-실패 (요소를 찾을 수 없음): {e}"

        except TimeoutException as e:
            assert False, f"❌ 또 먹은 후기 등록하기-식사유형 자동 적용-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 또 먹은 후기 등록하기-식사유형 자동 적용-실패 (알 수 없는 오류): {e}"


    #@pytest.mark.skip()
    def test_teamfeed_087(self,driver:WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)
            team_feed_page.eat_same_menu_btn_click()

            # 기존 사천해물탕 후기 이미지의 src 값 (실제 웹 페이지에서 얻어야 함)
            expected_src = TeamFeedPageLocators.same_menu_src

            #이미지 요소의 src 속성 값 가져오기
            wait = ws(driver, 10)        
            image_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.SAME_MENU_IMAGE_CSS)))
            actual_src = image_element.get_attribute("src")

            #이미지 src 값 비교
            assert actual_src == expected_src, f"❌ 이미지 src 불일치: 기대값 '{expected_src}', 실제값 '{actual_src}'"
            print("✅ 이미지 src 일치")

        except NoSuchElementException as e:
            assert False, f"❌ 또 먹은 후기 등록하기-이미지 자동 적용-실패 (요소를 찾을 수 없음): {e}"

        except TimeoutException as e:
            assert False, f"❌ 또 먹은 후기 등록하기-이미지 자동 적용-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 또 먹은 후기 등록하기-이미지 자동 적용-실패 (알 수 없는 오류): {e}"


    #@pytest.mark.skip()
    def test_teamfeed_088(self,driver:WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)
            team_feed_page.eat_same_menu_btn_click()

            # 기존 사천해물탕 메뉴 명
            wait = ws(driver, 10)        
            input_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.SAME_MENU_NAME_CSS)))

            # input 요소의 value 속성 값 가져오기
            actual_value = input_element.get_attribute("value")

            #이미지 src 값 비교
            assert actual_value == "사천해물탕", f"❌ 메뉴 명 불일치, 실제: '{actual_value}'"
            print("✅ 메뉴 명 일치")

        except NoSuchElementException as e:
            assert False, f"❌ 또 먹은 후기 등록하기-메뉴 명 자동 적용-실패 (요소를 찾을 수 없음): {e}"

        except TimeoutException as e:
            assert False, f"❌ 또 먹은 후기 등록하기-메뉴 명 자동 적용-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 또 먹은 후기 등록하기-메뉴 명 자동 적용-실패 (알 수 없는 오류): {e}"


    #@pytest.mark.skip()
    def test_teamfeed_089(self,driver:WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)
            team_feed_page.eat_same_menu_btn_click()

            # 기존 사천해물탕 카테고리
            wait = ws(driver, 10)        
            selected_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select option[selected]")))
            selected_value = selected_option.text
            
            assert selected_value == "중식", f"❌ 카테고리 불일치"
            print("✅ 카테고리 일치")

        except NoSuchElementException as e:
            assert False, f"❌ 또 먹은 후기 등록하기-카테고리 자동 적용-실패 (요소를 찾을 수 없음): {e}"

        except TimeoutException as e:
            assert False, f"❌ 또 먹은 후기 등록하기-카테고리 자동 적용-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 또 먹은 후기 등록하기-카테고리 자동 적용-실패 (알 수 없는 오류): {e}"


    #@pytest.mark.skip()
    def test_teamfeed_090(self,driver:WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)
            team_feed_page.eat_same_menu_btn_click()

            expected_review_text = TeamFeedPageLocators.SAME_MENU_REVIEW_TEXT

            # 기존 사천해물탕 후기
            wait = ws(driver, 10)        
            review_input_area = wait.until(EC.presence_of_element_located((By.XPATH, TeamFeedPageLocators.SAME_MENU_REVIEW_XPATH)))
            actual_text = review_input_area.get_attribute("value")
            
            assert actual_text == expected_review_text, f"❌ 후기내용 불일치, 실제: '{actual_text}"
            print("✅ 후기내용 일치")

        except NoSuchElementException as e:
            assert False, f"❌ 또 먹은 후기 등록하기-후기내용 자동 적용-실패 (요소를 찾을 수 없음): {e}"

        except TimeoutException as e:
            assert False, f"❌ 또 먹은 후기 등록하기-후기내용 자동 적용-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 또 먹은 후기 등록하기-후기내용 자동 적용-실패 (알 수 없는 오류): {e}"


    # #@pytest.mark.skip()
    def test_teamfeed_091(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)
            team_feed_page.eat_same_menu_btn_click()

            # 별점 값 요소 찾기
            wait = ws(driver, 10)
            star_input_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, TeamFeedPageLocators.SAME_MENU_STAR_CSS)))

            # 실제 별점 값 가져오기
            actual_star_value = star_input_element.get_attribute("value")

            # 별점이 자동 적용되지 않고 초기화(0)되었는지 검증
            assert actual_star_value != "0", f"❌ 별점이 초기화됨, 예상: '이전 별점', 실제: '{actual_star_value}'"
            print("✅ 별점이 자동 적용됨 (정상적인 동작)")

        except NoSuchElementException as e:
            assert False, f"❌ 또 먹은 후기 등록하기-별점 초기화 적용-실패 (요소를 찾을 수 없음): {e}"

        except TimeoutException as e:
            assert False, f"❌ 또 먹은 후기 등록하기- 초기화 적용-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 또 먹은 후기 등록하기-별점 초기화 적용-실패 (알 수 없는 오류): {e}"