"""
Author: Cody Duong
KUID: 3050266
Date: 2022-08-30
Lab: lab01
Last modified: 2022-08-30
Purpose: Contains classes to deal with boardgame properties
"""

from typing import NoReturn, Tuple, TypeVar

# from typing import Self
# compatibility alias
Self = TypeVar("Self", bound="Boardgame")

# Tuple is imported for compat reasons
T = Tuple[str, str, float, float, int, int]


class Boardgame:
    """
    A Boardgame class with readonly properties
    """

    def __init__(self, T: T):
        self._filter = "name"
        properties = [
            "name",
            "year",
            "gibbons_rating",
            "public_rating",
            "min_players",
            "max_playtime",
        ]
        for i, property in enumerate(properties):
            self.__assign(f"_{property}", T[i])

    def __assign(self: Self, s: str, v: any) -> NoReturn:
        setattr(self, s, v)

    @property
    def name(self: Self) -> str:
        return self._name

    @property
    def year(self: Self) -> int:
        return self._year

    @property
    def gibbons_rating(self: Self) -> float:
        return self._gibbons_rating

    @property
    def public_rating(self: Self) -> float:
        return self._public_rating

    @property
    def min_players(self: Self) -> int:
        return self._min_players

    @property
    def max_playtime(self: Self) -> int:
        return self._max_playtime

    def set_sort_filter(self: Self, filter: str) -> Self:
        if getattr(self, filter) is not None:
            self._filter = filter
            return self
        else:
            raise Exception("Failed to resolve filter")

    def __lt__(self: Self, other: Self) -> bool:
        return self[self._filter] < other[self._filter]

    def __le__(self: Self, other: Self) -> bool:
        return self[self._filter] <= other[self._filter]

    def __gt__(self: Self, other: Self) -> bool:
        return self[self._filter] > other[self._filter]

    def __ge__(self: Self, other: Self) -> bool:
        return self[self._filter] >= other[self._filter]

    def __eq__(self: Self, other: Self) -> bool:
        return self[self._filter] == other[self._filter]

    def __ne__(self: Self, other: Self) -> bool:
        return self[self._filter] != other[self._filter]

    def __getitem__(self: Self, key: str) -> any:
        return getattr(self, key)

    def __str__(self: Self) -> str:
        return f"{self.name} ({self.year}) [GR={self.gibbons_rating}, PR={self.public_rating}, MP={self.min_players}, MT={self.max_playtime}]"


class BoardgameBuilder:
    """
    A builder class for Boardgames
    """

    def __init__() -> NoReturn:
        pass

    # Surely this is an antipattern? w/e
    @staticmethod
    def __parse_row(r: str) -> T:
        p = r.split("\t")
        # The .tsv download is different from the format specified...
        # 2.) Dr. Gibbons changed the input file given to match the format given on the lab wiki like the following.
        # <name> <gibbons-rating> <people's rating> <year published> <min players> <max playtime> 
        return Boardgame(
            [str(p[0]), int(p[3]), float(p[1]), float(p[2]), int(p[4]), int(p[5])]
        )

    @staticmethod
    def parse_raw_input(s: str) -> Tuple[Boardgame]:
        return tuple(map(BoardgameBuilder.__parse_row, s.split("\n")))
