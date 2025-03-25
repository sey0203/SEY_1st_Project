import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from tests.pages.team_feed import TeamFeedPage
from tests.pages.login_page import LoginPage
from selenium.webdriver.common.action_chains import ActionChains



@pytest.mark.usefixtures("login_driver")
class TestTeamFeedPage:
    GNB_SELECTOR = "div.fixed.bottom-0.w-full.z-50.max-w-\\[600px\\].border-t-\\[1px\\].bg-white.border-gray-200.p-3.h-16"
    TEAM_FEED_ICON_SELECTOR = "svg.fill-current"
    COMBOBOX_XPATH = "//span[text()='개발 1팀']"
    PROFILE_SELECTOR = "svg.cursor-pointer"
    
    @pytest.mark.skip(reason="테스트 통과해서 생략")
    def test_TC_001(self, driver: WebDriver):
        try:
            home_gnb = driver.find_element(By.CSS_SELECTOR, self.GNB_SELECTOR)
            wait = ws(driver, 10)
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.GNB_SELECTOR)))
            
            assert home_gnb.is_displayed(), "❌ 홈 GNB 찾지못함"
            print("✅ 홈 GNB 나타남")
            
            team_feed_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.TEAM_FEED_ICON_SELECTOR)))
            
            assert team_feed_icon.is_displayed(), "❌ 팀 피드 아이콘 표시 안됨"
            print("✅ 팀 피드 아이콘 표시")
            driver.save_screenshot("팀 피드 아이콘-성공.png")
        
        except NoSuchElementException as e:
            assert False, f"팀 피드 페이지-오픈-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"팀 피드 페이지-오픈-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드 페이지-오픈-실패 (알 수 없는 오류) : {e}"


    # @pytest.mark.skip(reason="테스트 통과해서 생략")
    def test_TC_002(self, driver: WebDriver):
        try:
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()

            assert "teams" in driver.current_url
            driver.save_screenshot("팀 피드 페이지-오픈-성공.png")
        
        except NoSuchElementException as e:
            assert False, f"팀 피드 페이지-오픈-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"팀 피드 페이지-오픈-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드 페이지-오픈-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip(reason="테스트 통과해서 생략")
    def test_TC_003(self, driver: WebDriver):
        try:
            home_gnb = driver.find_element(By.CSS_SELECTOR, self.GNB_SELECTOR)
            wait = ws(driver, 10)
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.GNB_SELECTOR)))
            
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()
            
            wait.until(EC.url_contains("teams"))

            assert "teams" in driver.current_url
            driver.save_screenshot("팀 피드 페이지-오픈-성공.png")
        
        except NoSuchElementException as e:
            assert False, f"팀 피드 페이지-오픈-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"팀 피드 페이지-오픈-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드 페이지-오픈-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip(reason="테스트 통과해서 생략")
    def test_combobox_select(self, driver: WebDriver):
        try:
            driver.find_element(By.CSS_SELECTOR, self.GNB_SELECTOR)
            wait = ws(driver, 10)
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.GNB_SELECTOR)))
            
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()
            
            wait.until(EC.url_contains("teams"))

            team_feed_page.combobox_btn_click()

            # "개발 1팀" 선택           
            team_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.COMBOBOX_XPATH)))
            ActionChains(driver).move_to_element(team_option).click().perform()

            time.sleep(2)

            assert "teams/1" in driver.current_url, "❌ 개발 1팀 선택 실패"
            print("✅ 개발 1팀 선택 성공")
            driver.save_screenshot("팀 피드 페이지-콤보박스-개발1팀 선택-성공.png")

        except NoSuchElementException as e:
            assert False, f"팀 피드 페이지-오픈-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"팀 피드 페이지-오픈-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드 페이지-오픈-실패 (알 수 없는 오류) : {e}"


    @pytest.mark.skip(reason="테스트 통과해서 생략")
    def test_profile_edit(self, driver: WebDriver):
        try:
            driver.find_element(By.CSS_SELECTOR, self.GNB_SELECTOR)
            wait = ws(driver, 10)
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.GNB_SELECTOR)))
            
            team_feed_page = TeamFeedPage(driver)
            team_feed_page.team_feed_click()
            
            wait.until(EC.url_contains("teams"))

            team_feed_page.combobox_btn_click()

            # "개발 1팀" 선택           
            team_option = wait.until(EC.visibility_of_element_located((By.XPATH, self.COMBOBOX_XPATH)))
            ActionChains(driver).move_to_element(team_option).click().perform()

            time.sleep(2)

            # 프로필 정보 수정
            team_feed_page.profile_edit_click()

            edit_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.PROFILE_SELECTOR)))
            assert edit_page.is_displayed(), "❌ 음식 성향 수정화면 이동 실패"
            print("✅ 음식 성향 수정화면 이동 성공")

        except NoSuchElementException as e:
            assert False, f"팀 피드 페이지-오픈-실패 (요소를 찾을 수 없음) : {e}"

        except TimeoutException as e:
            assert False, f"팀 피드 페이지-오픈-실패 (시간 초과) : {e}"

        except Exception as e:
            assert False, f"❌ 팀 피드 페이지-오픈-실패 (알 수 없는 오류) : {e}"