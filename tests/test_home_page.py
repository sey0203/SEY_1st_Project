@pytest.mark.parametrize("category", ["한식", "중식", "양식"])
def test_food_category(login_driver, category):
    """로그인 후 음식 카테고리 선택 및 추천 과정 검증"""
    try:
        # 1. 홈 페이지 로드
        home_page = HomePage(login_driver)
        home_page.load_home()
        assert home_page.is_home_loaded(), "홈 페이지 로드 실패"
        
        # 2. 혼자 먹기 버튼 클릭 및 페이지 로드 확인
        solo_page = SoloKoreanFood(login_driver)
        solo_page.eat_solo()
        assert solo_page.is_load_alone_page(), "혼자 먹기 페이지 로드 실패"

        # 3. 음식 카테고리 선택
        solo_page.select_category(category)
        solo_page.click_complete_button()

        # 4. 추천 메뉴 확인
        recommendation_page = RecommendationPage(login_driver)
        assert recommendation_page.is_menu_displayed(), "추천 메뉴 확인 실패"
        recommendation_page.accept_recommendation()

        # 5. 추천 히스토리 확인
        history_page = HistoryPage(login_driver)
        assert login_driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/history", "추천 히스토리 페이지 확인 실패"
        history_page.go_back()
        assert login_driver.current_url == home_page.base_url, "혼자 먹기 페이지 복귀 실패"

        print("테스트 전체 플로우: PASS")
    except AssertionError as e:
        print(f"테스트 실패: FAIL - {e}")
        raise
