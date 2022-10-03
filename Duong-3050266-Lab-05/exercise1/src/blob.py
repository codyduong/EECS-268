"""
Author: Cody Duong
KUID: 3050266
Date: 2022-10-03
Lab: lab05
Last modified: 2022-10-03
Purpose: blob spreading thing
"""

from enum import Enum
import os
from re import L
from typing import Annotated, Generic, List, Tuple, TypeVar, Union
from exercise1.src.assertx import assertx
from exercise1.src.typingx import Self


class Direction(Enum):
    """
    A directionallity enum, assuming the top-left is [0,0]

    Index order is [column][row]
    """

    UP = [0, -1]
    RIGHT = [1, 0]
    DOWN = [0, 1]
    LEFT = [-1, 0]


Rows = TypeVar("Rows")
Columns = TypeVar("Columns")


class Blob(Generic[Rows, Columns]):
    def __init__(
        self: Self,
        map_state: Annotated[List[Annotated[List, Columns]], Rows],
        blob_location: Tuple[int, int],
    ) -> Self:
        """
        Initialize the blob by asking the user for a file
        """
        pass

    def __process_step(
        blob_map_state: Annotated[List[Annotated[List, Columns]], Rows],
        blob_location: Tuple[int, int],
        steps: Union[int, None] = None,
    ) -> None:
        """
        The recursive function used for processing blob spread
        """
        for d in Direction:
            pass

    def step():
        """
        Runs one iteration of the blob spreading
        """
        pass

    def run():
        """
        Runs all the iterations of the blob spreading
        """
        pass

    @staticmethod
    def prompt_file() -> Tuple[Annotated[List[Annotated[List, Columns]], Rows], Tuple[int, int]]:
        """
        Static method for prompting user for a specific input file, and parses it, should be passed into the initializer
        of the blob class. Exceptions should be handled externally.

        :return: tuple of [map_state, blob_location]
        :example:
          blob = Blob(*Blob.prompt_file())
        """
        file_name = input("Enter the name of the input file (tests/mocks/input1.txt): ")
        if file_name == "":
            file_name = "tests/mocks/input1.txt"
        while not os.path.isfile(file_name):
            file_name = input(
                "File was not found, please try again (tests/mocks/input1.txt): "
            )
            if file_name == "":
                file_name = "tests/mocks/input1.txt"
        with open(file_name, encoding="utf-8") as f:
            all_lines = f.readlines()
            metadata = all_lines[:2:]

            rows, cols = metadata[0].split(" ")
            if len(metadata[0]) > 2:
                print(
                    "Received more row/column arguments than expected, disregarding superfluous arguments"
                )
            rows, cols = int(rows), int(cols)
            assertx(not rows < 1, ValueError, f"Expected rows to be >= 1, received: {rows}")
            assertx(
                not cols < 1, ValueError, f"Expected columns to be >= 1, received: {cols}"
            )

            map_state_raw = all_lines[2::]
            map_state = [[None] * cols] * rows
            for row_index, row in enumerate(map_state_raw):
                for col_index, value in enumerate(row.strip()):
                    print((row_index, col_index, value))
                    try:
                        print(map_state[row_index][col_index])
                        map_state[row_index][col_index] = value
                        print(map_state[row_index][col_index])
                    except IndexError:
                        raise IndexError(
                            f"Row/Column metadata mismatch, tried to access point at [{row_index}, {col_index}], but is out of specified bounds"
                        )

            blob_location = metadata[1].split(" ")
            if len(blob_location) > 2:
                print(
                    "Recieved more blob location arguments than expected, disregarding superfluous arguments"
                )
            blob_location = [int(blob_location[0]), int(blob_location[1])]

            return [map_state, blob_location]
