"""
Author: Cody Duong
KUID: 3050266
Date: 2022-10-31
Lab: lab07
Last modified: 2022-10-31
Purpose: Prompter
"""

import sys
from typing import Any, Callable, Dict, Union
from src.Pokemon import Pokemon
from src.Pokedex import Pokedex


class Prompter:
    """
    Prompts and handle commands for pokedex lab
    """

    def __init__(
        self,
        pokedex: Union[Pokedex, None] = None,
    ) -> None:
        self._pokedex: Pokedex = pokedex or Pokedex()

        self.COMMANDS: Dict[str, Callable[[], Any]] = {
            "Search": self._search,
            "Add": self._add,
            "Print": self._print_prompt,
            "Quit": self._quit,
        }
        self.PRINT_COMMANDS: Dict[str, Callable[[], Any]] = {
            "Print in Pre-order": self._print_preorder,
            "Print in In-order": self._print_inorder,
            "Print in Post-order": self._print_postorder,
        }

    def _search(self) -> None:
        search_id: int = int(input("Id to search for?: "))
        try:
            print(self._pokedex.search(search_id).value)  # type: ignore
        except Exception as e:
            print(f"Error: {e}, try again!")
            return

    def _add(self) -> None:
        i: int
        name_EN: str
        name_JP: str
        try:
            i = int(input("Pokemon id?: "))
            name_EN = input("Pokemon EN Name?: ")
            name_JP = input("Pokemon JP Name?: ")
        except Exception as e:
            print(f"An error occured: f{e}, please try again")
        try:
            self._pokedex.add(Pokemon(i, name_EN, name_JP))  # type: ignore
        except ValueError as e:
            raise RuntimeError(e)

    def _print_preorder(self) -> None:
        for i in self._pokedex.preorder():
            print(i)

    def _print_inorder(self) -> None:
        for i in self._pokedex.inorder():
            print(i)

    def _print_postorder(self) -> None:
        for i in self._pokedex.postorder():
            print(i)

    def _print_prompt(self) -> None:
        self._prompt_for_command(self.PRINT_COMMANDS, loop=False)

    def _quit(self) -> None:
        sys.exit(0)

    def _prompt_for_command(
        self, commands: Dict[str, Callable[[], Any]], loop: bool = True
    ) -> None:
        while True:
            enumerated_commands = enumerate(commands.items())
            formatted_commands = [
                f"{i+1}) {name}" for i, (name, _) in enumerated_commands
            ]
            reformatted_commands = [command for _, command in commands.items()]
            reformatted_commands_dict = {
                name.lower(): command for name, command in commands.items()
            }
            print("\n".join(formatted_commands))
            command_input = input("What would you like to do?: ")
            try:
                command_index = int(command_input)
                try:
                    reformatted_commands[command_index - 1]()
                except IndexError:
                    print("Not an available command! Try again.")
            except ValueError:
                cleaned_input = command_input.lower().strip()
                try:
                    reformatted_commands_dict[cleaned_input]()
                except KeyError:
                    print("Not an available command! Try again.")

            # this is extra dumb
            if not loop:
                break

    def run(self) -> None:
        self._prompt_for_command(self.COMMANDS)
