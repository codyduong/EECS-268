"""
Author: Cody Duong
KUID: 3050266
Date: 2022-03-07
Lab: lab05
Last modified: 2022-09-23
Purpose: Lists and strings web navigator.

This is code adapated originally written for the EECS168 equivalent.
"""

import os.path
import sys
from typing import TypeVar
from .linked_list import LinkedList
from .typingx import Self

Self = TypeVar("Self", bound="History")


class History:
    def __init__(self: Self):
        self._buffer = LinkedList()
        # init at -1, as default failcase
        self.index = 0
        self.COMMANDS = {
            "NAVIGATE": self.navigate,
            "BACK": self.back,
            "FORWARD": self.forward,
            "HISTORY": self.history,
            "EXIT": self.__exit,
        }

    def navigate(self: Self, url: str = None) -> None:
        """
        Navigate to a url

        :param url: string to navigate to
        """
        if url is None or url == "":
            print("A url is a required parameter for NAVIGATE")
            return
        if self.index != len(self._buffer):
            self._buffer = self._buffer[: self.index + 1] + LinkedList(url)
        else:
            self._buffer.append(url)
        self.forward()

    def back(self: Self) -> None:
        """
        Goes back in history
        """
        self.index -= 1 if self.index > 0 and len(self._buffer) > 1 else 0

    def forward(self: Self) -> None:
        """
        Goes forward in history
        """
        history_len = len(self._buffer) - 1  # 0 indiced
        self.index += 1 if history_len > self.index and self.index != history_len else 0

    def __exit(self: Self) -> None:
        """
        Exits the program
        .. deprecated:: 1.0.0
            Not a requirement in this lab
        """
        sys.exit(0)

    def history(self) -> None:
        """
        Displays the current history
        """
        list_history = "\n".join(
            iter(
                LinkedList(
                    *iter(
                        f'{f"{url}":<24}{"  <==current" if index == self.index else ""}'.rstrip()
                        for index, url in enumerate(self._buffer)
                    )
                )
            )
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
        """
        Input a command

        :param command: Command to use, supported commands 'NAVIGATE', 'BACK', 'FORWARD', 'HISTORY', 'EXIT'
        :param *argv: Superfluous arguments to pass to command function
        """
        command_upper = command.upper()
        if command_upper not in LinkedList(
            "NAVIGATE", "BACK", "FORWARD", "HISTORY", "EXIT"
        ):
            print(f"Invalid command '{command_upper}'.\nIgnoring and continuing...")
        else:
            try:
                self.COMMANDS[command_upper](*argv)
            except TypeError:
                print(
                    f"Invalid command '{command_upper}' with invalid arguments: {argv}\nIgnoring and continuing..."
                )

    def prompt_file_input(self: Self) -> None:
        """Prompt the user for a file to read history from"""

        file_name = input("Enter the name of the input file (exercise1_input.txt): ")
        if file_name == "":
            file_name = "exercise1_input.txt"
        while not os.path.isfile(file_name):
            file_name = input(
                "File was not found, please try again (exercise1_input.txt): "
            )
            if file_name == "":
                file_name = "exercise1_input.txt"
        with open(file_name, encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                # I think split uses a list built-in? Is this allowed. w/e...
                self.input_command(*line.strip().split(" "))
