import time
import pytest
import random
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from pages.login_page import LoginPage
from pages.signup_page import SignupPage

FakeData = {"name" : "육조임", "team" : "개발 1팀","value" : 1, "Ltext" : "한식에서 매콤한 음식을 좋아합니다." ,"Htext" : "중식에서 느끼한 음식을 싫어합니다."}
InvalidData = {"name" : "김", "team" : "개발 4팀","value" : 0.99, "Ltext" : "         " ,"Htext" : "         "}
LongData = {"name" : "@"*100,
                "team" : "#"*100,
                "value" : 10, "Ltext" : "백자가넘는텍스트"*20 ,"Htext" : "백자가넘는텍스트"*20}

@pytest.mark.usefixtures("driver")
class TestSignupPage:    
    print("123")
    def test_signup_TC002(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)
            
            #페이지 로딩
            login_page.open()
            login_page.check_url("signin")
            #로그인 버튼 클릭
            login_page.click_button("로그인")
            login_page.check_url("login")

            #TC98
            login_page.login("qwer1@qwer.qwer","qwerQWER1!")
            login_page.check_url("welcome")

            #TC99
            signup_page.set_name(FakeData["name"])
            signup_page.get_name()

            #TC100
            signup_page.set_select_option(FakeData["team"])
            signup_page.get_team_option()

            
            #TC101, TC102
            signup_page.set_slider_value("단", FakeData["value"])
            print(signup_page.get_slider_value("단"))
            signup_page.set_slider_value("단", FakeData["value"]*-1)
            print(signup_page.get_slider_value("단"))

            #TC103, TC104
            signup_page.set_slider_value("짠", FakeData["value"])
            print(signup_page.get_slider_value("짠"))
            signup_page.set_slider_value("짠", FakeData["value"]*-1)
            print(signup_page.get_slider_value("짠"))
            

            #TC105, TC106
            signup_page.set_slider_value("매운", FakeData["value"])
            print(signup_page.get_slider_value("매운"))
            signup_page.set_slider_value("매운", FakeData["value"]*-1)
            print(signup_page.get_slider_value("매운"))

            #TC107, TC108
            signup_page.set_like_textarea(FakeData["Ltext"])
            signup_page.set_hate_textarea(FakeData["Htext"])

            print(signup_page.get_hate_textarea())
            print(signup_page.get_like_textarea())
            
            #TC107 ~ TC117
            signup_page.click_button("제출하기")
            signup_page.error_messages_check()

        except NoSuchElementException as e:
            
            assert False