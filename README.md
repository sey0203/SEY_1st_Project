# 💡 ‘오늘 뭐먹지?’ QA 자동화 테스트 프로젝트

본 저장소는 엘리스 트랙에서 제공한 **‘오늘 뭐먹지?’** 를 대상으로 진행한 Selenium 기반의 테스트 자동화 및 관련 산출물을 정리한 포트폴리오용 저장소입니다.

<br>

## 📌 프로젝트 개요
- 직장인 대상 AI 맞춤형 점심 메뉴 추천 서비스 **‘오늘 뭐먹지?’**의 핵심 기능 QA 자동화 프로젝트
- Selenium 기반 테스트 자동화를 통해 서비스 품질과 테스트 효율성을 실질적으로 개선
<br>

## 🔗 대상 사이트
http://kdt-pt-1-pj-2-team03.elicecoding.com
<br>
<br>

## 👥 팀 구성
: 팀원 3명
<br>
<br>

## 🔍 담당 페이지와 기능 (우선순위)

신은영 - 팀 피드
<br>
<br>
팀 선택 드롭다운 (상)
<br>
팀 성향 (중)
<br>
팀 통계 (하)
<br>
팀이 먹은 메뉴 (중)
<br>
<br>


## 🧪 목표
- 자동화 스크립트를 직접 작성·실행하며 테스트 자동화의 원리를 학습하여 실무 감각 향상
- 프로젝트를 통해 효과적인 협업 및 소통 방법을 익힘
- 오류 및 환경 설정 문제 등을 해결하며 실전 대응 능력 강화
- 웹 주요 기능을 자동화하여 오류를 조기 발견하고, 반복되는 빌드 과정에서 서비스 안정성과 테스트 효율 높이기
<br>


## 🛠 사용 기술
- Python, Selenium, Google Sheets, GitHub, Discode
<br>


## ⚙️ 환경 설정

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
