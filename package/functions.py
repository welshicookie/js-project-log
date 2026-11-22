import re


def valid_emails(text: str) -> list[str]:
    """1. 유효한 이메일 주소 추출 (도메인 형식 손상 제외)"""
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)


def phone_numbers(text: str) -> list[str]:
    """2. 010으로 시작하는 휴대폰 번호 추출 (구분자: -, ., 공백 허용 / 자릿수 부족 및 지역번호 제외)"""
    pattern = r"\b010[-.\s]\d{4}[-.\s]\d{4}\b"
    return re.findall(pattern, text)


def students(text: str) -> list[tuple[str, str]]:
    """3. 본교 재학생(202로 시작하는 9자리 학번) 학번과 학과를 (학번, 학과) 튜플로 추출"""
    pattern = r"\[(202\d{6})\s*/\s*([^\]]+)\]"
    matches = re.findall(pattern, text)
    return [(student_id, dept.strip()) for student_id, dept in matches]


def github_coupons(text: str) -> tuple[list[str], list[str]]:
    """4. GitHub 저장소 URL(gitlab 제외) 및 2026년 유효 쿠폰 코드 추출"""
    github_pattern = r"https?://github\.com/[^\s]+"
    coupon_pattern = r"\bFEST-2026-[A-Z0-9]{4}\b"

    github_urls = re.findall(github_pattern, text)
    valid_coupons = re.findall(coupon_pattern, text)
    return github_urls, valid_coupons


def sales_summary(text: str) -> tuple[list[int], int]:
    """5. 부스별 총 매출액 추출(세부 내역 및 쿠폰 금액 제외) 및 전체 합산"""
    pattern = r"매출:\s*([0-9,]+)원"
    raw_amounts = re.findall(pattern, text)

    sales_list = [int(amount.replace(",", "")) for amount in raw_amounts]
    total_sales = sum(sales_list)
    return sales_list, total_sales