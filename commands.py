"""
Author: Cody Duong
KUID: 3050266
Date: 2022-08-30
Lab: lab01
Last modified: 2022-08-31
Purpose: A command handler for requiring user input while providing number interface
"""

import sys
from typing import Dict, NoReturn, TypeVar
Self = TypeVar("Self", bound="CommandHandler")


class CommandHandler:
    """
    A command handler with immutable command list with built in runner
    """

    def __init__(self: Self, commands: Dict) -> Self:
        self._COMMANDS = commands
        ENUMERATED_COMMANDS = enumerate(self._COMMANDS.items())
        self._FORMATTED_COMANDS = [
            f"{i+1}) {name}" for i, (name, _) in ENUMERATED_COMMANDS
        ]
        self._REFORMATTED_COMMANDS = [
            command for _, command in self._COMMANDS.items()
        ]
        self._REFORMATTED_COMMANDS_DICT = {
            name.lower(): command for name, command in self._COMMANDS.items()
        }

    def run(self: Self) -> NoReturn:
        try:
            while True:
                print("\n".join(self._FORMATTED_COMANDS))
                command_input = input("What would you like to do?: ")
                try:
                    command_index = int(command_input)
                    try:
                        if (not command_index - 1 < 0):
                            self._REFORMATTED_COMMANDS[command_index - 1]()
                        else:
                            raise IndexError
                    except IndexError:
                        print("Not an available command! Try again.\n")
                except ValueError:
                    cleaned_input = command_input.lower().strip()
                    try:
                        self._REFORMATTED_COMMANDS_DICT[cleaned_input]()
                    except KeyError:
                        print("Not an available command! Try again.\n")
        except KeyboardInterrupt:
            sys.exit(1)
