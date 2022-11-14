"""
Author: Cody Duong
KUID: 3050266
Date: 2022-10-30
Lab: lab07
Last modified: 2022-10-30
Purpose: Pokemon
"""


from typing import Any


class Pokemon:
    def __init__(self, i: int | str, name_EN: str, name_JP: str) -> None:
        self.id: int = int(i)
        self.name_EN: str = name_EN
        self.name_JP: str = name_JP

    def __lt__(self, other: Any) -> bool:
        return self.id < other.id

    def __gt__(self, other: Any) -> bool:
        return self.id > other.id

    def __eq__(self, other: Any) -> bool:
        return self.id == other.id

    def __str__(self) -> str:
        return (
            f"(US name: {self.name_EN:<24} JP name: {self.name_JP:<24} id: {self.id})"
        )

    # def __repr__(self) -> str:
    #     """
    #     Ignore superfluous info in repr
    #     """

    #     return f"{self.id}"
