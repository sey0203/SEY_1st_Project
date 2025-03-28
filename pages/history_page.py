#history_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time
import random
import os 

class HistoryPage:
    URL = "http://kdt-pt-1-pj-2-team03.elicecoding.com/"

    def __init__(self, driver: WebDriver):
        self.driver = driver



    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def clear(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).send_keys(text)

    def text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def texts(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        return [el.text for el in elements]

    def is_displayed(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()


    
    def get_attribute(self, by_locator, attribute):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).get_attribute(attribute)



    def menu_list(self):
        result = []
        boxes = self.driver.find_elements(*self.menu_box_locator)
        for box in boxes:
            main = box.find_element(*self.main_category_locator).text
            sub = box.find_element(*self.sub_category_locator).text
            name = box.find_element(*self.menu_name_locator).text
            score = box.find_element(*self.score_locator).text
            result.append([main, sub, name, score])
        return result

    #히스토리 탭 진입 버튼
    history_btn = (By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[3]/a')
    #GNB 영역
    back_btn = (By.CLASS_NAME,'cursor-pointer')
    GNB_history = (By.XPATH,'//*[@id="root"]/div[1]/header/div/span')
    #히스토리탭 영역
    history_title = (By.XPATH,'//*[@id="root"]/div[1]/main/section/section/span')
    review_register_btn = (By.XPATH, "//button[contains(text(), '후기 등록')]") 
    #히스토리탭 - 메뉴 박스 영역
    menu_box_locator = (By.XPATH, "//div[@class='flex w-full gap-6 p-4 shadow-md rounded-2xl']")
    main_category_locator = (By.XPATH, ".//div[contains(@class, 'bg-main')]")
    sub_category_locator = (By.XPATH, ".//div[contains(@class, 'bg-sub')]")
    menu_name_locator = (By.XPATH, ".//div[@class='font-bold']")
    score_locator = (By.CSS_SELECTOR, "span.font-bold.text-sub-2.text-subbody")

    #리뷰탭
    review_tab = (By.XPATH,'//*[@id="modal-root"]/div')
    #리뷰탭 - GNB 영역
    GNB_review = (By.XPATH,'//*[@id="modal-root"]/div/div[1]/span')
    GNB_review_back_btn = (By.XPATH,'//*[@id="modal-root"]/div/div[1]/button')
    #리뷰탭 - 식사 유형
    eat_alone = (By.XPATH, "//label[@for='혼밥']")
    eat_group = (By.XPATH, "//label[@for='그룹']")
    eat_together = (By.XPATH, "//label[@for='회식']")
    eat_alone_radio = (By.ID, "혼밥")
    eat_group_radio = (By.ID, "그룹")
    eat_together_radio = (By.ID, "회식")
    #리뷰탭 - 후기 사진
    review_img_is_null = (By.XPATH, ".//div[contains(@class, 'object-cover w-24 h-24 rounded-md border-[1px] border-light-gray')]")
    review_img_btn = (By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/button')
    review_img_input = (By.NAME, 'reviewImg')
    image_path = os.path.abspath('utils/망글곰.png')
    review_img = (By.XPATH,"//img[@alt='후기 사진']")
    #리뷰탭 - 메뉴 명
    review_menu = (By.NAME, 'menu')
    #리뷰탭 - 카테고리
    review_category = (By.XPATH, "//button[@role= 'combobox']")
    #리뷰탭 - 후기
    review_comment = (By.NAME, 'comment')

    #리뷰탭 - 별점
    review_star_gray = (By.XPATH,".//div[contains(@class, 'text-gray-300')]" )
    review_star_yellow = (By.XPATH,".//div[contains(@class, 'text-yellow-400')]" )
    review_stars_3 = (By.XPATH, '//div[text()="★"][3]')

    #리뷰탭 - 후기 작성 완료 버튼
    review_submit_btn = (By.XPATH, "//button[contains(text(), '후기 작성 완료')]")

    #리뷰탭 - 경고
    review_img_warning = (By.XPATH, "//p[contains(text(), '리뷰 이미지는 필수입니다')]")
    review_text_warning = (By.XPATH, "//p[contains(text(), '후기는 필수입니다')]")
    review_star_warning = (By.XPATH, "//p[contains(text(), '별점은 최소 1점 이상이어야 합니다')]")

    #홈 탭 - 혼자 먹기

    eat_alone_home_btn = (By.XPATH, "//button[.//p[text()='혼자 먹기']]")
    eat_alone_home_combobox = (By.XPATH, "//button[@role='combobox']")
    eat_alone_home_category_Korean = (By.XPATH, "//span[text()='한식']")
    eat_alone_home_choose_btn = (By.XPATH, "//button[text()='선택 완료']")
    eat_alone_home_accept_recommend = (By.XPATH, "//button[text()='추천 수락하기']")