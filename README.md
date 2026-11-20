# js-project-log

# 2026 대동제 & 해커톤 통합 운영 로그 분석기 (`js-project-log`)

학교 대동제 및 밤샘 해커톤 통합 운영 로그 데이터(`data_log.txt`)에서 정규표현식(Regular Expression)을 활용하여 유효한 핵심 정보만을 추출하고 정산하는 파이썬 프로그램입니다.

## 📁 프로젝트 구조

```text
js-project-log/
├── package/
│   ├── __init__.py      # 패키지 외부 인터페이스 정의
│   ├── load.py          # 로그 파일 로드 모듈
│   └── functions.py     # 5가지 항목별 정규표현식 추출 모듈
├── data_log.txt         # 분석 대상 원본 로그 데이터
├── main.py              # 프로그램 실행 및 결과 출력
└── README.md            # 프로젝트 설명 문서