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
#@pytest.mark.skip()
class TestHistoryPage:

    def add_new_history(self, driver):
        history_page = HistoryPage(driver)
        history_page.click(HistoryPage.eat_alone_home_btn)
        history_page.click(HistoryPage.eat_alone_home_combobox)
        history_page.click(HistoryPage.eat_alone_home_category_Korean)
        history_page.click(HistoryPage.eat_alone_home_choose_btn)
        history_page.click(HistoryPage.eat_alone_home_accept_recommend)
        return history_page

    def navigate_to_history(self, driver):
        history_page = HistoryPage(driver)
        history_page.click(HistoryPage.history_btn)
        WebDriverWait(driver, 10).until(EC.url_contains("history"))
        return history_page

    def test_history_001(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
        except Exception as e:
            
            assert False, "히스토리 페이지 진입 테스트 실패"

    def test_history_002(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.back_btn)
            WebDriverWait(driver,10).until_not(EC.url_contains("history"))
        except Exception as e:
            print(f"뒤로가기 버튼 누르기 실패")
            assert False
        assert "history" != driver.current_url, "아직 history 탭에 남아있음"

    
    def test_history_003(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            GNB_name = history_page.text(HistoryPage.GNB_history)
        except Exception as e:
            assert False , "GNB 이름 찾기 실패"
        assert GNB_name == "추천 히스토리" , "GNB 이름이 '추천 히스토리'가 아님"

    
    def test_history_004(self, driver: WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            title = history_page.text(HistoryPage.history_title)
        except Exception as e:
            assert False, "추천 받았던 메뉴들이에요! 가 미노출"
        assert "추천 받았던 메뉴들이에요!" in title , "추천 받았던 메뉴들이에요! 가 다르게 노출됨"
    
    def test_history_005(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            btn = history_page.text(HistoryPage.review_register_btn)
        except Exception as e:
            assert False, "추천 후기 등록하기 버튼 탐색 실패"
        assert "추천 후기 등록" in btn, "추천 후기 등록 버튼 미노출"

    def test_history_006(self,driver:WebDriver):
        try:
            history_page = self.add_new_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.is_displayed(HistoryPage.review_tab)
            time.sleep(5)
        except Exception as e:
            assert False, "후기 등록 탭 탐색 실패"
        assert result == True, "후기 등록 탭 미노출"

    
    def test_history_007(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            review_title = history_page.text(HistoryPage.GNB_review)
        except Exception as e:
            assert False, "후기 등록하기 GNB 탐색 실패"
        assert "후기 등록하기" in review_title, "후기 등록 GNB 미노출"

    
    def test_history_008(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            radio_alone = history_page.text(HistoryPage.eat_alone)
            radio_group = history_page.text(HistoryPage.eat_group)
            radio_together = history_page.text(HistoryPage.eat_together)
        except Exception as e:
            assert False, "라디오 버튼 탐색 실패"
        assert radio_alone == "혼밥", "혼밥 라디오 버튼 미노출"
        assert radio_group == "그룹", "그룹 라디오 버튼 미노출"
        assert radio_together == "회식", "회식 라디오 버튼 미노출"

    
    def test_history_009(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.is_displayed(HistoryPage.review_img_is_null)
        except Exception as e:
            assert False, "이미지 영역 미노출"
        assert result == True, "이미지 영역에 무언가 들어있음"

    def test_history_010(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.send_keys(HistoryPage.review_img_input, HistoryPage.image_path)
            src = history_page.get_attribute(HistoryPage.review_img, "src")
            result = is_similar(src, HistoryPage.image_path)
        except Exception as e:
            assert False, "이미지 비교 실패"
        assert result > 0.9, "이미지가 다름"
        
    
    def test_history_011(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            menu_list = history_page.menu_list()
            history_menu_name = menu_list[0][2]
            history_page.click(HistoryPage.review_register_btn)
            value = history_page.get_attribute(HistoryPage.review_menu, "value")
        except Exception as e:
            assert False, "히스토리 메뉴명 또는 후기 메뉴명 탐색 실패"
        assert history_menu_name == value, "히스토리 메뉴명과 후기 메뉴명이 다름"

    def test_history_012(self,driver:WebDriver):
        try:
            history_page = self.add_new_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.is_displayed(HistoryPage.review_category)
        except Exception as e:
            assert False, "카테고리 탐색 실패"
        assert result == True, "카테고리 미노출"
    
    def test_history_013(self,driver:WebDriver):
        try:
            history_page = self.add_new_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.is_displayed(HistoryPage.review_comment)
        except Exception as e:
            assert False, "후기 입력란 감지 실패"
        assert result == True, "후기 입력란 감지 실패"
    
    def test_history_014(self,driver:WebDriver):
        try:
            history_page = self.add_new_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            result = history_page.get_attribute(HistoryPage.review_comment, "placeholder")
        except Exception as e:
            assert False, "후기 입력란 placeholder 미감지"
        assert "후기를 입력해주세요." in result, "후기 입력 placeholder이 다르게 노출됨"

    def test_history_015(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            lenth = len(history_page.texts(HistoryPage.review_star_gray))            
        except Exception as e:            
            assert False, "별점 탐색 실패"
        assert lenth == 5, "칠해지지 않은 별점 수가 5개가 아님"

    def test_history_016(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            class_attr = history_page.get_attribute(HistoryPage.eat_alone_radio, "class")
            if "disabled:cursor-not-allowed" in class_attr:
                assert True
            else:
                assert False, "식사 유형 활성화됨"
        except Exception as e:
            print("TC016 실패")
            assert False

    def test_history_017(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.send_keys(HistoryPage.review_comment, "123")
            result = history_page.get_attribute(HistoryPage.review_comment, "value")
        except Exception as e:
            assert False
        assert result == "123", "동일한 값이 아님"
    
    def test_history_018(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)

            history_page.send_keys(HistoryPage.review_comment, "a" * 500)
            result = history_page.get_attribute(HistoryPage.review_comment, "value")
        except Exception as e:
            assert False
        assert result != "a" * 500, "후기에 500자 전부 입력됨"

    
    def test_history_019(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            
            history_page.click(HistoryPage.review_stars_3)
            result = len(history_page.texts(HistoryPage.review_star_yellow))            
        except Exception as e:
            assert False, "별점 불러오기 실패"
        assert result == 3, "별점이 3개가 아님"
    
    def test_history_020(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.click(HistoryPage.review_submit_btn)
            result = history_page.is_displayed(HistoryPage.review_tab)
            assert result == True, "후기 등록 실패했으나 탭이 닫힘"
        except Exception as e:
            assert False

    
    def test_history_021(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.click(HistoryPage.review_submit_btn)
            warning_text = history_page.is_displayed(HistoryPage.review_img_warning)                      
        except Exception as e:
            assert False
        assert warning_text == True, "이미지 경고 메시지 미노출"
    
    def test_history_022(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.click(HistoryPage.review_submit_btn)
            warning_text = history_page.is_displayed(HistoryPage.review_text_warning)
        except Exception as e:
            assert False
        assert warning_text == True, "리뷰 이미지후기 입력 경고 메시지 미노출"  
    
    def test_history_023(self,driver:WebDriver):
        try:
            history_page = self.navigate_to_history(driver)
            history_page.click(HistoryPage.review_register_btn)
            history_page.click(HistoryPage.review_submit_btn)
            warning_text = history_page.is_displayed(HistoryPage.review_star_warning)          
        except Exception as e:
            assert False
        assert warning_text == True, "별점 입력 경고 메시지 미노출"
    
    def test_history_024(self,driver:WebDriver):
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

        
    def test_history_025(self,driver:WebDriver):
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
            