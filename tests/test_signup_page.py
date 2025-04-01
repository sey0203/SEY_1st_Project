import pytest
import random
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

NewLoginData = {"username" : "qwer11@qwer.qwer", "password" : "qwerQWER1!"}
LoginData = {"username" : "qwer3@qwer.qwer", "password" : "qwerQWER1!","password1" : "!Q2w3e4r"}
FalseLogin = {"username1" : "hi@com", "password1" : "qwerqwer", "password2" : "12341234" }


def setup(login_page) :
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("회원가입")
            login_page.check_url("u/signup")

@pytest.mark.usefixtures("driver")
class TestSignPage:
    def test_signup_TC032(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            background_color = driver.execute_script(
            "return window.getComputedStyle(document.documentElement).getPropertyValue('--widget-background-color');"
            )
            if background_color == "#ffffff" :
                print(background_color)
                assert True
                return
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC033(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            class_value="환영합니다"
            get_text = driver.find_element(By.XPATH, f"//h1[contains(text(),'{class_value}')]").text

            if class_value in get_text :
                print(get_text)
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC034(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            class_value="오늘 뭐 먹지? 를 사용하시려면 회원가입을 진행해주세요."
            get_text = driver.find_element(By.XPATH, f"//p[contains(text(),'{class_value}')]").text

            if class_value in get_text :
                print(get_text)
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
    
    
    def test_signup_TC035(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            driver.find_element(By.NAME, "email")
        except NoSuchElementException as e:
                    print("이메일 인풋을 찾지 못함")
                    assert False


        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
        
    
    def test_signup_TC036(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            driver.find_element(By.NAME, "password")

        except NoSuchElementException as e:
            print("비밀번호 인풋을 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
        

    
    def test_signup_TC037(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            driver.find_element(By.XPATH, '//button[@data-action="toggle"]')

        except NoSuchElementException as e:
            print("비밀번호 표시 버튼 못찾음")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
        
    
    def test_signup_TC038(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            driver.find_element(By.XPATH, '//button[contains(text(),"계속하기")]').click()
            
        except NoSuchElementException as e:
            print("계속하기 버튼 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
        
    
    def test_signup_TC039(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            class_value="이미 계정이 있으신가요"
            get_text = driver.find_element(By.XPATH, f"//p[contains(text(),'{class_value}')]").text
            if class_value in get_text:
                driver.find_element(By.XPATH, '//a[contains(text(),"로그인")]')
                print(get_text)
                assert True
                return
            assert False
        except NoSuchElementException as e:
            print("로그인 버튼 또는 텍스트 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
        
    
    def test_signup_TC040(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            background_color = driver.execute_script(
            "return window.getComputedStyle(document.body).getPropertyValue('--page-background-color');"
        )
            if background_color == "#fff7ed" :
                print(background_color)
                assert True
                return
            assert False
            
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
    
    
    def test_signup_TC041(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            name=driver.find_element(By.NAME, "email")
            name.send_keys(FalseLogin["username1"])
            
        except NoSuchElementException as e:
            print("이메일 인풋 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC042(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            name=driver.find_element(By.NAME, "password")
            name.send_keys(FalseLogin["password1"])
            
        except NoSuchElementException as e:
            print("비밀번호 인풋 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC043(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            name=driver.find_element(By.NAME, "password")
            name.send_keys(FalseLogin["password1"])
            driver.find_elements(By.CSS_SELECTOR, "span.cac336714")
                
        except NoSuchElementException as e:
            print("비밀번호 규칙창 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC044_TC045(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            name=driver.find_element(By.NAME, "password")
            name.send_keys(FalseLogin["password1"])
            length_element = driver.find_elements(By.CSS_SELECTOR, "span.cac336714")

            count=0
            for i in range(1, 6):
                if "At least 8 characters" in length_element[i].text :
                    if length_element[0].value_of_css_property("color") != length_element[i].value_of_css_property("color"):
                        count += 1
                        print(length_element[i].text+length_element[i].value_of_css_property("color"))
                if "Lower case letters (a-z)" in length_element[i].text :
                    if length_element[0].value_of_css_property("color") != length_element[i].value_of_css_property("color"):
                        count += 1
                        print(length_element[i].text+length_element[i].value_of_css_property("color"))
                if count >=2 :
                    assert True
                    return
            assert False

        except NoSuchElementException as e:
            print("비밀번호 규칙창 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC046_TC048(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            name=driver.find_element(By.NAME, "password")
            name.send_keys(LoginData["password1"])
            length_element = driver.find_elements(By.CSS_SELECTOR, "span.cac336714")

            count=0
            for i in range(1, 6):
                print(length_element[i].text)
                if "At least 8 characters" in length_element[i].text :
                    if length_element[0].value_of_css_property("color") != length_element[i].value_of_css_property("color"):
                        count += 1
                        print(length_element[i].text+length_element[i].value_of_css_property("color"))
                if "Numbers (0-9)" in length_element[i].text :
                    if length_element[0].value_of_css_property("color") != length_element[i].value_of_css_property("color"):
                        count += 1
                        print(length_element[i].text+length_element[i].value_of_css_property("color"))
                if count >=2 :
                    assert True
                    return
            assert False

        except NoSuchElementException as e:
            print("비밀번호 규칙창 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC049_TC055(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            name=driver.find_element(By.NAME, "password")
            name.send_keys(LoginData["password1"])
            length_element = driver.find_elements(By.CSS_SELECTOR, "span.cac336714")
            
            count=0
            for i in range(1, 6):
                if length_element[0].value_of_css_property("color") != length_element[i].value_of_css_property("color"):
                    print(length_element[i].text)
                    count += 1
                if count>=5 :
                    assert True
                    return
            assert False

        except NoSuchElementException as e:
            print("비밀번호 규칙창 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC056(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)

            name=driver.find_element(By.NAME, "password")
            name.send_keys(FalseLogin["password1"])

            driver.find_element(By.XPATH, '//button[@data-action="toggle"]').click()
        except NoSuchElementException as e:
            print("비밀번호 표시 버튼 못찾음")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC057(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)
            
            driver.find_element(By.XPATH, '//button[contains(text(),"계속하기")]').click()
            
            username_field = driver.find_element(By.ID, "email")
            error_massage=username_field.get_attribute("validationMessage")
            active_element = driver.switch_to.active_element

            # 확인 로직
            expected_focus_id = "email"
            if active_element.get_attribute("id") == expected_focus_id:
                if error_massage == "이 입력란을 작성하세요." :
                    print(error_massage)
                    print("✅ 테스트 성공: 필수 인풋으로 포커싱 이동함")
                    assert True
                    return
            else:
                print("❌ 테스트 실패: 예상한 필드로 포커싱되지 않음")
            assert False

        except NoSuchElementException as e:
            print("계속하기 버튼 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC058(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)
            
            driver.find_element(By.ID, "email").send_keys(FalseLogin["username1"])

            driver.find_element(By.XPATH, '//button[contains(text(),"계속하기")]').click()

            usespassword_field = driver.find_element(By.ID, "password")
            error_massage=usespassword_field.get_attribute("validationMessage")
            
            active_element = driver.switch_to.active_element
            print("포커스된 요소 ID:", 
            active_element.get_attribute("id"))
            # 확인 로직
            expected_focus_id = "password"
            if active_element.get_attribute("id") == expected_focus_id:
                if error_massage == "이 입력란을 작성하세요." :
                    print(error_massage)
                    print("✅ 테스트 성공: 필수 인풋으로 포커싱 이동함")
                    assert True
                    return
            else:
                print("❌ 테스트 실패: 예상한 필드로 포커싱되지 않음")
            assert False
            
        except NoSuchElementException as e:
            print("계속하기 버튼 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC059(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)
            
            
            driver.find_element(By.ID, "email").send_keys(LoginData["username"])
            driver.find_element(By.ID,"password").send_keys(FalseLogin["password2"])
            driver.find_element(By.XPATH, '//button[contains(text(),"계속하기")]').click()

            usespassword_field=driver.find_element(By.XPATH, '//div[contains(text(),"비밀번호*")]')
            default_color="rgba(208, 60, 56, 1)"
            field_color=usespassword_field.value_of_css_property("color")
            if default_color==field_color:
                print(field_color)
                assert True
                return
            
            assert False
            
        except NoSuchElementException as e:
            print("계속하기 버튼 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC060(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)
            
            
            driver.find_element(By.ID, "email").send_keys(FalseLogin["username1"])
            driver.find_element(By.ID,"password").send_keys(LoginData["password1"])
            driver.find_element(By.XPATH, '//button[contains(text(),"계속하기")]').click()
            
            try :
                error=ws(driver, 2).until(
                    EC.presence_of_element_located((By.ID, "error-element-email")) 
                )
                if "이메일이 유효하지 않습니다." in error.text:
                    print("TC060"+error.text)
                    assert True
                    return
                
            except TimeoutException:
                print("TC60 테스트 실패")
                assert False            
            
        except NoSuchElementException as e:
            print("계속하기 버튼 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
            
    
    def test_signup_TC061(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)
            
            
            driver.find_element(By.ID, "email").send_keys("qwer@qwer.qwer")
            driver.find_element(By.ID,"password").send_keys(LoginData["password1"])
            driver.find_element(By.XPATH, '//button[contains(text(),"계속하기")]').click()
            
            try :
                error=ws(driver, 2).until(
                    EC.presence_of_element_located((By.ID, "prompt-alert")) 
                )
                if "문제가 발생했습니다. 나중에 다시 시도해 주세요" in error.text:
                    print("TC061"+error.text)
                    assert True
                    return
                assert False
            except TimeoutException:
                print("TC61 테스트 실패")
                assert False            
            
        except NoSuchElementException as e:
            print("계속하기 버튼 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC062(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            setup(login_page)
            
            driver.find_element(By.ID, "email").send_keys(NewLoginData["username"])
            driver.find_element(By.ID,"password").send_keys(FalseLogin["password2"])
            driver.find_element(By.XPATH, '//button[contains(text(),"계속하기")]').click()

            usespassword_field=driver.find_element(By.XPATH, '//div[contains(text(),"비밀번호*")]')
            default_color="rgba(208, 60, 56, 1)"
            field_color=usespassword_field.value_of_css_property("color")
            if default_color==field_color:
                print(field_color)
                assert True
                return
            
            assert False
            
        except NoSuchElementException as e:
            print("계속하기 버튼 찾지 못함")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False


