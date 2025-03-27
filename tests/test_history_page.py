#test_history_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random
import pytest
from pages.history_page import HistoryPage

'''
참고
menu_list의 출력 예시
[['회식', '기타', '랍스터롤', '44.0 %'], 
['회식', '패스트푸드', '머핀', '44.0 %'], 
['그룹', '아시안', '해물쌀국수', '53.0 %'], 
['그룹', '분식', '날치알김밥', '52.0 %'], 
['그룹', '일식', '다시마키타마고', '52.0 %'], 
['혼밥', '양식', '토르텔리니', '52.0 %'], 
['혼밥', '중식', '사천탕면', '53.0 %'], 
['혼밥', '한식', '동태탕', '52.0 %']]
'''



@pytest.mark.usefixtures("login_driver")
@pytest.mark.skip()
class TestMyPage:

    category_list = [
    (0, "회식", "기타"),
    (1, "회식", "패스트푸드"),
    (2, "그룹", "아시안"),
    (3, "그룹", "분식"),
    (4, "그룹", "일식"),
    (5, "혼밥", "양식"),
    (6, "혼밥", "중식"),
    (7, "혼밥", "한식")]

    def navigate_to_history(self, driver):
        history_page = HistoryPage(driver)
        history_page.click(HistoryPage.history_btn)
        WebDriverWait(driver, 10).until(EC.url_contains("history"))
        return history_page

    @pytest.mark.skip()
    def test_history_001(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
        except Exception as e:
            print(f"히스토리 페이지 진입 테스트 실패")
            assert False

    @pytest.mark.skip()
    def test_history_002(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.back_btn)
            WebDriverWait(driver,10).until_not(EC.url_contains("history"))
            assert "history" != driver.current_url, "아직 history 탭에 남아있음"
        except Exception as e:
            print(f"뒤로가기 버튼 누르기 실패")
            assert False

    @pytest.mark.skip()

    def test_history_003(self, driver: WebDriver):

        try:
            history_page = self.navigate_to_history(driver)
            GNB_name = history_page.text(HistoryPage.GNB_history)
            assert GNB_name == "추천 히스토리" , "GNB 이름이 '추천 히스토리'가 아님"
        except Exception as e:
            print(f"GNB 이름 찾기 실패")
            assert False

    @pytest.mark.skip()
    def test_history_004(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            title = history_page.text(HistoryPage.history_title)
            assert "추천 받았던 메뉴들이에요!" in title , "추천 받았던 메뉴들이에요! 가 다르게 노출됨"
        except Exception as e:
            print(f"추천 받았던 메뉴들이에요! 가 미노출")
            assert False

    @pytest.mark.skip()
    def test_history_005(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            menu_list = history_page.menu_list()
            print(menu_list[0])
            assert len(menu_list) == 8 , "8개보다 적거나 많음"
        except Exception as e:
            print(f"메뉴들을 찾아내지 못함")
            assert False

    



    @pytest.mark.skip()
    @pytest.mark.parametrize("index, expected_main, expected_sub", category_list)
    def test_history_006_008_010_012_014_016_018_020(self,driver: WebDriver, index, expected_main, expected_sub):  #6,8,10,12,14,16,18,20번 TC
        try:
            history_page = self.navigate_to_history(driver)
            menu_list = history_page.menu_list()
            assert expected_main == menu_list[index][0], f"{index}번째 메인 카테고리가 다름"
            assert expected_sub == menu_list[index][1], f"{index}번째 서브 카테고리가 다름"
        except Exception as e:
            print(f"{index}번 오류: {e}")
            assert False

    @pytest.mark.skip()
    def test_history_022(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            
            btn = history_page.text(HistoryPage.review_register_btn)
            assert "추천 후기 등록" in btn, "추천 후기 등록 버튼이 없음"
        except Exception as e:
            print("추천 후기 등록하기 버튼 미노출")
            assert False

    @pytest.mark.skip()
    def test_history_023(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            button = history_page.review_register_btn()
            button.click()            
            #assert len(GNB) > 0 , "후기 등록하기 페이지가 열리지 않음"
        except Exception as e:
            print("후기 등록 탭 미노출")
            assert False
