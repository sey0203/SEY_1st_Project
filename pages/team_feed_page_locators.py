from selenium.webdriver.common.by import By
import os



class TeamFeedPageLocators:

     # GNB (Global Navigation Bar) 관련 선택자
     GNB_SELECTOR = "div.fixed.bottom-0.w-full.z-50.max-w-\\[600px\\].border-t-\\[1px\\].bg-white.border-gray-200.p-3.h-16"

     # 팀 피드 관련 선택자
     TEAM_FEED_SELECTOR = "a[href='/teams/1']"  # 팀 피드 페이지로 이동하는 링크
     TEAM_FEED_ICON_SELECTOR = "svg.fill-current"  # 팀 피드 아이콘
     TEAM_FEED_TITLE_XPATH = "//span[text()='팀 피드']"  # 팀 피드 페이지 타이틀

     # 파이차트, 막대그래프
     PIECHART_XPATH = "//div[contains(@class, 'relative aspect-square')]/canvas"
     BARCHART_XPATH = "//div[contains(@class, 'flex flex-col gap-2')]/canvas[last()]"

     # 프로필 관련 선택자
     PROFILE_EDIT_ICON_SELECTOR = "div.flex.items-center.justify-between.text-subbody > svg.cursor-pointer"  # 프로필 수정 아이콘
     PROFILE_EDIT_FINISH_BTN_SELECTOR = "button.cursor-pointer[type='submit']"  # 프로필 수정 완료 버튼
     PROFILE_EDIT_X_BTN_SELECTOR = "button.text-2xl.cursor-pointer"  # 프로필 수정 창 닫기 버튼
     FAVORITE_FOOD_INPUT_XPATH = '//textarea[@placeholder="좋아하는 음식 성향을 이야기해주세요!"]'
     HATE_FOOD_INPUT_XPATH = '//textarea[@placeholder="싫어하는 음식 성향을 이야기해주세요!"]'
     REVIEW_10MORE_REQUIRED_MESSAGE_XPATH = "//p[contains(text(), '10자 이상 입력해주세요')]"  # 후기 필수 메시지

     # 팀이 먹은 메뉴 관련 선택자
     TEAM_EATEN_MENU_ADD_BTN_SELECTOR = "div.flex.items-center.gap-4 > button"  # 메뉴 추가 버튼
     TEAM_EATEN_MENU_XPATH = "//span[contains(text(), '팀이 먹은 메뉴')]"  # 팀이 먹은 메뉴 타이틀

     # 새로운 후기 등록하기 관련 선택자
     REVIEW_CONTAINER_CSS = "div.flex.w-full.gap-6.p-4.shadow-md.rounded-2xl" #리뷰 컨테니어
     NEW_REVIEW_FINISH_BTN_XPATH = "//button[text()='후기 작성 완료']"  # 새로운 후기 작성 완료 버튼
     ADD_REVIEW_TITLE_XPATH = "//span[text()='새로운 후기 등록하기']"  # 새로운 후기 등록하기 제목
     MENU_REQUIRED_MESSAGE_XPATH = "//p[contains(text(), '메뉴명은 필수입니다')]"  # 메뉴명 필수 메시지
     CATEGORY_REQUIRED_MESSAGE_XPATH = "//p[contains(text(), '카테고리는 필수입니다')]"  # 카테고리 필수 메시지
     REVIEW_REQUIRED_MESSAGE_XPATH = "//p[contains(text(), '후기는 필수입니다')]"  # 후기 필수 메시지
     STAR_REQUIRED_MESSAGE_XPATH = "//p[contains(text(), '별점은 최소 1점 이상이어야 합니다')]"  # 별점 필수 메시지
     IMAGE_REQUIRED_MESSAGE_XPATH = "//p[contains(text(), '리뷰 이미지는 필수입니다')]"  # 이미지 필수 메시지
     TEST_REVIEW_XPATH = "//div[text()='팀피드실시간테스트']"  #테스트용 후기 업로드 확인
     TEST_REVIEW_MENU_XPATH = '//div[@class="font-bold" and text()="막국수"]'
     TEST_REVIEW_TAG_XPATH = '//div[contains(@class, "bg-main") and text()="회식"]'

     # 식사 유형 관련 선택자
     SOLO_DINNER_XPATH = "//label[@for='혼밥']" 
     GROUP_DINNER_XPATH = "//div[contains(@class, 'inline-flex') and contains(text(), '그룹')]"
     TEAM_DINNER_XPATH = "//div[contains(@class, 'inline-flex') and contains(text(), '회식')]"

     # 리뷰탭 - 후기 사진
     review_img_is_null = (By.XPATH, ".//div[contains(@class, 'object-cover w-24 h-24 rounded-md border-[1px] border-light-gray')]")
     review_img_btn = (By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/button')
     review_img_input = (By.NAME, 'reviewImg')
     image_path = os.path.abspath(r"\\utils\\깜자.png")
     review_img = (By.XPATH,"//img[@alt='후기 사진']")
     review_register_btn = (By.XPATH, "//button[contains(text(), '후기 등록')]") 
     #리뷰탭 - 메뉴 명
     review_menu = (By.NAME, 'menu')
     #리뷰탭 - 카테고리
     review_category = (By.XPATH, "//button[@role= 'combobox']")
     #리뷰탭 - 후기
     review_comment = (By.NAME, 'comment')
     review_star_yellow = ".//div[contains(@class, 'text-yellow-400')]" #별점 선택시 변화하는 요소
     review_stars_3 = '//div[text()="★"][3]'


     # 팀 이름 콤보박스 관련 선택자
     COMBOBOX_SELECTOR = "button[role='combobox']"  # 카테고리 선택 콤보박스
     COMBOBOX_TEAM1_XPATH = "//span[text()='개발 1팀']"  # 팀 선택 콤보박스
     COMBOBOX_TEAM2_XPATH = "//span[text()='개발 2팀']"  # 팀 선택 콤보박스
     COMBOBOX_TEAM3_XPATH = "//span[text()='디자인 1팀']"  # 팀 선택 콤보박스
     COMBOBOX_TEAM4_XPATH = "//span[text()='디자인 2팀']"  # 팀 선택 콤보박스

     # 팀 정보 관련 선택자
     FOOD_TENDENCY_XPATH = "//span[contains(text(), '음식 성향')]"  # 음식 성향 섹션
     TEAM_STATS_XPATH = "//span[contains(text(), '팀 통계')]"  # 팀 통계 섹션
     TEAM_NAME_SELECTOR = "div.px-2.py-1.rounded-lg.bg-sub-2 > span"  # 팀 이름 표시

     # 팀의 맛 성향 관련 선택자
     TEAM_SWEET_FLAVOR_TITLE_SELECTOR = "section:nth-child(2) > span.font-semibold.w-14.text-main-black" #단맛 타이틀
     TEAM_SALTY_FLAVOR_TITLE_SELECTOR = "section:nth-child(3) > span.font-semibold.w-14.text-main-black" #짠맛 타이틀
     TEAM_SPICY_FLAVOR_TITLE_SELECTOR = "section:nth-child(4) > span.font-semibold.w-14.text-main-black" #매운맛 타이틀
     TEAM_SWEET_FLAVOR_XPATH = "//section[span[text()='단 맛']]//span[@role='slider']"  # 단 맛 슬라이더
     TEAM_SALTY_FLAVOR_XPATH = "//section[span[text()='짠 맛']]//span[@role='slider']"  # 짠 맛 슬라이더
     TEAM_SPICY_FLAVOR_XPATH = "//section[span[text()='매운 맛']]//span[@role='slider']"  # 매운 맛 슬라이더
     TEAM_FLAVOR_REQUIRED_MESSAGE_XPATH = "//p[contains(text(), '맛에 대한 성향은 최소 1 이상 설정해주세요')]"  # 별점 필수 메시지
     SLIDER_BAR_CSS = 'span[data-orientation="horizontal"]' #슬라이더 바
     SLIDER_VALUE_SPAN_CSS = 'span.w-8.text-right.text-gray-500.text-subbody' #슬라이더 값

     # 팀의 좋아하는 음식 및 싫어하는 음식 관련 선택자
     TEAM_FAVORITE_FOOD_XPATH = "//*[@id='root']/div[1]/main/section/section/section/div[2]/div[1]/p"  # 좋아하는 음식
     TEAM_HATE_FOOD_XPATH = "//*[@id='root']/div[1]/main/section/section/section/div[2]/div[2]/p"  # 싫어하는 음식

     # 프로필 정보 수정 관련 선택자
     PROFILE_EDIT_XPATH = "//span[text()='프로필 정보 수정']"  # 프로필 정보 수정

     # 슬라이더 관련 선택자
     SWEET_SLIDER_XPATH = "//section[contains(., '단 맛')]//span[@role='slider']"  # 단 맛 슬라이더

     # '또 먹은 후기' 관련 선택자
     EAT_SAME_MENU_BTN_XPATH = "//*[@id='root']/div[1]/main/section/section/div[3]/div[2]/div[1]/div[2]/button"  # 또 먹은 메뉴 버튼
     SAME_MENU_REVIEW_TITLE_XPATH = "//span[text()='또 먹은 후기 등록하기']"  # 또 먹은 후기 등록하기 제목
     SAME_MENU_IMAGE_CSS = "img.object-cover.w-full.h-full.rounded-md.border-\\[1px\\].border-light-gray" #이미지
     #사천해물탕 사진 경로
     same_menu_src = "https://elice-assign-bucket.s3.ap-northeast-2.amazonaws.com/uploads/db111fd4-c9d7-4806-b625-644650b268cf_300_300_20230902021820639_photo_3cfebe345c18.webp"
     SAME_MENU_NAME_CSS = "input.flex.w-full.rounded-md[name='menu']" #메뉴이름
     SAME_MENU_CATEGORY_XPATH = "button[role='combobox'] span" #카테고리
     SAME_MENU_REVIEW_XPATH = "//textarea[@name='comment']" #후기내용 타이틀
     SAME_MENU_REVIEW_TEXT = "이번에 부장님을 모셨는데 비린 맛이 난다고 싫어하시더라구요 여긴 다시 안 가야겠습니다" #후기내용텍스트
     NEW_REVIEW_TEXT = "가"*30  #새로 입력할 후기 내용
     SAME_MENU_STAR_CSS = "input[name='star']" #별점