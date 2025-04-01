#test_my_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
import time
import random
import pytest
from pages.my_page import MyPage
from utils.image_is_similar import is_similar
import math



@pytest.mark.usefixtures("login_driver_second")
#@pytest.mark.skip()
class TestMyPage:
    
    def navigate_to_my_page(self, driver):
        my_page = MyPage(driver)
        my_page.click(MyPage.my_feed_btn)
        WebDriverWait(driver, 10).until(EC.url_contains("my"))
        return my_page
                            
    def precondition_ai_recommend(self,driver:WebDriver):
        my_page = MyPage(driver)
        my_page.click(MyPage.add_AI_recommend)
        my_page.click(MyPage.add_AI_category)
        element_list = my_page.elements(MyPage.add_AI_categories_list)
        element_list[7].click()
        my_page.click(MyPage.add_AI_btn)
        my_page.click(MyPage.add_AI_accept_btn)
        my_page.click(MyPage.history_add_review)
        my_page.send_keys(MyPage.add_review_img,MyPage.image_path)
        my_page.send_keys(MyPage.comment,"123")
        my_page.click(MyPage.star_3)
        my_page.click(MyPage.review_submit_btn)
        my_page.click(MyPage.my_feed_btn)
        return my_page
    
    def test_my_001(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.text(MyPage.my_feed_btn)
        except TimeoutException:
            assert False, "URL에 'my'가 포함되지 않았습니다. "
        except NoSuchElementException:
            assert False, "개인 피드 탭이 존재하지 않습니다."
        except Exception as e:
            assert False, "test_my_001 예외 발생"
    
    def test_my_002(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.back_btn)
            WebDriverWait(driver,10).until_not(EC.url_contains("my"))
        except TimeoutException:
            assert False , "test_my_002 뒤로가기가 눌리지 않음"
        except NoSuchElementException:
            assert False , "test_my_002 뒤로가기 버튼이 존재하지 않음"
        except Exception as e:
            assert False , "test_my_002 예외 발생"
    
    def test_my_003(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            result = my_page.text(MyPage.GNB_my_page)
            assert result == "내 피드"
        except TimeoutException:
            assert False , "test_my_003 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_003  존재하지 않음"
        except AssertionError:
            assert False , "test_my_003 텍스트 불일치"
        except Exception as e:
            assert False , "test_my_003 예외 발생"
    
    def test_my_004(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            section = my_page.is_displayed(MyPage.my_profile_section)
        except TimeoutException:
            assert False , "test_my_004 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_004  존재하지 않음"
        except Exception as e:
            assert False , "test_my_004 예외 발생"
        assert section == True, "섹션 위치가 안보임"
    
    def test_my_005(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            status = my_page.text(MyPage.my_status)
            
        except TimeoutException:
            assert False , "test_my_005 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_005  존재하지 않음"
        except Exception as e:
            assert False , "test_my_005 예외 발생"
        assert "통계" in status , "내 피드 통계 미노출"
    
    @pytest.mark.flaky(reruns=3, reruns_delay=0.5)
    def test_my_006(self, driver:WebDriver):
        try:
            my_page = self.precondition_ai_recommend(driver)
            title = my_page.text(MyPage.my_add_history_menu)
            main = my_page.text(MyPage.my_add_history_eat_main_type)   
            sub = my_page.text(MyPage.my_add_history_eat_sub_type)
            sub2 = my_page.text(MyPage.my_add_history_eat_sub_2_type)
            src = my_page.get_attribute(MyPage.my_add_history_pic,"src")
            similar_result = is_similar(src, MyPage.my_add_image_path)
            stars = my_page.texts(MyPage.my_add_history_star)
            count_star = stars[:5].count('★')
            btn_check = my_page.is_displayed(MyPage.my_add_history_btn)
        except TimeoutException:
            assert False , "test_my_006 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_006  존재하지 않음"
        except Exception as e:
            assert False , "test_my_006 예외 발생"
        assert "내가 먹은 메뉴" in title, "내가 먹은 메뉴 타이틀 미노출"
        assert main == "회식", "내가 먹은 메뉴 - 메인 카테고리 잘못된 값 노출"
        assert sub == "기타", "내가 먹은 메뉴 - 서브 카테고리 잘못된 값 노출"
        assert sub2 == "AI 추천", "내가 먹은 메뉴 - 서브 2 카테고리 잘못된 값 노출"
        assert similar_result == True, "내가 먹은 메뉴 - 동일하지 않은 이미지 노출"
        assert count_star == 3, "내가 먹은 메뉴 - 별점 잘못된 값 노출"
        assert btn_check == True, "내가 먹은 메뉴 - 같은 메뉴 먹기 버튼 미노출"
    
    def test_my_007(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_profile_btn)
        except TimeoutException:
            assert False , "test_my_007 작동 않음"
        except NoSuchElementException:
            assert False , "test_my_007  존재하지 않음"
        except Exception as e:
            assert False , "test_my_007 예외 발생"
        assert my_page.is_displayed(MyPage.my_add_review_tab) == True, "탭이 노출되지 않음"
    
    def test_my_008(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_profile_btn)
            profile_gnb = my_page.text(MyPage.my_profile_gnb)
            profile_back_btn = my_page.is_displayed(MyPage.my_profile_back_btn)
        except TimeoutException:
            assert False , "test_my_008 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_008  존재하지 않음"
        except Exception as e:
            assert False , "test_my_008 예외 발생"
        assert profile_gnb == "프로필 정보 수정", "프로필 정보 수정 GNB 미노출"
        assert profile_back_btn == True, "프로필 정보 수정 뒤로가기 버튼 미노출"
    
    def test_my_009(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_profile_btn)
            profile_edit_title = my_page.text(MyPage.my_profile_edit_title)
            profile_img = my_page.get_attribute(MyPage.my_profile_img,"src")
            similar = is_similar(profile_img,MyPage.default_profile)
        except TimeoutException:
            assert False , "test_my_009 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_009  존재하지 않음"
        except Exception as e:
            assert False , "test_my_009 예외 발생"
        assert profile_edit_title == "프로필 이미지 수정" , "프로필 정보 수정 - 프로필 이미지 수정 타이틀 잘못 노출됨"
        assert similar == True, "프로필이 기본 프로필이 아님"
    
    def test_my_010(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_profile_btn)
            my_page.send_keys(MyPage.my_profile_img_input,MyPage.image_path)
            profile_img = my_page.get_attribute(MyPage.my_profile_img,"src")
            similar = is_similar(profile_img,MyPage.image_path)
        except TimeoutException:
            assert False , "test_my_010 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_010  존재하지 않음"
        except Exception as e:
            assert False , "test_my_010 예외 발생"
        assert similar == True, "프로필 정보 수정 - 이미지 변경이 안됨"
    
    
    def test_my_011(self, driver: WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_profile_btn)
            time.sleep(0.5)
            my_page.move_sliders(MyPage.sliders,MyPage.sliders_size,MyPage.sliders_size_sub,0.0,0.5,0.9)
            actual_list  = my_page.texts(MyPage.sliders_amount)
            my_page.click(MyPage.my_profile_submit_btn)
            warn = len(my_page.texts(MyPage.my_add_desc_list))
            expected_list = ['0.0','0.5','0.9']
        except Exception as e:
            assert False, f"test_my_011 예외 발생: {e}"
        for i, (e, a) in enumerate(zip(expected_list, actual_list)):
            diff = abs(float(e) - float(a))
            assert diff <= 0.1, "값이 다름 "
        assert warn == 3, "맛에 대한 성향 슬라이더 경고 메세지 일부 미노출"
  
    def test_my_012(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_profile_btn)
            time.sleep(0.5)
            my_page.move_sliders(MyPage.sliders,MyPage.sliders_size,MyPage.sliders_size_sub,2.0,4.0,4.5)
            actual_list = my_page.texts(MyPage.sliders_amount)
            expected_list = ['2.0','4.0','4.5']
        except TimeoutException:
            assert False , "test_my_012 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_012  존재하지 않음"
        except Exception as e:
            assert False , "test_my_012 예외 발생"
        for i, (e, a) in enumerate(zip(expected_list, actual_list)):
            diff = abs(float(e) - float(a))
            assert diff <= 0.1, "값이 다름"
            
    def test_my_013(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_profile_btn)
            my_page.clear(MyPage.my_profile_prefer)
            my_page.clear(MyPage.my_profile_hate)
            prefer_placeholder = my_page.get_attribute(MyPage.my_profile_prefer,"placeholder")
            hate_placeholder = my_page.get_attribute(MyPage.my_profile_hate,"placeholder")
        except TimeoutException:
            assert False , "test_my_013 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_013  존재하지 않음"
        except Exception as e:
            assert False , "test_my_013 예외 발생"
        assert "좋아하는 음식 성향을 이야기해주세요!" in prefer_placeholder, "placeholder이 다르게 노출됨"
        assert "싫어하는 음식 성향을 이야기해주세요!" in hate_placeholder, "placeholder이 다르게 노출됨"
    
    def test_my_014(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_profile_btn)
            my_page.clear(MyPage.my_profile_prefer)
            my_page.clear(MyPage.my_profile_hate)
            my_page.send_keys(MyPage.my_profile_prefer,"123")
            my_page.send_keys(MyPage.my_profile_hate,"456")
            my_page.click(MyPage.my_profile_submit_btn)
            prefer_value = my_page.get_attribute(MyPage.my_profile_prefer,"value")
            hate_value = my_page.get_attribute(MyPage.my_profile_hate,"value")
            warn_count = len(my_page.elements(MyPage.my_profile_warn))
        except TimeoutException:
            assert False , "test_my_014 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_014  존재하지 않음"
        except Exception as e:
            assert False , "test_my_014 예외 발생"
        assert "123" == prefer_value, "프로필 수정 좋아하는 음식 성향에 값이 잘못 들어가짐"
        assert "456" == hate_value, "프로필 수정 싫어하는 음식 성향에 값이 잘못 들어가짐"
        assert warn_count == 2 , "프로필 수정 경고가 덜 노출됨"
    
    def test_my_015(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_profile_btn)
            my_page.clear(MyPage.my_profile_prefer)
            my_page.clear(MyPage.my_profile_hate)
            my_page.send_keys(MyPage.my_profile_prefer,"한식에서 매콤한 음식을 좋아합니다.")
            my_page.send_keys(MyPage.my_profile_hate,"중식에서 느끼한 음식을 싫어합니다.")
            my_page.click(MyPage.my_profile_submit_btn)
            complete_status = my_page.is_displayed(MyPage.my_profile_edit_complete)
            list = my_page.texts(MyPage.my_profile_feed)
        except TimeoutException:
            assert False , "test_my_015 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_015  존재하지 않음"
        except Exception as e:
            assert False , "test_my_015 예외 발생"
        assert complete_status == True, "프로필 수정 완료 미노출"
        assert list[0] == "한식에서 매콤한 음식을 좋아합니다.", "좋아하는 성향 변경 미반영"
        assert list[1] == "중식에서 느끼한 음식을 싫어합니다.", "싫어하는 성향 변경 미반영"
    
    def test_my_016(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu)
            result = my_page.is_displayed(MyPage.my_add_review_tab)
        except TimeoutException:
            assert False , "test_my_016 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_016  존재하지 않음"
        except Exception as e:
            assert False , "test_my_016 예외 발생"
        assert result == True, "리뷰탭 미노출"

    
    def test_my_017(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu)
            result_GNB = my_page.is_displayed(MyPage.my_add_review_GNB)
            result_back_btn = my_page.is_displayed(MyPage.my_add_review_back_btn)
            text_eat_alone = my_page.text(MyPage.my_add_eat_alone)
            text_eat_group = my_page.text(MyPage.my_add_eat_group)
            text_eat_together = my_page.text(MyPage.my_add_eat_together)
        except TimeoutException:
            assert False , "test_my_017 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_017  존재하지 않음"
        except Exception as e:
            assert False , "test_my_017 예외 발생"
        assert result_GNB == True , "리뷰 추가 GNB 미노출"
        assert result_back_btn == True , " 리뷰 뒤로가기 버튼 미노출"
        assert text_eat_alone == "혼밥", " 혼밥 텍스트 미노출"
        assert text_eat_group == "그룹", " 그룹 텍스트 미노출"
        assert text_eat_together == "회식", "회식 텍스트 미노출"
    
    def test_my_018(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu)
            review_title = my_page.is_displayed(MyPage.my_add_review_title)
            review_img_is_null = my_page.is_displayed(MyPage.my_add_review_img_is_null)
            review_img_btn = my_page.is_displayed(MyPage.my_add_review_img_btn)
        except TimeoutException:
            assert False , "test_my_018 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_018  존재하지 않음"
        except Exception as e:
            assert False , "test_my_018 예외 발생"
        assert review_title == True , "리뷰 이미지 타이틀 미노출"
        assert review_img_is_null == True , "리뷰 이미지 빈공간이 노출되지 않음"
        assert review_img_btn == True , "리뷰 이미지 추가 버튼이 노출되지 않음"

    
    def test_my_019(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu)
            menu_title = my_page.is_displayed(MyPage.my_add_menu_title)
            menu_name_placeholder = my_page.get_attribute(MyPage.my_add_menu_name,"placeholder")
        except TimeoutException:
            assert False , "test_my_019 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_019  존재하지 않음"
        except Exception as e:
            assert False , "test_my_019 예외 발생"
        assert menu_title == True , "메뉴 명 타이틀이 미노출"
        assert menu_name_placeholder == "메뉴 명을 입력해주세요." , "메뉴명 placeholder이 다르게 노출됨"

    
    def test_my_020(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu)
            my_page.click(MyPage.my_add_category_name)
            category_title = my_page.text(MyPage.my_add_category_title)
            category_name = my_page.is_displayed(MyPage.my_add_category_name)
            category_name_text = my_page.text(MyPage.my_add_category_text)
            category_list = my_page.texts(MyPage.my_add_category_list_name)
            expected_list = ['한식', '중식', '양식', '일식', '분식', '아시안', '패스트푸드', '기타']

        except TimeoutException:
            assert False , "test_my_020 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_020  존재하지 않음"
        except Exception as e:
            assert False , "test_my_020 예외 발생"
        assert category_title == "카테고리"
        assert category_name == True
        assert "음식 카테고리를 설정" in category_name_text
        assert category_list == expected_list

    
    def test_my_021(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu) 
            comment_title = my_page.text(MyPage.my_add_comment_title)
            comment_name = my_page.get_attribute(MyPage.my_add_comment_name, "placeholder")

        except TimeoutException:
            assert False , "test_my_021 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_021  존재하지 않음"
        except Exception as e:
            assert False , "test_my_021 예외 발생"
        assert comment_title == "후기" , "후기 타이틀이 다르게 노출됨"
        assert "후기를 입력해주세요." in comment_name , "후기 입력란 placeholder 오류"

    
    def test_my_022(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu)
            star_title = my_page.text(MyPage.my_add_star_title)
            star_rate = my_page.texts(MyPage.my_add_star_rate)
        except TimeoutException:
            assert False , "test_my_022 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_022 존재하지 않음"
        except Exception as e:
            assert False , "test_my_022 예외 발생"
        assert star_title == "별점", "후기 별점이 다르게 노출됨"
        assert len(star_rate) == 5 , "별점 수가 5개보다 많거나 적음"

    
    def test_my_023(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu)
            is_alone_clicked = my_page.get_attribute(MyPage.my_add_eat_alone_radio,"data-state")
            is_group_clicked = my_page.get_attribute(MyPage.my_add_eat_group_radio,"data-state")
            is_together_clicked = my_page.get_attribute(MyPage.my_add_eat_together_radio,"data-state")
        except TimeoutException:
            assert False , "test_my_023 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_023  존재하지 않음"
        except Exception as e:
            assert False , "test_my_023 예외 발생"
        assert is_alone_clicked == "checked", "혼밥에 체크가 안되어있음"
        assert is_group_clicked == "unchecked", "그룹에 체크가 되어있음"
        assert is_together_clicked == "unchecked", "회식에 체크가 되어있음"

    
    def test_my_024(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu) 
            my_page.click(MyPage.my_add_eat_group_click)
            with_title = my_page.text(MyPage.my_add_eat_with_title)
            with_name = my_page.get_attribute(MyPage.my_add_eat_with_name,"placeholder")
        except TimeoutException:
            assert False , "test_my_024 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_024  존재하지 않음"
        except Exception as e:
            assert False , "test_my_024 예외 발생"
        assert with_title == "같이 먹은 사람 등록", "같이 먹은 사람 등록 타이틀 미노출"
        assert with_name == "이름을 검색해주세요", "같이 먹은 사람 등록 placeholder 미노출"

    
    def test_my_025(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu) 
            my_page.click(MyPage.my_add_submit_btn)
            desc_list = my_page.texts(MyPage.my_add_desc_list)
            expected_list = ['리뷰 이미지는 필수입니다', '메뉴명은 필수입니다', '카테고리는 필수입니다', '후기는 필수입니다', '별점은 최소 1점 이상이어야 합니다']
        except TimeoutException:
            assert False , "test_my_025 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_025  존재하지 않음"
        except Exception as e:
            assert False , "test_my_025 예외 발생"
        assert desc_list[0] == expected_list[0], "리뷰 이미지 필수 여부 노출되지 않음"
        assert desc_list[1] == expected_list[1], "메뉴명 필수 여부 노출되지 않음"
        assert desc_list[2] == expected_list[2], "카테고리 필수 여부 노출되지 않음"
        assert desc_list[3] == expected_list[3], "후기 필수 여부 노출되지 않음"
        assert desc_list[4] == expected_list[4], "별점 필수 여부 노출되지 않음"

    
    def test_my_026(self, driver:WebDriver):
        try: 
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu) 
            my_page.send_keys(MyPage.my_add_review_img_input, MyPage.my_add_image_path)
            src = my_page.get_attribute(MyPage.my_add_review_img, "src")
            similar_result = is_similar(src, MyPage.my_add_image_path)
        except TimeoutException:
            assert False , "test_my_026 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_026  존재하지 않음"
        except Exception as e:
            assert False , "test_my_026 예외 발생"
        assert similar_result == True, "업로드한 이미지가 다르게 노출됨"

    
    def test_my_027(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu)
            my_page.send_keys(MyPage.my_add_menu_name,"a" * 500)
            value = my_page.get_attribute(MyPage.my_add_menu_name,"value")
        except TimeoutException:
            assert False , "test_my_027 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_027  존재하지 않음"
        except Exception as e:
            assert False , "test_my_027 예외 발생"
        assert len(value) < 500, "메뉴 명 입련란이 500자 이상 작성 가능"

    
    def test_my_028(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu)
            my_page.click(MyPage.my_add_category_name)
            category_list = my_page.elements(MyPage.my_add_category_clickable_list)
            category_list[4].click() # 분식 클릭
            category_text = my_page.text(MyPage.my_add_category_text)
        except TimeoutException:
            assert False , "test_my_028 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_028  존재하지 않음"
        except Exception as e:
            assert False , "test_my_028 예외 발생"
        assert category_text == "분식", "카테고리 변경 실패"

    
    def test_my_029(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu)
            my_page.send_keys(MyPage.my_add_comment_name,"a" * 500)
            value = my_page.get_attribute(MyPage.my_add_comment_name,"value") 
            time.sleep(3)
        except TimeoutException:
            assert False , "test_my_029 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_029  존재하지 않음"
        except Exception as e:
            assert False , "test_my_029 예외 발생"
        assert len(value) < 500, "후기 입련란이 500자 이상 작성 가능"

    
    def test_my_030(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu)
            my_page.click(MyPage.my_add_stars_3)
            gray_stars = my_page.texts(MyPage.my_add_star_rate)
            yellow_stars = my_page.texts(MyPage.my_add_star_yellow)
        except TimeoutException:
            assert False , "test_my_030 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_030  존재하지 않음"
        except Exception as e:
            assert False , "test_my_030 예외 발생"
        assert len(gray_stars) == 2, "리뷰 별점 3점으로 설정되지 않음"
        assert len(yellow_stars) == 3 , "리뷰 별점이 3점으로 설정되지 않음"

    
    @pytest.mark.flaky(reruns=3, reruns_delay=0.25)
    def test_my_031(self, driver:WebDriver):
        try:
            my_page = self.navigate_to_my_page(driver)
            my_page.click(MyPage.my_add_menu)
            my_page.send_keys(MyPage.my_add_menu_name,"123")
            my_page.send_keys(MyPage.my_add_comment_name,"123")         
            my_page.send_keys(MyPage.my_add_review_img_input,MyPage.my_add_image_path) 
            my_page.click(MyPage.my_add_stars_3)              
            my_page.click(MyPage.my_add_category_name)
            category_list = my_page.elements(MyPage.my_add_category_clickable_list)
            category_list[4].click()
            my_page.click(MyPage.my_add_submit_btn)

            status_shown = my_page.is_displayed(MyPage.my_add_review_status)
        except TimeoutException:
            assert False , "test_my_031 작동 않음" 
        except NoSuchElementException:
            assert False , "test_my_031  존재하지 않음"
        except Exception as e:
            assert False , "test_my_031 예외 발생"
        assert status_shown == True, "리뷰 등록 완료 나오지 않음"

    
    @pytest.mark.flaky(reruns=3, reruns_delay=0.25)
    def test_my_032(self, driver:WebDriver):
        try:
            my_page = self.precondition_ai_recommend(driver)
            driver.fullscreen_window()
            my_page.click(MyPage.my_add_history_btn)
            review_again_gnb = my_page.text(MyPage.my_add_review_again_GNB)
            review_again_back_btn = my_page.is_displayed(MyPage.my_add_review_back_btn)
        except TimeoutException:
            assert False , "test_my_032 작동 않음"
        except NoSuchElementException:
            assert False , "test_my_032  존재하지 않음"
        except Exception as e:
            assert False , "test_my_032 예외 발생"
        assert review_again_gnb == "또 먹은 후기 등록하기", "새로운 후기 등록하기 GNB가 나오지 않음"
        assert review_again_back_btn == True, "뒤로가기 버튼이 나오지 않음"

    
    @pytest.mark.flaky(reruns=3, reruns_delay=0.25)
    def test_my_033(self, driver:WebDriver):
        errors = []
        try:
            my_page = self.precondition_ai_recommend(driver)
            driver.fullscreen_window()
            my_page.click(MyPage.my_add_history_btn)
            eat_title = my_page.text(MyPage.my_add_eat_title)
            alone_radio = my_page.get_attribute(MyPage.my_add_eat_alone_radio,"data-state")
            group_radio = my_page.get_attribute(MyPage.my_add_eat_group_radio,"data-state")
            together_radio = my_page.get_attribute(MyPage.my_add_eat_together_radio,"data-state")
        except TimeoutException:
            assert False , "test_my_033 작동 않음"
        except NoSuchElementException:
            assert False , "test_my_033  존재하지 않음"
        except Exception as e:
            assert False , "test_my_033 예외 발생"
        if eat_title != "식사 유형":
            errors.append("또 먹은 후기 - 타이틀 잘못 노출됨")
        if alone_radio != "unchecked":
            errors.append("또 먹은 후기 - 혼밥에 체크됨")
        if group_radio != "unchecked":
            errors.append("또 먹은 후기 - 그룹에 체크됨")
        if together_radio != "checked":
           errors.append("또 먹은 후기 - 회식에 체크 안됨")
        assert not errors, " / ".join(errors)

    
    @pytest.mark.flaky(reruns=3, reruns_delay=0.25)
    def test_my_034(self, driver:WebDriver):
        try:
            my_page = self.precondition_ai_recommend(driver)
            driver.fullscreen_window()
            my_page.click(MyPage.my_add_history_btn)
            review_img_title = my_page.text(MyPage.my_add_review_title)
            review_img_btn = my_page.is_displayed(MyPage.my_add_review_img_btn)
            review_img = my_page.get_attribute(MyPage.my_add_review_img,"src")
            similar = is_similar(review_img,MyPage.image_path)
        except TimeoutException:
            assert False , "test_my_034 작동 않음"
        except NoSuchElementException:
            assert False , "test_my_034  존재하지 않음"
        except Exception as e:
            assert False , "test_my_034 예외 발생"
        assert similar == True, "또 먹은 후기 - 이미지가 유사하지 않음"
        assert review_img_btn == True, "또 먹은 후기 - 이미지가 유사하지 않음"
        assert review_img_title == "후기 사진", "또 먹은 후기 사진 타이틀이 잘못 노출됨"

    
    @pytest.mark.flaky(reruns=3, reruns_delay=0.25)
    def test_my_035(self, driver:WebDriver):
        errors = []
        try:
            my_page = self.precondition_ai_recommend(driver)
            driver.fullscreen_window()
            my_page.click(MyPage.my_add_history_btn)
            category_title = my_page.text(MyPage.my_add_category_title)
            category_text = my_page.text(MyPage.my_add_category_text)
        except TimeoutException:
            assert False , "test_my_035 작동 않음"
        except NoSuchElementException:
            assert False , "test_my_035  존재하지 않음"
        except Exception as e:
            assert False , "test_my_035 예외 발생"
        assert category_title == "카테고리", "또 먹은 후기 - 카테고리 타이틀이 잘못 노출됨"
        assert category_text == "기타", "또 먹은 후기 - 카테고리 내 텍스트 잘못 노출됨"

    
    @pytest.mark.flaky(reruns=3, reruns_delay=0.25)
    def test_my_036(self, driver:WebDriver):
        errors = []
        try:
            my_page = self.precondition_ai_recommend(driver)
            driver.fullscreen_window()
            my_page.click(MyPage.my_add_history_btn)
            comment_title = my_page.text(MyPage.my_add_comment_title)
            comment_text = my_page.get_attribute(MyPage.my_add_comment_name,"value")
        except TimeoutException:
            assert False , "test_my_036 작동 않음"
        except NoSuchElementException:
            assert False , "test_my_036  존재하지 않음"
        except Exception as e:
            assert False , "test_my_036 예외 발생"
        assert comment_title == "후기", "또 먹은 후기 - 후기 작성란 타이틀 잘못 노출됨"
        assert comment_text == "123", "또 먹은 후기 - 후기 작성란 내용 잘못 노출됨"


    @pytest.mark.flaky(reruns=3, reruns_delay=0.25)
    def test_my_037(self, driver:WebDriver):
        errors = []
        try:
            my_page = self.precondition_ai_recommend(driver)
            driver.fullscreen_window()
            my_page.click(MyPage.my_add_history_btn)
            star_title = my_page.text(MyPage.my_add_star_title)
            star_rate = my_page.texts(MyPage.my_add_star_rate)
        except TimeoutException:
            assert False , "test_my_037 작동 않음"
        except NoSuchElementException:
            assert False , "test_my_037  존재하지 않음"
        except Exception as e:
            assert False , "test_my_037 예외 발생"
        assert star_title == "별점", "또 먹은 후기 - 별점 타이틀 잘못 노출됨"
        assert len(star_rate) == 5, "또 먹은 후기 - 별점이 잘못 노출됨"


    @pytest.mark.flaky(reruns=3, reruns_delay=0.25)
    def test_my_038(self, driver:WebDriver):
        errors = []
        try:
            my_page = self.precondition_ai_recommend(driver)
            driver.fullscreen_window()
            my_page.click(MyPage.my_add_history_btn)
            submit_btn = my_page.is_displayed(MyPage.my_add_submit_btn)
            
        except TimeoutException:
            assert False , "test_my_038 작동 않음"
        except NoSuchElementException:
            assert False , "test_my_038  존재하지 않음"
        except Exception as e:
            assert False , "test_my_038 예외 발생"
        assert submit_btn == True, "또 먹은 후기 - 후기 작성 완료 버튼 미노출"


    @pytest.mark.flaky(reruns=3, reruns_delay=0.25)
    def test_my_039(self, driver:WebDriver):
        errors = []
        try:
            my_page = self.precondition_ai_recommend(driver)
            driver.fullscreen_window()
            my_page.click(MyPage.my_add_history_btn)
            my_page.click(MyPage.my_add_stars_5)
            my_page.click(MyPage.my_add_submit_btn)
            stars = my_page.texts(MyPage.my_add_history_star)
            count_star = stars[:5].count('★')
        except TimeoutException:
            assert False , "test_my_039 작동 않음"
        except NoSuchElementException:
            assert False , "test_my_039  존재하지 않음"
        except Exception as e:
            assert False , "test_my_039 예외 발생"
        assert count_star == 5, "별점이 다르게 노출됨"