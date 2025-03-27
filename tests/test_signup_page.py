import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from pages.login_page import LoginPage
from pages.signup_page import SignupPage

FakeData = {"name" : "육조임", "team" : "개발 1팀","value" : 0.99, "Ltext" : "한식에서 매콤한 음식을 좋아합니다." ,"Htext" : "중식에서 느끼한 음식을 싫어합니다."}
InvalidData = {"name" : "", "team" : "","value" : "", "Ltext" : "" ,"Htext" : ""}
LongData = {"name" : "@"*100,
                "team" : "#"*100,
                "value" : 10, "Ltext" : "백자가넘는텍스트"*20 ,"Htext" : "백자가넘는텍스트"*20}
LoginData = {"username" : "qwer2@qwer.qwer", "password" : "qwerQWER1!"}

def setup(login_page) :
            login_page.open()
            login_page.check_url("signin")
            #로그인 버튼 클릭
            login_page.click_button("로그인")
            login_page.check_url("login")
            
            #TC98
            login_page.login(LoginData["username"], LoginData["password"])
            login_page.check_url("welcome")
            
@pytest.mark.skip
@pytest.mark.usefixtures("driver")
class TestSignupPage:

    @pytest.mark.skip
    def test_signup_TC098(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)

            setup(login_page)

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip
    def test_signup_TC099(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            
            signup_page.set_name(FakeData["name"])
            if signup_page.get_name()!=FakeData["name"] :
                assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip        
    def test_signup_TC100(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            
            #TC100
            signup_page.set_select_option(FakeData["team"])
            
            if signup_page.get_team_option()!=FakeData["team"] :
                assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip   
    def test_signup_TC101(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            
            signup_page.set_slider_value("단", FakeData["value"])

            if float(signup_page.get_slider_value("단"))!=round(FakeData["value"],1) :
                assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip   
    def test_signup_TC102(self, driver: WebDriver):
            try:
                login_page = LoginPage(driver)
                signup_page= SignupPage(driver)

                setup(login_page)
                signup_page.set_slider_value("단", FakeData["value"])
                signup_page.set_slider_value("단", FakeData["value"]*-1)
                if float(signup_page.get_slider_value("단"))!=0.0 :
                    assert False

            except Exception as e:
                print(f"오류 발생: {e}")
                assert False

    @pytest.mark.skip
    def test_signup_TC103(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            
            signup_page.set_slider_value("짠", FakeData["value"])

            if float(signup_page.get_slider_value("짠"))!=round(FakeData["value"],1) :
                assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip
    def test_signup_TC104(self, driver: WebDriver):
            try:
                login_page = LoginPage(driver)
                signup_page= SignupPage(driver)

                setup(login_page)
                signup_page.set_slider_value("짠", FakeData["value"])
                signup_page.set_slider_value("짠", FakeData["value"]*-1)
                if float(signup_page.get_slider_value("짠"))!=0.0 :
                    assert False

            except Exception as e:
                print(f"오류 발생: {e}")
                assert False

    @pytest.mark.skip
    def test_signup_TC105(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            
            signup_page.set_slider_value("매운", FakeData["value"])

            if float(signup_page.get_slider_value("매운"))!=round(FakeData["value"],1) :
                assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip
    def test_signup_TC106(self, driver: WebDriver):
            try:
                login_page = LoginPage(driver)
                signup_page= SignupPage(driver)

                setup(login_page)
                signup_page.set_slider_value("매운", FakeData["value"])
                signup_page.set_slider_value("매운", FakeData["value"]*-1)
                if float(signup_page.get_slider_value("매운"))!=0.0 :
                    assert False

            except Exception as e:
                print(f"오류 발생: {e}")
                assert False

    @pytest.mark.skip
    def test_signup_TC107(self, driver: WebDriver):
            try:
                login_page = LoginPage(driver)
                signup_page= SignupPage(driver)

                setup(login_page)
                signup_page.set_like_textarea(FakeData["Ltext"])

                if signup_page.get_like_textarea()!=FakeData["Ltext"] :
                    assert False

            except Exception as e:
                print(f"오류 발생: {e}")
                assert False

    @pytest.mark.skip
    def test_signup_TC108(self, driver: WebDriver):
            try:
                login_page = LoginPage(driver)
                signup_page= SignupPage(driver)

                setup(login_page)
                signup_page.set_hate_textarea(FakeData["Htext"])

                if signup_page.get_hate_textarea()!=FakeData["Htext"] :
                    assert False

            except Exception as e:
                print(f"오류 발생: {e}")
                assert False

    @pytest.mark.skip
    def test_signup_TC0109(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            
            signup_page.click_button("제출하기")
            
            for error in signup_page.error_messages_check():
                 if error.text in "이름을 입력해주세요"  :
                    assert True
                    return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip  
    def test_signup_TC110(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            
            signup_page.click_button("제출하기")
            
            for error in signup_page.error_messages_check():
                 if error.text in "팀을 선택해주세요"  :
                    assert True
                    return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip  
    def test_signup_TC111(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            
            signup_page.click_button("제출하기")
            
            flavor_section_xpath = f"//section[.//span[text()='단 맛']]"
            flavor_section =driver.find_element(By.XPATH , flavor_section_xpath)
            sweet_error=flavor_section.find_element(By.XPATH, '//*[@id="root"]//p[contains(text(),"맛에 대한 성향은 최소")]')
            if sweet_error.text in "맛에 대한 성향은 최소 1 이상 설정해주세요":
                assert True
                return
            assert False
            
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip
    def test_signup_TC112(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            
            signup_page.click_button("제출하기")
            
            flavor_section_xpath = f"//section[.//span[text()='짠 맛']]"
            flavor_section =driver.find_element(By.XPATH , flavor_section_xpath)
            sweet_error=flavor_section.find_element(By.XPATH, '//*[@id="root"]//p[contains(text(),"맛에 대한 성향은 최소")]')
            if sweet_error.text in "맛에 대한 성향은 최소 1 이상 설정해주세요":
                assert True
                return
            assert False
            
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip
    def test_signup_TC113(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            
            signup_page.click_button("제출하기")
            
            flavor_section_xpath = f"//section[.//span[text()='매운 맛']]"
            flavor_section = driver.find_element(By.XPATH , flavor_section_xpath)
            sweet_error=flavor_section.find_element(By.XPATH, './/p[contains(text(),"맛에 대한 성향은 최소")]')
            if sweet_error.text in "맛에 대한 성향은 최소 1 이상 설정해주세요":
                assert True
                return
            assert False
            
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip
    def test_signup_TC114(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            
            signup_page.click_button("제출하기")
            parent=driver.find_element(By.NAME, 'pros')
            child=parent.find_element(By.XPATH, "parent::*")
            error=child.find_element(By.XPATH,'.//p[contains(text(),"10자 이상 입력해주세요")]')
            
            if error.text in "10자 이상 입력해주세요"  :
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip
    def test_signup_TC115(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            
            signup_page.click_button("제출하기")
            parent=driver.find_element(By.NAME, 'cons')
            child=parent.find_element(By.XPATH, "parent::*")
            error=child.find_element(By.XPATH,'.//p[contains(text(),"10자 이상 입력해주세요")]')
            
            if error.text in "10자 이상 입력해주세요"  :
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip
    def test_signup_TC116(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            signup_page.set_like_textarea(LongData["Ltext"])
            signup_page.click_button("제출하기")
            parent=driver.find_element(By.NAME, 'pros')
            child=parent.find_element(By.XPATH, "parent::*")
            try :
                error=child.find_element(By.XPATH,'.//p[contains(text(),"100자 이내로 입력해주세요")]')
            except NoSuchElementException:
                assert False
                
            if error.text in "100자 이내로 입력해주세요"  :
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip
    def test_signup_TC117(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            signup_page.set_hate_textarea(LongData["Ltext"])
            signup_page.click_button("제출하기")
            parent=driver.find_element(By.NAME, 'cons')
            child=parent.find_element(By.XPATH, "parent::*")
            try :
                error=child.find_element(By.XPATH,'.//p[contains(text(),"100자 이내로 입력해주세요")]')
            except NoSuchElementException:
                assert False
                
            if error.text in "100자 이내로 입력해주세요"  :
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    @pytest.mark.skip
    def test_signup_TC118(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)
            #페이지 로딩
            setup(login_page)

            #TC99
            signup_page.set_name(FakeData["name"])
            signup_page.get_name()

            #TC100
            signup_page.set_select_option(FakeData["team"])
            signup_page.get_team_option()

            
            #TC101, TC102
            signup_page.set_slider_value("단", FakeData["value"])
           
            #TC103, TC104
            signup_page.set_slider_value("짠", FakeData["value"])
            

            #TC105, TC106
            signup_page.set_slider_value("매운", FakeData["value"])
            

            #TC107, TC108
            signup_page.set_like_textarea(FakeData["Ltext"])
            signup_page.set_hate_textarea(FakeData["Htext"])

            
            #TC107 ~ TC117
            signup_page.click_button("제출하기")
            if signup_page.error_messages_check() == None :
                assert True
                return
            
            assert False
            

        except NoSuchElementException as e:
            assert False