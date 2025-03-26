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



@pytest.mark.usefixtures("login_driver")
class TestMyPage:

    @pytest.mark.skip()
    def test_001(self, driver: WebDriver):
        try:
            history_page = HistoryPage(driver)
            history_btn = history_page.history_btn()
            history_btn.click()
            WebDriverWait(driver,10).until(EC.url_contains("history"))
        except Exception as e:
            print(f"히스토리 페이지 진입 테스트 실패")
            assert False

    @pytest.mark.skip()
    def test_002(self, driver: WebDriver):
        try:
            history_page = HistoryPage(driver)
            history_page.history_btn().click()
            WebDriverWait(driver,10).until(EC.url_contains("history"))
            back_btn = history_page.back_btn()
            back_btn.click()
            WebDriverWait(driver,10).until_not(EC.url_contains("history"))
        except Exception as e:
            print(f"뒤로가기 버튼 누르기 실패")
            assert False

    @pytest.mark.skip()
    def test_003(self, driver: WebDriver):
        try:
            history_page = HistoryPage(driver)
            history_page.history_btn().click()
            WebDriverWait(driver,10).until(EC.url_contains("history"))

            GNB_name = history_page.GNB_name()
            assert GNB_name == "추천 히스토리" , "GNB 이름이 '추천 히스토리'가 아님"
        except Exception as e:
            print(f"GNB 이름 찾기 실패")
            assert False

    @pytest.mark.skip()
    def test_004(self, driver: WebDriver):
        try:
            history_page = HistoryPage(driver)
            history_page.history_btn().click()
            WebDriverWait(driver,10).until(EC.url_contains("history"))
            
            menu_list = history_page.menus()
            print(menu_list)
        except Exception as e:
            print(f"메뉴들을 찾아내지 못함")
            assert False
