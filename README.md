# ‘오늘 뭐먹지?’ QA 자동화 테스트 프로젝트
<br>

## 대상
: 직장인의 점심 메뉴 고민을 해결하는 AI 기반 맞춤형 추천 서비스 ‘오늘 뭐먹지? '홈페이지의 핵심 기능 전체
<br>

## 대상 사이트
:  http://kdt-pt-1-pj-2-team03.elicecoding.com
<br>

## 팀원
: 박재윤(조장), 신은영, 이세중
<br>

## 담당 페이지와 기능 (우선순위)
<br>

박재윤 - 히스토리, 개인 피드
<br>
히스토리 - 추천받은 메뉴 (중)
<br>
개인 피드 - 개인 프로필 탭 (중)
<br>
개인 피드 - 내 통계 (중)
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

이세중 - 로그인, 회원가입
<br>
로그인(상)
<br>
회원가입(상)
<br>

최효원 - 홈 탭
<br>
AI 메뉴 추천 (상)
<br>
선호 음식 종류 (하)
<br>
메뉴 추천 (중)
<br>
취향 분석 (하)
<br>

## 목표
- 자동화 스크립트를 직접 작성·실행하며 테스트 자동화의 원리를 학습하여 실무 감각 향상
- 프로젝트를 통해 효과적인 협업 및 소통 방법을 익힘
- 오류 및 환경 설정 문제 등을 해결하며 실전 대응 능력 강화
- 웹 주요 기능을 100% 자동화하여 오류를 조기 발견하고, 반복되는 빌드 과정에서 서비스 안정성과 테스트 효율 높이기
<br>


## utils 폴더

utils = 일단 테스트데이터인 망글곰.png, 치즈버거.jpg, webp이미지.webp 와 같은 파일과 이름, 소속, 이메일주소같은 데이터를 다 집어넣을 폴더.
<br>
```
from ..utils.test_data import test_files
from ..utils.test_data import test_datas 
```
와 같은 형식으로 불러오기
<br>


## 환경 설정

```
python -m venv venv
또는 
python -m venv .venv
(파이썬 가상환경 폴더 생성)

.\venv\Scripts\activate
(파이썬 가상환경 실행)

pip install selenium
pip install pytest
pip install pytest-rerunfailures

```

이후 추가
