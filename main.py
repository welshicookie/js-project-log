from pathlib import Path
from package import (
    loader,
    valid_emails,
    phone_numbers,
    students,
    github_and_coupons,
    sales_summary,
)


def main() -> None:
    log_path = Path(__file__).parent / "data_log.txt"
    log_text = loader(log_path)

    emails = valid_emails(log_text)
    phones = phone_numbers(log_text)
    students_list = students(log_text)
    github_urls, coupons = github_and_coupons(log_text)
    sales_list, total_sales = sales_summary(log_text)

    print("=== [1] 유효한 이메일 목록 ===")
    print(emails, "\n")

    print("=== [2] 휴대폰 번호 목록 ===")
    print(phones, "\n")

    print("=== [3] 본교 재학생 (학번, 학과) 목록 ===")
    print(students_list, "\n")

    print("=== [4] GitHub 저장소 및 2026 유효 쿠폰 ===")
    print("GitHub URL:", github_urls)
    print("유효 쿠폰:", coupons, "\n")

    print("=== [5] 부스별 총 매출액 및 전체 합계 ===")
    print("부스별 매출:", [f"{s:,}원" for s in sales_list])
    print(f"전체 매출 합계: {total_sales:,}원")


if __name__ == "__main__":
    main()