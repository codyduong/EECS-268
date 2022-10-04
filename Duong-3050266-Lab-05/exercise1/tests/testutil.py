from typing import List


def text_str(s: str) -> str:
    return f"exercise1/tests/mocks/{s}.txt"


def str_to_matrix(s: str) -> List[List[int]]:
    return [[*i] for i in s.split("\n")]  # pyright: ignore
