"""
Author: Cody Duong
KUID: 3050266
Date: 2022-11-14
Lab: lab09
Last modified: 2022-11-14
Description: Max heap type compliance
"""

# https://github.com/python/typing/issues/59
# tldr: stole this implementation lol
import typing
from typing import Any
from typing_extensions import Protocol
from abc import abstractmethod

C = typing.TypeVar("C", bound="Comparable")


class Comparable(Protocol):
    @abstractmethod
    def __eq__(self, other: Any, /) -> bool:
        pass

    @abstractmethod
    def __lt__(self: C, other: C, /) -> bool:
        pass

    @abstractmethod
    def __gt__(self: C, other: C, /) -> bool:
        pass

    @abstractmethod
    def __le__(self: C, other: C, /) -> bool:
        pass

    @abstractmethod
    def __ge__(self: C, other: C, /) -> bool:
        pass
