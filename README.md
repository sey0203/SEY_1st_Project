# ‘오늘 뭐먹지?’ QA 자동화 테스트 프로젝트
<br>

## 대상
: 직장인의 점심 메뉴 고민을 해결하는 AI 기반 맞춤형 추천 서비스 ‘오늘 뭐먹지? '홈페이지의 핵심 기능 전체
<br>

## 대상 사이트
:  http://kdt-pt-1-pj-2-team03.elicecoding.com
<br>

## 팀원
: 3명
<br>

## 담당 페이지와 기능 (우선순위)
<br>
신은영 - 팀 피드
<br>
팀 선택 드롭다운 (상)
<br>
팀 성향 (중)
<br>
팀 통계 (하)
<br>
팀이 먹은 메뉴 (중)
<br>


## 목표
- 자동화 스크립트를 직접 작성·실행하며 테스트 자동화의 원리를 학습하여 실무 감각 향상
- 프로젝트를 통해 효과적인 협업 및 소통 방법을 익힘
- 오류 및 환경 설정 문제 등을 해결하며 실전 대응 능력 강화
- 웹 주요 기능을 100% 자동화하여 오류를 조기 발견하고, 반복되는 빌드 과정에서 서비스 안정성과 테스트 효율 높이기
<br>

## 환경 설정

```
python -m venv venv
.\venv\Scripts\activate
git clone https://github.com/Jaypark711/QA_1st_project.git
pip install selenium
pip install pytest
pip install pytest-rerunfailures
pip install opencv-python
echo LOGIN_INFO = {"user_id" : "1xdist@test.com", "user_password" : "!Q2w3e4r"} > QA_1st_project\user_info.py
pytest
```
