import pytest
import random
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.login_page import LoginPage
from pages.signup_page import SignupPage
FakeData = {"name" : "육조임", "team" : "개발 1팀","value" : 0.99, "Ltext" : "한식에서 매콤한 음식을 좋아합니다." ,"Htext" : "중식에서 느끼한 음식을 싫어합니다."}
InvalidData = {"name" : "", "team" : "","value" : "", "Ltext" : "" ,"Htext" : ""}
LongData = {"name" : "@"*100,
                "team" : "#"*100,
                "value" : 10, "Ltext" : "백자가넘는텍스트"*20 ,"Htext" : "백자가넘는텍스트"*20}
NewLoginData = {"username" : "qwer"+str(random.randint(1000,9999))+"@qwer.qwer", "password" : "qwerQWER1!","password1" : "!Q2w3e4r"}

def setup(login_page) :
            login_page.open()
            login_page.check_url("signin")
            #로그인 버튼 클릭
            login_page.click_button("로그인")
            login_page.check_url("login")
            
            #TC98
            login_page.login(NewLoginData["username"], NewLoginData["password"])
            login_page.check_url("welcome")


@pytest.mark.usefixtures("driver")
class TestconsentPage:

    def test_signup_TC063(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("회원가입")
            login_page.check_url("u/signup")

            if login_page.signup(NewLoginData["username"],NewLoginData["password"]):
                return
            print("TC063 실패")
            assert False
            
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
    
    def test_signup_TC064(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            login_page.login(NewLoginData["username"], NewLoginData["password"])
            login_page.check_url("u/consent")

            class_value="c53c6f72a,cd0e583bc,cf991a62f"   
            
            get_text=driver.find_element(By.CLASS_NAME, class_value).text
            if NewLoginData["username"] in get_text :
                print(get_text)
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
        except TimeoutException:
            print("슬라이드 로딩 시간 초과.")
            return False
    
    
    def test_signup_TC065(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)

            setup(login_page)

            login_page.login(NewLoginData["username"], NewLoginData["password"])
            login_page.check_url("u/consent")
            text="Decline"
            driver.find_element(By.XPATH, f'//button[contains(text(),"{text}")]').click()
            login_page.check_url("signin")
            driver.find_element(By.XPATH, '//button[contains(text(),"다시 시도")]').click()
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC066(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)

            setup(login_page)
            login_page.login(NewLoginData["username"], NewLoginData["password"])
            login_page.check_url("u/consent")
            text="Accept"
            driver.find_element(By.XPATH, f'//button[contains(text(),"{text}")]').click()
            login_page.check_url("welcome")
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC067(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)

            login_page.open()
            login_page.check_url("signin")
            #로그인 버튼 클릭
            login_page.click_button("회원가입")
            login_page.check_url("u/signup")

            text="로그인"
            driver.find_element(By.XPATH, f'//a[contains(text(),"{text}")]').click()
            login_page.check_url("login")
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False



@pytest.mark.skip
@pytest.mark.usefixtures("driver")
class TestWelcomePage:
    def test_signup_TC069(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)

            setup(login_page)
            class_value="p-4,bg-white"   
            driver.find_element(By.CLASS_NAME, class_value)
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    def test_signup_TC070(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            src_path="https://elice-assign-bucket.s3.ap-northeast-2.amazonaws.com/assign_logo.png"
            setup(login_page)
            img_path=ws(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//img[contains(@alt,"오늘 뭐 먹지?")]'))
            ).get_attribute("src")
            
            if img_path==src_path :
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC071(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)

            class_value="서비스 이용을 위해"
            get_text = driver.find_element(By.XPATH, f"//span[contains(text(),'{class_value}')]").text
            print(get_text)
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC072(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)

            class_value="이름을 입력해주세요"
            get_text = driver.find_element(By.XPATH, f"//p[contains(text(),'{class_value}')]").text
            print(get_text)
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC073(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)

            driver.find_element(By.NAME, "name")
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC074(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)
            class_value="본인이 속한 팀을"
            get_text = driver.find_element(By.XPATH, f"//p[contains(text(),'{class_value}')]").text
            print(get_text)
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
            
    
    def test_signup_TC075(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)
            driver.find_element(By.XPATH, '//*[@id="root"]//select')
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC076(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)
            text="팀 선택"
            get_text=driver.find_element(By.XPATH, f'//*[@id="root"]//span[contains(text(),"{text}")]').text
            print(get_text)
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    @pytest.mark.parametrize("TEAM", [0,1,2,3])
    def test_signup_TC077_TC80(self, driver: WebDriver, TEAM):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)
            option = driver.find_element(By.XPATH, '//*[@id="root"]//select')
            select_element = Select(option)
            get_text=select_element.options[TEAM].text
            print(get_text)
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC081(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)
            class_value="음식 성향에 대해"
            get_text = driver.find_element(By.XPATH, f"//p[contains(text(),'{class_value}')]").text
            print(get_text)
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    @pytest.mark.parametrize("TASTE", ["단","짠","매운"])
    def test_signup_TC082_TC087(self, driver: WebDriver,TASTE):
        try:
            login_page = LoginPage(driver)
            setup(login_page)
            signup_page= SignupPage(driver)
            signup_page.set_slider_value(TASTE, 0)
            get_text=signup_page.get_slider_value(TASTE)
            print(get_text)

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC088(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)
            text="음식 성향을 이야기 해주세요!"
            get_text=driver.find_element(By.XPATH, f'//*[@id="root"]//p[contains(text(),"{text}")]').text
            print(get_text)
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC089(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)
            text="점은 좋아요"
            get_text=driver.find_element(By.XPATH, f'//*[@id="root"]//p[contains(text(),"{text}")]').text
            print(get_text)
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC090(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)
            driver.find_element(By.NAME, 'pros')
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC091(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)

            driver.find_element(By.NAME, 'pros')
            parent=driver.find_element(By.NAME, 'pros')
            child=parent.find_element(By.XPATH, "parent::*")
            num_text=child.find_element(By.CLASS_NAME, "text-subbody, text-dark-gray").text
            print(num_text)
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC093(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)
            text="점은 싫어요"
            get_text=driver.find_element(By.XPATH, f'//*[@id="root"]//p[contains(text(),"{text}")]').text
            print(get_text)
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC094(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)
            driver.find_element(By.NAME, 'cons')
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC095(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)
            
            driver.find_element(By.NAME, 'cons')
            parent=driver.find_element(By.NAME, 'cons')
            child=parent.find_element(By.XPATH, "parent::*")
            num_text=child.find_element(By.CLASS_NAME, "text-subbody, text-dark-gray").text
            print(num_text)
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC096(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            
            setup(login_page)
            
            driver.find_element(By.XPATH, '//*[@id="root"]//button[contains(text(),"제출하기")]')
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC097(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)

            setup(login_page)

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC098(self, driver: WebDriver):
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

            
    def test_signup_TC099(self, driver: WebDriver):
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

       
    def test_signup_TC100(self, driver: WebDriver):
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

       
    def test_signup_TC101(self, driver: WebDriver):
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

    
    def test_signup_TC102(self, driver: WebDriver):
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

    
    def test_signup_TC103(self, driver: WebDriver):
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

    
    def test_signup_TC104(self, driver: WebDriver):
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

    
    def test_signup_TC105(self, driver: WebDriver):
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

    
    def test_signup_TC106(self, driver: WebDriver):
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

    
    def test_signup_TC107(self, driver: WebDriver):
            try:
                login_page = LoginPage(driver)
                signup_page= SignupPage(driver)

                setup(login_page)
                signup_page.set_like_textarea(FakeData["Ltext"])

                driver.find_element(By.NAME, 'pros')
                parent=driver.find_element(By.NAME, 'pros')
                child=parent.find_element(By.XPATH, "parent::*")
                num_text=child.find_element(By.CLASS_NAME, "text-subbody, text-dark-gray").text
                if num_text == "19/100자" :
                    print(num_text)
                    assert True
                    return
                assert False
                
            except Exception as e:
                print(f"오류 발생: {e}")
                assert False

    
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

    
    def test_signup_TC109(self, driver: WebDriver):
            try:
                login_page = LoginPage(driver)
                signup_page= SignupPage(driver)

                setup(login_page)
                signup_page.set_hate_textarea(FakeData["Htext"])

                driver.find_element(By.NAME, 'cons')
                parent=driver.find_element(By.NAME, 'cons')
                child=parent.find_element(By.XPATH, "parent::*")
                num_text=child.find_element(By.CLASS_NAME, "text-subbody, text-dark-gray").text
                if num_text == "19/100자" :
                    print(num_text)
                    assert True
                    return
                assert False
                
            except Exception as e:
                print(f"오류 발생: {e}")
                assert False

    
    def test_signup_TC0110(self, driver: WebDriver):
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

      
    def test_signup_TC111(self, driver: WebDriver):
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

      
    def test_signup_TC112(self, driver: WebDriver):
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

    
    def test_signup_TC113(self, driver: WebDriver):
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

    
    def test_signup_TC114(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            signup_page= SignupPage(driver)

            setup(login_page)
            
            signup_page.click_button("제출하기")
            
            flavor_section_xpath = f"//section[.//span[text()='매운 맛']]"
            flavor_section = driver.find_element(By.XPATH , flavor_section_xpath)
            sweet_error=flavor_section.find_element(By.XPATH, '//*[@id="root"]//p[contains(text(),"맛에 대한 성향은 최소")]')
            if sweet_error.text in "맛에 대한 성향은 최소 1 이상 설정해주세요":
                assert True
                return
            assert False
            
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC115(self, driver: WebDriver):
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

    
    def test_signup_TC116(self, driver: WebDriver):
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

    
    def test_signup_TC117(self, driver: WebDriver):
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

    
    def test_signup_TC118(self, driver: WebDriver):
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

    
    def test_signup_TC119(self, driver: WebDriver):
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