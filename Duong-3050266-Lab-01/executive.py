
"""
Author: Cody Duong
KUID: 3050266
Date: 2022-08-30
Lab: lab01
Last modified: 2022-08-30
Purpose: Handles executive functions of lab1
"""

from functools import lru_cache
from boardgame import Boardgame, BoardgameBuilder
from typing import Callable, NoReturn, List, TypeVar
import sys
# from typing import Self
# compatibility alias
Self = TypeVar("Self", bound="Executive")


class Executive:
    def __init__(self: Self, file_name: str) -> Self:
        self._COMMANDS = {
            "Print all games highest Gibbons range to lowest": self.__get_games_by_rating_gibbons,
            "Print all games from a year": self.__get_games_year,
            "Time for a game?": self.__get_games_suitable_time,
            "The People VS Dr. Gibbons ": self.__get_games_by_rating_seperation,
            "Print based on ranking ": self.__get_games_by_rating_greater,
            "Exit the program": self.__quit,
        }

        with open(file_name, encoding="utf-8") as f:
            self._boardgames = BoardgameBuilder.parse_raw_input(f.read())

    @property
    def boardgames(self: Self) -> List[Boardgame]:
        return self._boardgames

    def run(self: Self) -> NoReturn:
        try:
            while True:
                enumerated_commands = enumerate(self._COMMANDS.items())
                formatted_commands = [
                    f"{i+1}) {name}" for i, (name, _) in enumerated_commands
                ]
                reformatted_commands = [
                    command for _, command in self._COMMANDS.items()
                ]
                reformatted_commands_dict = {
                    name.lower(): command for name, command in self._COMMANDS.items()
                }
                print("\n".join(formatted_commands))
                command_input = input("What would you like to do?: ")
                try:
                    command_index = int(command_input)
                    try:
                        if (not command_index - 1 < 0):
                            reformatted_commands[command_index - 1]()
                        else:
                            raise IndexError
                    except IndexError:
                        print("Not an available command! Try again.\n")
                except ValueError:
                    cleaned_input = command_input.lower().strip()
                    try:
                        reformatted_commands_dict[cleaned_input]()
                    except KeyError:
                        print("Not an available command! Try again.\n")
        except KeyboardInterrupt:
            sys.exit(1)

    @staticmethod
    def __pretty_print_boardgame(b: Boardgame) -> str:
        b_stringified_list = str(b).split(' ')
        print(
            f"{b_stringified_list[0].ljust(64)} {b_stringified_list[1].ljust(6)} {''.join(map(lambda s: s.rjust(12),b_stringified_list[2::]))}")

    @staticmethod
    def __rebuild_boardgame(filter: str) -> Boardgame:
        return lambda b: b.set_sort_filter(filter)

    @lru_cache(maxsize=None)
    def __rebuild_boardgames(self: Self, filter: str) -> List[Boardgame]:
        return list(map(Executive.__rebuild_boardgame(filter), self._boardgames))

    @staticmethod
    def __filter_boardgames(b: List[Boardgame], f: Callable[[Boardgame], bool]) -> NoReturn:
        matching_boardgames = [boardgame for boardgame in b if f(boardgame)]
        if (len(matching_boardgames) > 0):
            for boardgame in matching_boardgames:
                Executive.__pretty_print_boardgame(boardgame)
            else:
                print("\n")
        else:
            print("No matches found!\n")

    def __get_games_by_rating_gibbons(self: Self) -> NoReturn:
        boardgame_new_filter = self.__rebuild_boardgames("gibbons_rating")
        boardgame_new_filter.sort(reverse=True)
        for boardgame in boardgame_new_filter:
            Executive.__pretty_print_boardgame(boardgame)
        else:
            print("\n")

    def __get_games_year(self: Self) -> NoReturn:
        year = int(input("What year would you like to search for? "))
        Executive.__filter_boardgames(
            self._boardgames, lambda b: b.year == year)

    def __get_games_suitable_time(self: Self) -> NoReturn:
        rebuilt_boardgames = self.__rebuild_boardgames("max_playtime")
        rebuilt_boardgames.sort()
        time = float(input("How much time do you have to play a boardgame? "))
        Executive.__filter_boardgames(
            rebuilt_boardgames, lambda b: b.max_playtime <= time)

    def __get_games_by_rating_seperation(self: Self) -> NoReturn:
        rating = float(
            input("How much of a rating discrepancy are you searching for? "))
        while (not 0 <= rating <= 10):
            print("Rating must be between [0, 10], try again...")
            rating = float(
                input("How much of a rating discrepancy are you searching for? "))
        else:
            Executive.__filter_boardgames(self._boardgames, lambda b: abs(
                b.public_rating - b.gibbons_rating) >= abs(rating))

    def __get_games_by_rating_greater(self: Self) -> NoReturn:
        time = float(input("What rating or greater are you looking for? "))
        Executive.__filter_boardgames(
            self._boardgames, lambda b: b.public_rating >= time)

    def __quit(self: Self) -> NoReturn:
        sys.exit(0)
