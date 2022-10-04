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
from typing import (
    List,
    Tuple,
    TypedDict,
    Union,
)
from exercise1.src.assertx import assertx
from exercise1.src.typingx import Self


class Directions(Enum):
    """
    A directionallity enum, assuming the top-left is [0,0]

    Index order is [column][row]
    """

    UP = [-1, 0]
    RIGHT = [0, 1]
    DOWN = [1, 0]
    LEFT = [0, -1]


DIRECTION_OPPOSITE_MAP = {
    Directions.UP: Directions.DOWN,
    Directions.RIGHT: Directions.LEFT,
    Directions.DOWN: Directions.UP,
    Directions.LEFT: Directions.RIGHT,
}


class Blob:
    class ProcessedInput(TypedDict):
        map_state: List[List[int]]
        blob_location: Tuple[int, int]

    def __init__(
        self: Self,
        map_state: List[List[int]],
        blob_location: Tuple[int, int],
        debug: bool = False,
    ) -> Self:
        """
        Initialize the blob with a map_state and blob_location
        """
        self.map_state: List[List[int]] = map_state

        blob_row, blob_col = blob_location

        # The blob can only spawn on a `S` or `P`
        blob_spawn_value = map_state[blob_row][blob_col]
        assertx(
            blob_spawn_value in ["P", "S"],
            ValueError,
            f"The blob must be spawned within a valid point either in a street, or on a person,\nreceived col: {blob_col}, row: {blob_row}, {map_state[blob_col][blob_row]}",
        )
        self.map_state[blob_row][blob_col] = "B"
        self.blob_starting_pos = blob_location
        self.people_eaten: int = 1 if blob_spawn_value == "P" else 0
        self.sewers: List[Tuple[int, int]] = self._find_sewers()
        self.debug = debug

    def run(self: Self, debug: bool = False) -> None:
        """
        Run the blob spreading program
        """
        self._spread()
        print(self.state_to_str())

    def _spread(
        self: Self,
        blob_location: Union[Tuple[int, int], None] = None,
    ) -> None:
        """
        The recursive function used for processing blob spread

        :param blob_location: The current blob location to process spread from
        """
        if blob_location is None:
            blob_location = self.blob_starting_pos

        for d in Directions:
            blob_row, blob_col = blob_location
            col, row = blob_col + d.value[0], blob_row + d.value[1]
            printable_map = self.state_to_str()
            try:
                # prevent wraparound cases
                if col < 0 or row < 0:
                    raise IndexError("No wraparound!")
                if self.map_state[row][col] == "#":
                    continue
                if self.map_state[row][col] == "B":
                    continue
                if self.map_state[row][col] == "S":
                    self.map_state[row][col] = "B"
                    if self.debug:
                        print(printable_map)
                    self._spread((row, col))
                    continue
                if self.map_state[row][col] == "P":
                    self.map_state[row][col] = "B"
                    if self.debug:
                        print(printable_map)
                    self._spread((row, col))
                    self.people_eaten += 1
                    continue
                if self.map_state[row][col] == "@":
                    every_other_sewer = self.sewers
                    every_other_sewer.remove((row, col))
                    # start blob spread at every other sewer
                    for sewer in every_other_sewer:
                        self._spread(sewer)
            except IndexError:
                pass

    def _find_sewers(self: Self) -> List[Tuple[int, int]]:
        """
        Returns location of all the sewers in the current map
        """
        sewers_at = []
        for row_i, row in enumerate(self.map_state):
            for col_i in range(len(row)):
                if self.map_state[row_i][col_i] == "@":
                    sewers_at.append((row_i, col_i))
        return sewers_at

    def state_to_str(self: Self) -> str:
        """Converts the current state to a string for easy printing"""
        return (
            "\n"
            + "\n".join(["".join(row) for row in self.map_state])
            + "\n"
            + f"Total eaten: {self.people_eaten}"
        )

    @staticmethod
    def prompt_file() -> ProcessedInput:
        """
        Static method for prompting user for a specific input file, and parses it, should be passed into the initializer
        of the blob class. Exceptions should be handled externally.

        :return: dict of {"map_state": map_state, "blob_location": blob_location}
        :example:
          blob = Blob(**Blob.prompt_file())
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

            rows_and_cols = metadata[0].split(" ")
            if len(rows_and_cols) > 2:
                print(
                    "Received more row/column arguments than expected, disregarding superfluous arguments"
                )
            rows, cols = int(rows_and_cols[0]), int(rows_and_cols[1])
            assertx(
                rows >= 1, ValueError, f"Expected rows to be >= 1, received: {rows}"
            )
            assertx(
                cols >= 1,
                ValueError,
                f"Expected columns to be >= 1, received: {cols}",
            )

            map_state_raw = all_lines[2::]
            map_state = [list(range(cols)) for _ in range(rows)]
            for row_index, row in enumerate(map_state_raw):
                for col_index, value in enumerate(row.strip()):
                    # print(row_index, col_index)
                    try:
                        map_state[row_index][col_index] = value
                    except IndexError:
                        raise IndexError(
                            f"Metadata mismatch, tried to set value at col: {col_index}, row: {row_index},\nbut is out of specified bounds, max allowable row: {rows-1}, max allowable col: {cols-1}"
                        )

            blob_location = metadata[1].split(" ")
            if len(blob_location) > 2:
                print(
                    "Recieved more blob location arguments than expected, disregarding superfluous arguments"
                )

            blob_location = (int(blob_location[0]), int(blob_location[1]))

            return {"map_state": map_state, "blob_location": blob_location}
