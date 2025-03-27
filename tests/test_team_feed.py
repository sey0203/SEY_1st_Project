import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from pages.team_feed import TeamFeedPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("login_driver")
class TestTeamFeedPage:
    GNB_SELECTOR = "div.fixed.bottom-0.w-full.z-50.max-w-\\[600px\\].border-t-\\[1px\\].bg-white.border-gray-200.p-3.h-16"
    TEAM_FEED_ICON_SELECTOR = "svg.fill-current"
    COMBOBOX_TEAM_XPATH = "//span[text()='개발 1팀']"
    TEAM_FEED_TITLE_XPATH = "//span[text()='팀 피드']"
    FOOD_TENDENCY_XPATH = "//span[contains(text(), '음식 성향')]"
    TEAM_STATS_XPATH = "//span[contains(text(), '팀 통계')]"
    TEAM_EATEN_MENU_XPATH = "//span[contains(text(), '팀이 먹은 메뉴')]"
    TEAM_NAME_SELECTOR = "div.px-2.py-1.rounded-lg.bg-sub-2 > span"
    TEAM_SWEET_FLAVOR_SELECTOR = "section:nth-child(2) > span.font-semibold.w-14.text-main-black"
    TEAM_SALTY_FLAVOR_SELECTOR = "section:nth-child(3) > span.font-semibold.w-14.text-main-black"
    TEAM_SPICY_FLAVOR_SELECTOR = "section:nth-child(4) > span.font-semibold.w-14.text-main-black"
    TEAM_FAVORITE_FOOD_XPATH = "//*[@id='root']/div[1]/main/section/section/section/div[2]/div[1]/p"
    TEAM_HATE_FOOD_XPATH = "//*[@id='root']/div[1]/main/section/section/section/div[2]/div[2]/p"
    PROFILE_EDIT_XPATH = "//span[text()='프로필 정보 수정']"
    SWEET_SLIDER_XPATH = "//section[contains(., '단 맛')]//span[@role='slider']"
    SOLO_DINNER_XPATH = "//div[@class='inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-main text-white' and text()='혼밥']"
    GROUP_DINNER_XPATH = "//div[@class='inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-main text-white' and text()='그룹']"
    TEAM_DINNER_XPATH = "//div[@class='inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-main text-white' and text()='회식']"
    REVIEW_CONTAINER_CSS = "div.flex.w-full.gap-6.p-4.shadow-md.rounded-2xl"
    ADD_REVIEW_XPATH = "//span[text()='새로운 후기 등록하기']"

    
    @pytest.mark.skip()
    def test_teamfeed_001(self, driver: WebDriver):
        try:
            home_gnb = driver.find_element(By.CSS_SELECTOR, self.GNB_SELECTOR)
            wait = ws(driver, 10)
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.GNB_SELECTOR)))
            
            assert home_gnb.is_displayed(), "❌ 홈 GNB 찾지못함"
            print("✅ 홈 GNB 노출")
            
            team_feed_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.TEAM_FEED_ICON_SELECTOR)))
            
            assert team_feed_icon.is_displayed(), "❌ 팀 피드 아이콘 노출 안됨"
            print("✅ 팀 피드 아이콘 표시")
            driver.save_screenshot("✅ 팀 피드 아이콘-성공.png")
        
        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드 아이콘-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드 아이콘-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드 아이콘-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_002(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()

            assert "teams" in driver.current_url, f"❌ 현재 url: {driver.current_url}"
            driver.save_screenshot("✅ 팀 피드 페이지-오픈-성공.png")
        
        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드 페이지-오픈-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드 페이지-오픈-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드 페이지-오픈-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_003(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()

            wait = ws(driver, 10)
            title = wait.until(EC.visibility_of_element_located((By.XPATH, self.TEAM_FEED_TITLE_XPATH)))

            assert title.is_displayed(), f"❌ 팀 피드 title 노출 안됨, 실제: {title.text}"
            driver.save_screenshot("✅ 팀 피드 title 노출-성공.png")
        
        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드 title 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드 title 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드 title 노출-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_004(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            # "개발 1팀" 선택           
            wait = ws(driver, 10)
            team_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.COMBOBOX_TEAM_XPATH)))
            ActionChains(driver).move_to_element(team_option).click().perform()

            assert "teams/1" in driver.current_url, f"❌ 개발 1팀 선택 실패, 현재 url: {driver.current_url}"
            print("✅ 개발 1팀 선택 성공")
            driver.save_screenshot("✅ 팀 피드-드롭다운-개발1팀 선택-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-드롭다운-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-드롭다운-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-드롭다운-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_005(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team_select()

            wait = ws(driver, 10)
            food_tendency = wait.until(EC.presence_of_element_located((By.XPATH, self.FOOD_TENDENCY_XPATH)))

            assert food_tendency.is_displayed(), f"❌ 음식 성향 노출 안됨, 실제: {food_tendency.text}"
            print("✅ 음식 성향 노출 성공")
            driver.save_screenshot("✅ 팀 피드-음식 성향 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-음식 성향 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-음식 성향 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-음식 성향 노출-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_006(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team_select()

            team_feed_page.team_stats_scroll()
            team_stats = driver.find_element(By.XPATH, self.TEAM_STATS_XPATH)

            assert team_stats.is_displayed(), f"❌ 팀 통계 노출 안됨, 실제: {team_stats.text}"
            print("✅ 팀 통계 노출 성공")
            driver.save_screenshot("✅ 팀 피드-팀 통계 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-팀 통계 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-팀 통계 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-팀 통계 노출-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_007(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team_select()

            team_feed_page.team_stats_scroll()
            team_eaten_menu = driver.find_element(By.XPATH, self.TEAM_EATEN_MENU_XPATH)

            assert team_eaten_menu.is_displayed(), f"❌ 팀이 먹은 메뉴 노출 안됨, 실제: {team_eaten_menu.text}"
            print("✅ 팀이 먹은 메뉴 노출 성공")
            driver.save_screenshot("✅ 팀 피드-팀이 먹은 메뉴 노출-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴 노출-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴 노출-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_008(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, self.FOOD_TENDENCY_XPATH)))

            team_name =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.TEAM_NAME_SELECTOR)))

            assert team_name.text == "개발 1팀", f"❌ '개발 1팀' 텍스트 불일치, 실제: {team_name.text}"
            print("✅ '개발 1팀' 텍스트 확인 성공")  
            driver.save_screenshot("✅ 팀 피드-'개발 1팀' 텍스트-성공.png")                

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-'개발 1팀' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-'개발 1팀' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-'개발 1팀' 텍스트-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_009(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, self.FOOD_TENDENCY_XPATH)))

            team_sweet_flavor =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.TEAM_SWEET_FLAVOR_SELECTOR)))

            assert team_sweet_flavor.text == "단 맛", f"❌ '단 맛' 텍스트 불일치, 실제: {team_sweet_flavor.text}"
            print("✅ '단 맛' 텍스트 확인 성공")  
            driver.save_screenshot("✅ 팀 피드-'단 맛' 텍스트-성공.png")                

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-'단 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-'단 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-'단 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_010(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, self.FOOD_TENDENCY_XPATH)))

            team_salty_flavor =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.TEAM_SALTY_FLAVOR_SELECTOR)))

            assert team_salty_flavor.text == "짠 맛", f"❌ '짠 맛' 텍스트 불일치, 실제: {team_salty_flavor.text}"
            print("✅ '짠 맛' 텍스트 확인 성공")  
            driver.save_screenshot("✅ 팀 피드-'짠 맛' 텍스트-성공.png")                

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-'짠 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-'짠 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-'짠 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_011(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, self.FOOD_TENDENCY_XPATH)))

            team_spicy_flavor =  wait.until(EC.visibility_of_element_located((By.XPATH, self.TEAM_SPICY_FLAVOR_SELECTOR)))

            assert team_spicy_flavor.text == "매운 맛", f"❌ '매운 맛' 텍스트 불일치, 실제: {team_spicy_flavor.text}"
            print("✅ '매운 맛' 텍스트 확인 성공")  
            driver.save_screenshot("✅ 팀 피드-'매운 맛' 텍스트-성공.png")                

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-'매운 맛' 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-'매운 맛' 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-'매운 맛' 텍스트-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_012(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, self.FOOD_TENDENCY_XPATH)))

            team_favorite_food =  wait.until(EC.visibility_of_element_located((By.XPATH, self.TEAM_FAVORITE_FOOD_XPATH)))

            assert len(team_favorite_food.text) > 0 , f"❌ 좋아하는 음식 텍스트 존재하지 않음"
            print("✅ 좋아하는 음식 텍스트 존재")  
            driver.save_screenshot("✅ 팀 피드-좋아하는 음식 텍스트-성공.png")                

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-좋아하는 음식 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-좋아하는 음식 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-좋아하는 음식 텍스트-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_013(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team_select()

            wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, self.FOOD_TENDENCY_XPATH)))

            team_hate_food =  wait.until(EC.visibility_of_element_located((By.XPATH, self.TEAM_HATE_FOOD_XPATH)))

            assert len(team_hate_food.text) > 0 , f"❌ 싫어하는 음식 텍스트 존재하지 않음"
            print("✅ 싫어하는 음식 텍스트 존재")  
            driver.save_screenshot("✅ 팀 피드-싫어하는 음식 텍스트-성공.png")                

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-싫어하는 음식 텍스트-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-싫어하는 음식 텍스트-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-싫어하는 음식 텍스트-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_014(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()          

            team_feed_page.combobox_btn_click()

            team_feed_page.combobox_team_select()

            team_feed_page.profile_edit_icon_click()

            wait = ws(driver, 10)
            edit_title = wait.until(EC.visibility_of_element_located((By.XPATH, self.PROFILE_EDIT_XPATH)))

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


    @pytest.mark.skip()
    def test_teamfeed_015(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)

            team_feed_page.profile_edit_finish_btn_click()

            wait = ws(driver, 10)
            title = wait.until(EC.visibility_of_element_located((By.XPATH, self.TEAM_FEED_TITLE_XPATH)))

            assert title.is_displayed(), f"❌ 프로필 수정 완료 클릭-팀 피드 화면으로 돌아오기 실패"
            driver.save_screenshot("✅ 프로필 수정 완료 클릭-팀 피드 화면으로 돌아오기-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-프로필 수정 완료 클릭-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-프로필 수정 완료 클릭-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-프로필 수정 완료 클릭-실패 (알 수 없는 오류) : {e}"
        

    @pytest.mark.skip()
    def test_teamfeed_016(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_profile_edit(driver)

            team_feed_page.profile_edit_X_btn_click()

            wait = ws(driver, 10)
            title = wait.until(EC.visibility_of_element_located((By.XPATH, self.TEAM_FEED_TITLE_XPATH)))

            time.sleep(1)
            assert title.is_displayed(), f"❌ 'X' 버튼 클릭-팀 피드 화면으로 돌아오기 실패"
            driver.save_screenshot("✅ 'X' 버튼 클릭-팀 피드 화면으로 돌아오기-성공.png")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-'X' 버튼 클릭-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-'X' 버튼 클릭-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-'X' 버튼 클릭-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_082(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)

            #후기 컨테이너 선택
            wait = ws(driver, 10)
            review_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.REVIEW_CONTAINER_CSS)))

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


    @pytest.mark.skip()
    def test_teamfeed_083(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)

            solo_dinner = driver.find_elements(By.XPATH, self.SOLO_DINNER_XPATH)

            # 혼밥 태그가 없어야 정상 (이전 테스트 케이스에서 FAIL이 났으므로)
            assert len(solo_dinner) == 0, f"❌ 혼밥 태그가 표시됨 (버그 존재 가능)"
            print("✅ 기능명세서대로 혼밥태그 존재하지 않음")

        except NoSuchElementException as e:
            pass # 요소가 없으면 정상적으로 테스트 통과

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-혼밥태그-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-혼밥태그-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_084(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)

            group_dinner = driver.find_elements(By.XPATH, self.GROUP_DINNER_XPATH)

            assert len(group_dinner) > 0, f"❌ 팀이 먹은 메뉴-그룹태그 존재하지 않음"
            print("✅ 팀이 먹은 메뉴-그룹태그 확인")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-그룹태그-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-그룹태그-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-그룹태그-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip()
    def test_teamfeed_085(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)

            team_dinner = driver.find_elements(By.XPATH, self.TEAM_DINNER_XPATH)

            assert len(team_dinner) > 0, f"❌ 팀이 먹은 메뉴-회식태그 존재하지 않음"
            print("✅ 팀이 먹은 메뉴-회식태그 확인")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-회식태그-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-회식태그-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-팀이 먹은 메뉴-회식태그-실패 (알 수 없는 오류) : {e}"


    # @pytest.mark.skip()
    def test_teamfeed_086(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_team_eaten_menu(driver)

            team_feed_page.team_eaten_menu_add_btn_click()

            wait = ws(driver, 10)
            add_review_title = wait.until(EC.presence_of_element_located((By.XPATH, self.ADD_REVIEW_XPATH)))

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
            

    @pytest.mark.skip()
    def test_teamfeed_087(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.navigate_to_add_review(driver)

            # "혼밥" 라디오 버튼 찾기
            honbap_button = driver.find_element(By.ID, "혼밥")

            # aria-checked 속성값 가져오기
            is_checked = honbap_button.get_attribute("aria-checked")

            # 혼밥이 선택된 상태인지 검증
            assert is_checked == "true", "❌ 혼밥 라디오 버튼이 선택되지 않았음!"
            print("✅ 혼밥 라디오 버튼이 선택된 상태로 노출")

        except NoSuchElementException as e:
            assert False, f"❌ 팀 피드-새로운 후기 등록하기-혼밥라디오버튼-실패 (요소를 찾을 수 없음): {e}"

        except TimeoutException as e:
            assert False, f"❌ 팀 피드-새로운 후기 등록하기-혼밥라디오버튼-실패 (시간 초과): {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드-새로운 후기 등록하기-혼밥라디오버튼-실패 (알 수 없는 오류): {e}"
