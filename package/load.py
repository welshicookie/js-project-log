from pathlib import Path


def loader(file_path: str | Path) -> str:
    """지정된 경로의 로그 파일을 읽어 문자열로 반환합니다."""
    path = Path(file_path)
    return path.read_text(encoding="utf-8")