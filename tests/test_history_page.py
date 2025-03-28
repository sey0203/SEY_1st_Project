#test_history_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
import time
import random
import pytest
from pages.history_page import HistoryPage
import os
from utils.image_is_similar import is_similar


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
class TestHistoryPage:

    category_list = [
    (0, "회식", "기타"),
    (1, "회식", "패스트푸드"),
    (2, "그룹", "아시안"),
    (3, "그룹", "분식"),
    (4, "그룹", "일식"),
    (5, "혼밥", "양식"),
    (6, "혼밥", "중식"),
    (7, "혼밥", "한식")]

    meal_type = ["혼밥", "그룹", "회식"]

    def navigate_to_history(self, driver):
        history_page = HistoryPage(driver)
        history_page.click(HistoryPage.history_btn)
        WebDriverWait(driver, 10).until(EC.url_contains("history"))
        return history_page

    
    def test_history_001(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
        except Exception as e:
            print(f"히스토리 페이지 진입 테스트 실패")
            assert False

    
    def test_history_002(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.back_btn)
            WebDriverWait(driver,10).until_not(EC.url_contains("history"))
            assert "history" != driver.current_url, "아직 history 탭에 남아있음"
        except Exception as e:
            print(f"뒤로가기 버튼 누르기 실패")
            assert False

    
    def test_history_003(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            GNB_name = history_page.text(HistoryPage.GNB_history)
            assert GNB_name == "추천 히스토리" , "GNB 이름이 '추천 히스토리'가 아님"
        except Exception as e:
            print(f"GNB 이름 찾기 실패")
            assert False

    
    def test_history_004(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            title = history_page.text(HistoryPage.history_title)
            assert "추천 받았던 메뉴들이에요!" in title , "추천 받았던 메뉴들이에요! 가 다르게 노출됨"
        except Exception as e:
            print(f"추천 받았던 메뉴들이에요! 가 미노출")
            assert False

    
    def test_history_005(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            menu_list = history_page.menu_list()
            assert len(menu_list) == 8 , "8개보다 적거나 많음"
        except Exception as e:
            print(f"메뉴들을 찾아내지 못함")
            assert False

    
    @pytest.mark.parametrize("index, expected_main, expected_sub", category_list)
    def test_history_006_013(self,driver: WebDriver, index, expected_main, expected_sub):  #6번 ~ 13번 TC
        try:
            history_page = self.navigate_to_history(driver)
            menu_list = history_page.menu_list()
            assert expected_main == menu_list[index][0], f"{index}번째 메인 카테고리가 다름"
            assert expected_sub == menu_list[index][1], f"{index}번째 서브 카테고리가 다름"
        except Exception as e:
            print(f"{index}번 오류: {e}")
            assert False

    
    def test_014(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            
            btn = history_page.text(HistoryPage.review_register_btn)
            assert "추천 후기 등록" in btn, "추천 후기 등록 버튼 미노출"
        except Exception as e:
            print("추천 후기 등록하기 버튼 탐색 실패")
            assert False

    
    def test_015(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.is_displayed(HistoryPage.review_tab)
            assert result == True, "후기 등록 탭 미노출"
        except Exception as e:
            print("후기 등록 탭 탐색 실패")
            assert False

    
    def test_history_016(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            review_title = history_page.text(HistoryPage.GNB_review)
            assert "후기 등록하기" in review_title, "후기 등록 GNB 미노출"
        except Exception as e:
            print("후기 등록하기 GNB 탐색 실패")
            assert False

    
    def test_history_017(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            radio_alone = history_page.text(HistoryPage.eat_alone)
            radio_group = history_page.text(HistoryPage.eat_group)
            radio_together = history_page.text(HistoryPage.eat_together)
            assert radio_alone == "혼밥", "혼밥 라디오 버튼 미노출"
            assert radio_group == "그룹", "그룹 라디오 버튼 미노출"
            assert radio_together == "회식", "회식 라디오 버튼 미노출"
        except Exception as e:
            print("라디오 버튼 탐색 실패")
            assert False

    
    def test_history_018(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.is_displayed(HistoryPage.review_img_is_null)
            assert result == True, "이미지 영역에 무언가 들어있음"
        except Exception as e:
            print("이미지 영역 미노출")
            assert False

    
    def test_history_019(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.send_keys(HistoryPage.review_img_input, HistoryPage.image_path)
            src = history_page.get_attribute(HistoryPage.review_img, "src")
            result = is_similar(src, HistoryPage.image_path)
            assert result > 0.9, "이미지가 다름"
        except Exception as e:
            print("이미지 비교 실패")
            assert False
        
    
    def test_history_020(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            menu_list = history_page.menu_list()
            history_menu_name = menu_list[0][2]
            history_page.click(HistoryPage.review_register_btn)
            value = history_page.get_attribute(HistoryPage.review_menu, "value")
            assert history_menu_name == value, "히스토리 메뉴명과 후기 메뉴명이 다름"

        except Exception as e:
            print("히스토리 메뉴명 또는 후기 메뉴명 탐색 실패")
            assert False


    def test_history_021(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.is_displayed(HistoryPage.review_category)
            assert result == True, "카테고리 미노출"

        except Exception as e:
            print("카테고리 탐색 실패")
            assert False
    

    def test_history_022(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.is_displayed(HistoryPage.review_comment)
            assert result == True, print("후기 입력란 감지 실패")

        except Exception as e:
            assert False
    

    def test_history_023(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.get_attribute(HistoryPage.review_comment, "placeholder")
            assert "후기를 입력해주세요." in result, print("후기 입력 placeholder이 다르게 노출됨")
        except Exception as e:
            assert False        


    def test_history_024(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)

            lenth = len(history_page.texts(HistoryPage.review_star_gray))
            assert lenth == 5, "칠해지지 않은 별점 수가 5개가 아님"
        except Exception as e:
            print("별점 탐색 실패")
            assert False


    def test_history_025(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            class_attr = history_page.get_attribute(HistoryPage.eat_alone_radio, "class")
            if "disabled:cursor-not-allowed" in class_attr:
                assert True
            else:
                print("식사 유형활성화됨")
                assert False

        except Exception as e:
            print("TC025 실패")
            assert False


    #26번부터 30번까지는 테스트 데이터가 필요하므로 우선 스킵



    def test_history_031(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)

            history_page.send_keys(HistoryPage.review_comment, "123")
            result = history_page.get_attribute(HistoryPage.review_comment, "value")
            assert result == "123", print("동일한 값이 아님")
        except Exception as e:
            assert False

    
    def test_history_032(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)

            history_page.send_keys(HistoryPage.review_comment, "a" * 500)
            result = history_page.get_attribute(HistoryPage.review_comment, "value")
            assert result != "a" * 500, print("후기에 500자 전부 입력됨")
        except Exception as e:
            assert False

    
    def test_history_033(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            
            history_page.click(HistoryPage.review_stars_3)
            result = len(history_page.texts(HistoryPage.review_star_yellow))
            assert result == 3,print("별점이 3개가 아님")
        except Exception as e:
            assert False


    
    def test_history_034(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.click(HistoryPage.review_submit_btn)
            result = history_page.is_displayed(HistoryPage.review_tab)
            assert result == True, "후기 등록 실패했으나 탭이 닫힘"
        except Exception as e:
            assert False

    
    def test_history_035(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.click(HistoryPage.review_submit_btn)

            warning_text = history_page.is_displayed(HistoryPage.review_img_warning)
            assert warning_text == True, print("이미지 경고 메시지 미노출")            
        except Exception as e:
            assert False

    
    def test_history_036(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.click(HistoryPage.review_submit_btn)

            warning_text = history_page.is_displayed(HistoryPage.review_text_warning)
            assert warning_text == True, print("후기 입력 경고 메시지 미노출")            
        except Exception as e:
            assert False

    
    def test_history_037(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.click(HistoryPage.review_submit_btn)

            warning_text = history_page.is_displayed(HistoryPage.review_star_warning)
            assert warning_text == True, print("별점 입력 경고 메시지 미노출")            
        except Exception as e:
            assert False

@pytest.mark.usefixtures("login_driver_second")
@pytest.mark.skip()
class TestHistoryPage_Second:

    def add_new_history(self, driver):
        history_page = HistoryPage(driver)
        history_page.click(HistoryPage.eat_alone_home_btn)
        history_page.click(HistoryPage.eat_alone_home_combobox)
        history_page.click(HistoryPage.eat_alone_home_category_Korean)
        history_page.click(HistoryPage.eat_alone_home_choose_btn)
        history_page.click(HistoryPage.eat_alone_home_accept_recommend)
        return history_page

    
    def test_history_038(self,driver:WebDriver):
        try:
            history_page = self.add_new_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.send_keys(HistoryPage.review_img_input, HistoryPage.image_path)
            history_page.click(HistoryPage.review_stars_3)
            history_page.send_keys(HistoryPage.review_comment, "123")
            history_page.click(HistoryPage.review_submit_btn)            
            try:
                history_page.click(HistoryPage.GNB_history)
            except ElementClickInterceptedException:
                print("리뷰 작성 후 히스토리탭 이동 안함")
                assert False
        except Exception as e:
            print("리뷰 작성 후 히스토리탭 이동 실패")
            assert False

        
    def test_history_039(self,driver:WebDriver):
        try:
            history_page = self.add_new_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.send_keys(HistoryPage.review_img_input, HistoryPage.image_path)
            history_page.click(HistoryPage.review_stars_3)
            history_page.send_keys(HistoryPage.review_comment, "123")
            history_page.click(HistoryPage.review_submit_btn)
            time.sleep(0.1) #후기 등록 버튼이 변경되는 네트워크 시간을 기다림
            result = history_page.text(HistoryPage.review_register_btn)
            assert "완료" in result, "후기 등록 완료 버튼이 노출되지 않음"
        except Exception as e:
            print("후기 등록 완료 버튼이 노출되지 않음")
            