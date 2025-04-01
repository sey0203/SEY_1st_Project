import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

LoginData = {"username" : "qwer3@qwer.qwer", "password" : "qwerQWER1!","password1" : "!Q2w3e4r"}
FalseLogin = {"username1" : "hi@com", "password1" : "qwerqwer", "password2" : "12341234" }
NewLoginData = {"username" : "qwer11@qwer.qwer", "password" : "qwerQWER1!"}


@pytest.mark.usefixtures("driver")
class TestLoginPage:
    
    def test_login_TC001(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")

            background_color = driver.execute_script(
            "return window.getComputedStyle(arguments[0]).getPropertyValue('background-color');",
                driver.find_element(By.CLASS_NAME, "rounded-xl")
            )
            if background_color == "rgb(255, 255, 255)" :
                print(background_color)
                assert True
                return
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC002(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            src_path="https://elice-assign-bucket.s3.ap-northeast-2.amazonaws.com/assign_logo.png"
            
            img_path=ws(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//img[contains(@alt,"점심 뭐먹지 로고")]'))
            ).get_attribute("src")

            if img_path==src_path :
                assert True
                return
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC004(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            #페이지 로딩
            class_value="오늘 뭐 먹지?"
            get_text = driver.find_element(By.XPATH, f"//h1[contains(text(),'{class_value}')]").text

            if class_value in get_text :
                print(get_text)
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC005(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            #페이지 로딩
            class_value="오늘의 식사 메뉴를 추천해드립니다"
            get_text = driver.find_element(By.XPATH, f"//p[contains(text(),'{class_value}')]").text

            if class_value in get_text :
                print(get_text)
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC006_TC011(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            #로그인 버튼 클릭
            login_page.click_button("로그인")
            login_page.check_url("login")

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC007(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            #페이지 로딩
            class_value="또는"
            get_text = driver.find_element(By.XPATH, f"//span[contains(text(),'{class_value}')]").text

            if class_value in get_text :
                print(get_text)
                assert True
                return
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC008_TC012(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            #로그인 버튼 클릭
            login_page.click_button("회원가입")
            login_page.check_url("u/signup")

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC009(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            
            background_color = driver.execute_script(
                "return window.getComputedStyle(arguments[0]).getPropertyValue('background-color');",
                driver.find_element(By.CLASS_NAME, "bg-orange-50")
            )
            
            if background_color == "oklch(0.98 0.016 73.684)" :
                print(background_color)
                assert True
                return
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
            
    
    def test_login_TC010(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            #페이지 로딩
            class_value="© 오늘 뭐 먹지?"
            get_text = driver.find_element(By.XPATH, f"//p[contains(text(),'{class_value}')]").text

            if class_value in get_text :
                print(get_text)
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC013(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")

            background_color = driver.execute_script(
            "return window.getComputedStyle(arguments[0]).getPropertyValue('background-color');",
                driver.find_element(By.CLASS_NAME, "cd059af9c, c1647f822")
            )
            
            if background_color == "rgb(255, 255, 255)" :
                print(background_color)
                assert True
                return
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC014(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")

            class_value="오늘 뭐 먹지?"
            get_text = driver.find_element(By.XPATH, f"//h1[contains(text(),'{class_value}')]").text

            if class_value in get_text :
                print(get_text)
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC015(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            #페이지 로딩
            class_value="맛있는 선택은 당신의 하루를 바꿉니다."
            get_text = driver.find_element(By.XPATH, f"//p[contains(text(),'{class_value}')]").text

            if class_value in get_text :
                print(get_text)
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC016(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            #페이지 로딩

            driver.find_element(By.NAME, "username")
        except NoSuchElementException as e:
                    print("username 인풋을 찾지 못함")
                    assert False

                    
    def test_login_TC017(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            #페이지 로딩

            driver.find_element(By.NAME, "password")
        except NoSuchElementException as e:
                    print("password 인풋을 찾지 못함")
                    assert False

    
    def test_login_TC018(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            #페이지 로딩

            driver.find_element(By.XPATH, '//button[@data-action="toggle"]')

        except NoSuchElementException as e:
            print("비밀번호 표시 버튼 못찾음")
            assert False

    
    def test_login_TC019(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            #페이지 로딩
            class_value="비밀번호를 잊으셨나요?"
            get_text = driver.find_element(By.XPATH, f"//a[contains(text(),'{class_value}')]").text

            if class_value in get_text :
                print(get_text)
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC020(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")

            driver.find_element(By.XPATH, '//button[contains(text(),"계속하기")]').click()

        except NoSuchElementException as e:
            print("계속하기 버튼 찾지 못함")
            assert False

    
    def test_login_TC021(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            #페이지 로딩
            class_value="계정이 없으신가요?"
            get_text = driver.find_element(By.XPATH, f"//p[contains(text(),'{class_value}')]").text

            if class_value in get_text :
                print(get_text)
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC022(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            
            background_color = driver.execute_script(
                "return window.getComputedStyle(arguments[0]).getPropertyValue('--page-background-color');",
                driver.find_element(By.CLASS_NAME, "c3c4bf5c1, login")
            )
            
            if background_color == "#fff7ed" :
                print(background_color)
                assert True
                return
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
            
    
    def test_login_TC023_TC24(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            
            driver.find_element(By.NAME, "username").send_keys(FalseLogin["username1"])
            driver.find_element(By.NAME, "password").send_keys(FalseLogin["password1"])
            
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC025(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            
            driver.find_element(By.NAME, "password").send_keys(FalseLogin["password1"])
            driver.find_element(By.XPATH, '//button[@data-action="toggle"]').click()
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False


    
    def test_login_TC026(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            
            driver.find_element(By.XPATH, '//button[contains(text(),"계속하기")]').click()

            username_field = driver.find_element(By.ID, "username")
            error_massage=username_field.get_attribute("validationMessage")
            active_element = driver.switch_to.active_element

            # 확인 로직
            expected_focus_id = "username"
            if active_element.get_attribute("id") == expected_focus_id:
                if error_massage == "이 입력란을 작성하세요." :
                    print(error_massage)
                    print("✅ 테스트 성공: 필수 인풋으로 포커싱 이동함")
                    assert True
                    return
            else:
                print("❌ 테스트 실패: 예상한 필드로 포커싱되지 않음")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC027(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            
            driver.find_element(By.ID, "username").send_keys(FalseLogin["username1"])
            driver.find_element(By.XPATH, '//button[contains(text(),"계속하기")]').click()
            
            username_field = driver.find_element(By.ID, "password")
            error_massage=username_field.get_attribute("validationMessage")
            active_element = driver.switch_to.active_element

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
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC028(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            
            driver.find_element(By.ID, "username").send_keys(FalseLogin["username1"])
            driver.find_element(By.ID, "password").send_keys(FalseLogin["password1"])
            driver.find_element(By.XPATH, '//button[contains(text(),"계속하기")]').click()
            
            try:
                error_element = ws(driver, 2).until(
                    EC.presence_of_element_located((By.ID, "error-element-password"))  
                )
                print(error_element.text)
                return True
            except TimeoutException:
                assert False

            
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC029(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            
            driver.find_element(By.ID, "username").send_keys(LoginData["username"])
            driver.find_element(By.ID, "password").send_keys(LoginData["password"])
            url=driver.current_url
            driver.find_element(By.XPATH, '//button[contains(text(),"계속하기")]').click()
            
            try:
                ws(driver, 1).until(
                        EC.url_changes(url))
            except TimeoutException:
                assert False

            
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC030(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            
            driver.find_element(By.XPATH, '//a[contains(text(),"비밀번호를 잊으셨나요?")]').click()
            login_page.check_url("u/reset-password")
        
            
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC031(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            
            driver.find_element(By.XPATH, '//a[contains(text(),"회원가입")]').click()
            login_page.check_url("u/signup")
        
            
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC120(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")
            
            driver.find_element(By.XPATH, '//a[contains(text(),"비밀번호를 잊으셨나요?")]').click()
            login_page.check_url("u/reset-password")


            background_color = driver.execute_script(
            "return window.getComputedStyle(arguments[0]).getPropertyValue('background-color');",
                driver.find_element(By.CLASS_NAME, "cd059af9c, c1647f822")
            )
            
            if background_color == "rgb(255, 255, 255)" :
                print(background_color)
                assert True
                return
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC121(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")

            driver.find_element(By.XPATH, '//a[contains(text(),"비밀번호를 잊으셨나요?")]').click()
            login_page.check_url("u/reset-password")

            #페이지 로딩
            class_value="비밀번호를 잊어버리셨나요?"
            get_text = driver.find_element(By.XPATH, f"//h1[contains(text(),'{class_value}')]").text

            if class_value in get_text :
                print(get_text)
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_login_TC122(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")

            driver.find_element(By.XPATH, '//a[contains(text(),"비밀번호를 잊으셨나요?")]').click()
            login_page.check_url("u/reset-password")

            #페이지 로딩
            class_value="이메일 주소를 입력하면 비밀번호 재설정 지침을 보내드립니다."
            get_text = driver.find_element(By.XPATH, f"//p[contains(text(),'{class_value}')]").text

            if class_value in get_text :
                print(get_text)
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC123_128(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")

            driver.find_element(By.XPATH, '//a[contains(text(),"비밀번호를 잊으셨나요?")]').click()
            login_page.check_url("u/reset-password")

            driver.find_element(By.NAME, "email").send_keys(LoginData["username"])
        except NoSuchElementException as e:
                    print("이메일 인풋을 찾지 못함")
                    assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC124(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")

            driver.find_element(By.XPATH, '//a[contains(text(),"비밀번호를 잊으셨나요?")]').click()
            login_page.check_url("u/reset-password")

            driver.find_element(By.XPATH, '//button[contains(text(),"계속")]')
        except NoSuchElementException as e:
                    print("계속 버튼 찾지 못함")
                    assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC125(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")

            driver.find_element(By.XPATH, '//a[contains(text(),"비밀번호를 잊으셨나요?")]').click()
            login_page.check_url("u/reset-password")

            driver.find_element(By.XPATH, '//button[contains(text(),"로그인 화면으로 돌아가기")]')
        except NoSuchElementException as e:
                    print("로그인 화면 돌아가기 버튼 찾지 못함")
                    assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
    
    
    def test_signup_TC126(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")

            driver.find_element(By.XPATH, '//a[contains(text(),"비밀번호를 잊으셨나요?")]').click()
            login_page.check_url("u/reset-password")

            background_color = driver.execute_script(
                "return window.getComputedStyle(arguments[0]).getPropertyValue('--page-background-color');",
                driver.find_element(By.CLASS_NAME, "c3c4bf5c1, login")
            )
            
            if background_color == "#fff7ed" :
                print(background_color)
                assert True
                return
            assert False
        except NoSuchElementException as e:
                    print("계속 버튼 찾지 못함")
                    assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC127(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")

            driver.find_element(By.XPATH, '//a[contains(text(),"비밀번호를 잊으셨나요?")]').click()
            login_page.check_url("u/reset-password")

            driver.find_element(By.XPATH, '//button[contains(text(),"계속")]').click
            
            # 확인 로직
            expected_focus_id = "email"
            username_field = driver.find_element(By.ID, expected_focus_id)
            error_massage=username_field.get_attribute("validationMessage")
            active_element = driver.switch_to.active_element
            
            if active_element.get_attribute("id") == expected_focus_id:
                if error_massage == "이 입력란을 작성하세요." :
                    print(error_massage)
                    print("✅ 테스트 성공: 필수 인풋으로 포커싱 이동함")
                    assert True
                    return
            else:
                print("❌ 테스트 실패: 예상한 필드로 포커싱되지 않음")
            assert False
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False
    
    
    def test_signup_TC129(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")

            driver.find_element(By.XPATH, '//a[contains(text(),"비밀번호를 잊으셨나요?")]').click()
            login_page.check_url("u/reset-password")
            driver.find_element(By.NAME, "email").send_keys(FalseLogin["username1"])
            driver.find_element(By.XPATH, '//button[contains(text(),"계속")]').click()
            
            try:
                error_element = ws(driver, 2).until(
                    EC.presence_of_element_located((By.ID, "error-element-email"))  
                )
                print(error_element.text)
                return True
            except TimeoutException:
                assert False
            
        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC130(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")

            driver.find_element(By.XPATH, '//a[contains(text(),"비밀번호를 잊으셨나요?")]').click()
            login_page.check_url("u/reset-password")

            driver.find_element(By.XPATH, '//button[contains(text(),"로그인 화면으로 돌아가기")]').click()


        except NoSuchElementException as e:
                    print("로그인 화면 돌아가기 버튼 찾지 못함")
                    assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC131(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")

            driver.find_element(By.XPATH, '//a[contains(text(),"비밀번호를 잊으셨나요?")]').click()
            login_page.check_url("u/reset-password")

            driver.find_element(By.NAME, "email").send_keys(LoginData["username"])
            driver.find_element(By.XPATH, '//button[contains(text(),"계속")]').click()

            class_value="Check Your Email"
            get_text = driver.find_element(By.XPATH, f"//h1[contains(text(),'{class_value}')]").text

            if class_value in get_text :
                print(get_text)
                assert True
                return
            
            class_value1="Please check the email address"
            get_text1 = driver.find_element(By.XPATH, f"//p[contains(text(),'{class_value}')]").text

            if class_value1 in get_text1 :
                print(get_text)
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False

    
    def test_signup_TC132(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.check_url("signin")
            login_page.click_button("로그인")
            login_page.check_url("login")

            driver.find_element(By.XPATH, '//a[contains(text(),"비밀번호를 잊으셨나요?")]').click()
            login_page.check_url("u/reset-password")

            driver.find_element(By.NAME, "email").send_keys(LoginData["username"])
            driver.find_element(By.XPATH, '//button[contains(text(),"계속")]').click()

            driver.find_element(By.XPATH, '//button[contains(text(),"Resend email")]').click()
            class_value="비밀번호를 잊어버리셨나요?"

            get_text = driver.find_element(By.XPATH, f"//h1[contains(text(),'{class_value}')]").text

            if class_value in get_text :
                print(get_text)
                assert True
                return
            assert False

        except Exception as e:
            print(f"오류 발생: {e}")
            assert False