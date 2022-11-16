"""
Author: Cody Duong
KUID: 3050266
Date: 2022-11-16
Lab: lab09
Last modified: 2022-11-16
Description: Patient Class
"""

from typing import Any, TypeVar


Patient = TypeVar("Patient", bound="Patient")


class Patient:
    """Patient with immutable properties"""

    def __init__(
        self, f_name: str, l_name: str, age: int, illness: str, severity: int
    ) -> None:
        self._f_name: str = f_name
        self._l_name: str = l_name
        self._age: int = age
        self._illness: str = illness
        self._severity: int = severity

    @property
    def f_name(self) -> str:
      return self._f_name

    @property
    def l_name(self) -> str:
      return self._l_name

    @property
    def age(self) -> int:
      return self._age

    @property
    def illness(self) -> str:
      return self._illness

    @property
    def severity(self) -> int:
      return self._severity

    @staticmethod
    def parseLine(line: list[str]) -> Patient:
        """
        Parses a line and returns a patient, assumes a list of the following type:

        [str, str, str, str, str] <=> [f_name, l_name, age, illness, severity]
        """
        return Patient(line[0], line[1], int(line[2]), line[3], int(line[4]))

    def __eq__(self, other: Patient | Any) -> bool:
        if (isinstance(other, Patient)):
          return self._severity == other._severity
        return False

    def __lt__(self, other: Patient) -> bool:
      return self._severity < other._severity

    def __le__(self, other: Patient) -> bool:
      return self._severity <= other._severity

    def __gt__(self, other: Patient) -> bool:
      return self._severity > other._severity

    def __ge__(self, other: Patient) -> bool:
      return self._severity >= other._severity
