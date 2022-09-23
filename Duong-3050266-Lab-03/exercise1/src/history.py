"""
Author: Cody Duong
KUID: 3050266
Date: 2022-03-07
Lab: lab05
Last modified: 2022-09-23
Purpose: Lists and strings web navigator.

This is code adapated originally written for the EECS168 equivalent.
"""

import sys
from typing import TypeVar
from .linked_list import LinkedList
from .typingx import Self

Self = TypeVar("Self", bound="History")

def history_input():
    """The existence of this function is purely to make mocking this easier"""
    return input("Enter the name of the input file (exercise1_input.txt): ")

class History:
    def __init__(self: Self):
        self.history = LinkedList()
        # init at -1, as default failcase
        self.currently_at_index = -1
        self.COMMANDS = {
            "NAVIGATE": self.__navigate,
            "BACK": self.__back,
            "FORWARD": self.__next,
            "HISTORY": self.__print_history,
            "EXIT": self.__exit,
        }

    def __navigate(self: Self, url: str = None) -> None:
        if url is None:
            print("A url is a required parameter for NAVIGATE")
            return
        if len(self.history) - 1 == self.currently_at_index:
            self.history.append(url)
        else:
            self.history = self.history[: self.currently_at_index + 1] + LinkedList(url)
        self.currently_at_index += 1

    def __back(self: Self) -> None:
        self.currently_at_index -= (
            1 if self.currently_at_index > 0 and len(self.history) > 1 else 0
        )

    def __next(self: Self) -> None:
        history_len = len(self.history) - 1  # 0 indiced
        self.currently_at_index += (
            1
            if history_len > self.currently_at_index
            and self.currently_at_index != history_len
            else 0
        )

    def __exit(self: Self) -> None:
        """
        .. deprecated:: 1.0.0
            Not a requirement in this lab
        """
        sys.exit(0)

    def __print_history(self) -> None:
        list_history = "\n".join(
            iter(LinkedList(*iter(
                f'{f"{url}":<24}{"  <==current" if index == self.currently_at_index else ""}'
                for index, url in enumerate(self.history)
            )))
        )
        print(
            f"""Oldest
===========
{list_history}
===========
Newest
"""
        )

    def input_command(self: Self, command: str, *argv) -> None:
        command_upper = command.upper()
        if command_upper not in LinkedList(
            "NAVIGATE", "BACK", "FORWARD", "HISTORY", "EXIT"
        ):
            print(f"Invalid command {command_upper}. Ignoring and continuing...")
        else:
            self.COMMANDS[command_upper](*argv)

    def prompt_file_input(self: Self) -> None:
        file_name = history_input()
        if file_name == "":
            file_name = "exercise1_input.txt"
        with open(file_name, encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                # I think split uses a list built-in? Is this allowed. w/e...
                self.input_command(*line.strip().split(" "))
