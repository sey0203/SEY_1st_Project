from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

class SignupPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def open(self):
        self.driver.get(self.URL)

    def open_page(self, url : str):
        self.driver.get(url)
    
    def set_slider_value_action_chains(self, flavor, value):
        try:
            # 맛에 해당하는 슬라이더 섹션 찾기
            flavor_section_xpath = f"//section[.//span[text()='{flavor} 맛']]"
            flavor_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, flavor_section_xpath))
            )

            # # 슬라이더 thumb 요소 찾기
            thumb_element = flavor_section.find_element(By.XPATH, ".//span[@role='slider']")

            # # 슬라이더 트랙 요소 찾기
            track_element = flavor_section.find_element(By.XPATH, ".//span[@class='relative h-2 w-full grow overflow-hidden rounded-full bg-light-gray']")

                # 슬라이더 트랙의 시작점 x 좌표
            track_start_x = track_element.location['x']

            # 슬라이더 thumb 요소의 오프셋
            thumb_offset = thumb_element.size['width'] / 2

            # 이동할 x 좌표 계산
            target_x = track_start_x + (float(value) / 5) * track_element.size['width'] - thumb_offset

            # 드래그 앤 드롭 동작 수행
            action = ActionChains(self.driver)
            action.click_and_hold(thumb_element).move_by_offset(target_x - thumb_element.location['x'], 0).release().perform()

            return True
        except Exception as e:
            print(f"오류 발생: {e}")
            return False
