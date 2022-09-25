"""
Author: Cody Duong
KUID: 3050266
Date: 2022-09-25
Lab: lab04
Last modified: 2022-09-25
Purpose: Recursive Power Function
"""
import functools
from typing import TypeVar


Self = TypeVar("Self", bound="RecursivePower")
try:
    from typing import Self
except ImportError:
    pass


class RecursivePower:
    def __init__(self):
        pass

    @functools.cache
    def recursive_power(self: Self, base: int, power: int) -> int:
        """
        Return the base^power

        :param base: any int
        :param power: any int >= 0
        :return: int, result of base^power
        """
        return (
            base
            if power == 1
            else self.recursive_power(base, power - 1) * base
            if power != 0
            else 1
        )

    def prompt(self: Self) -> None:
        """Prompt the user for a base and power"""
        base = None  # type: int
        power = None  # type: int

        while True:
            try:
                base = input("Enter a base: ")
                base = int(base)
                if isinstance(base, int):
                    break
            except Exception as e:
                print(f"There was an error, try again!\n {e}")

        while True:
            try:
                power = input("Enter a power: ")
                power = int(power)
                if power < 0:
                    print("Sorry, your exponent must be zero or larger.")
                elif power >= 0 and isinstance(power, int):
                    break
            except Exception as e:
                print(f"There was an error, try again!\n {e}")

        print(f"Answer: {self.recursive_power(base, power)}")


if __name__ == "__main__":
    RecursivePower().prompt()
