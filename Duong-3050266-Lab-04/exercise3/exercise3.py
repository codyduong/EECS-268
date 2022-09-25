"""
Author: Cody Duong
KUID: 3050266
Date: 2022-09-25
Lab: lab04
Last modified: 2022-09-25
Purpose: Fibonacci
"""
import functools
from typing import TypeVar


Self = TypeVar("Self", bound="Fibonacci")
try:
    from typing import Self
except ImportError:
    pass


class Fibonacci:
    """Class to determine Fibonacci numbers"""

    def __init__(self: Self) -> Self:
        pass

    @functools.cache
    def number_at(self: Self, n: int) -> int:
        """
        Checks the fibonacci number at n
        :param n: The nth fibonacci number
        :return: int of the resulting fibonacci number
        """
        if not isinstance(n, int):
            raise TypeError(f"Invalid type, expected: {int}, received: {type(n)}")
        if n < 0:
            raise ValueError(f"Expected n > {0}, received {n}")
        if n == 0:
            return 0
        elif n in [1, 2]:
            return 1
        else:
            return self.number_at(n - 1) + self.number_at(n - 2)

    def in_sequence(self: Self, n: int) -> bool:
        """
        Checks if a int `n` is a fibonacci value
        :param n: the value to check
        :return: bool of whether it is a fibonacci value
        """
        if not isinstance(n, int):
            raise TypeError(f"Invalid type, expected: {int}, received: {type(n)}")
        if n < 0:
            return False
        i = 0
        while True:
            fib_number = self.number_at(i)
            if fib_number == n:
                return True
            if fib_number > n:
                return False
            i += 1


Self = TypeVar("Self", bound="FibonacciPrompter")


class FibonacciPrompter:
    """Class to prompt user for input"""

    def __init__(self: Self):
        self._fibonacci = Fibonacci()

        self.FLAGS_LINK = {
            "-i": self._fibonacci.number_at,
            "-v": self.__in_sequence_pretty,
        }
        self.FLAGS = self.FLAGS_LINK.keys()

    def __in_sequence_pretty(self: Self, i: int) -> int:
        "Wrapper to pretty print True/False"
        number_in = self._fibonacci.in_sequence(i)
        return f"{i} is{' not ' if not number_in else ' '}in the sequence"

    def prompt(self):
        """
        Prompt the user a single time for a command
        """
        try:
            command = input("Enter mode and value: ")
            command_parts = command.split(" ")
            if len(command_parts) < 2:
                raise RuntimeError(
                    f"Not enough flags received: {2}, received: {len(command_parts)}"
                )
            if len(command_parts) > 2:
                raise RuntimeError(
                    f"More flags received than expected, expected: {2}, received: {len(command_parts)}"
                )
            mode = command_parts[0]
            value = command_parts[1]
            if mode not in self.FLAGS:
                raise RuntimeError(
                    f"Unsupported mode received, expected one of: {self.FLAGS}, received: {command_parts[0]}"
                )
            """This is already checked by int"""
            # if "." in value:
            #     raise RuntimeError(
            #         f"Unsupported value type recieved, expected type of: {int}, received: {float}"
            #     )
            print(self.FLAGS_LINK[mode](int(value)))
        except Exception as e:
            print(f"Error encountered, program terminated gracefully:\n{e}")


if __name__ == "__main__":
    FibonacciPrompter().prompt()
