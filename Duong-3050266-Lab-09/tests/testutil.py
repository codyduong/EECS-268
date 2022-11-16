from io import TextIOWrapper


def text_str(s: str) -> str:
    return f"tests/mocks/{s}.txt"


def read_text_str(s: str) -> TextIOWrapper:
    return open(f"tests/mocks/{s}.txt", encoding="utf8")


def text_number_tuple(i: int) -> tuple[str, TextIOWrapper]:
    return (text_str(f"input{i}"), read_text_str(f"output{i}"))
