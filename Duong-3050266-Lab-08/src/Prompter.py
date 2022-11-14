"""
Author: Cody Duong
KUID: 3050266
Date: 2022-10-31
Lab: lab08
Last modified: 2022-11-13
Purpose: Prompter
"""

import sys
from distutils.util import strtobool
from typing import Any, Callable, Dict, Literal, Union

from src.Pokedex import Pokedex
from src.Pokemon import Pokemon


class Prompter:
    """
    Prompts and handle commands for pokedex lab
    """

    def __init__(
        self,
        pokedex: Union[Pokedex, None] = None,
    ) -> None:
        self._pokedex: Pokedex = pokedex or Pokedex()
        self._copy_pokedex: Pokedex | None = None

        self.COMMANDS: Dict[str, Callable[[], Any]] = {
            "Search": self._search,
            "Add": self._add,
            "Print": self._print_prompt,
            "Copy": self._copy,
            "Remove": self._remove,
            "Quit": self._quit,
        }
        self.PRINT_COMMANDS: Dict[str, Callable[[], Any]] = {
            "Print in Pre-order": self._print_preorder,
            "Print in In-order": self._print_inorder,
            "Print in Post-order": self._print_postorder,
        }

    def _select_pokedex(self) -> Pokedex:
        if self._copy_pokedex:
            use_other: Literal[0, 1] = strtobool(
                input("Use the copied pokedex? (y/N): ") or "n".lower()
            )
            if use_other == 1:
                return self._copy_pokedex
        return self._pokedex

    def _search(self) -> None:
        current_pokedex: Pokedex = self._select_pokedex()
        search_id: int = int(input("Id to search for?: "))
        try:
            print(f"{current_pokedex.search(search_id).value}" + "\n")  # type: ignore
        except AttributeError:
            print(f"Could not find id: {search_id}" + "\n")
            return
        except Exception as e:
            print(f"Error: {e}, try again!")
            return

    def _add(self) -> None:
        current_pokedex: Pokedex = self._select_pokedex()
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
            to_add: Pokemon = Pokemon(i, name_EN, name_JP)  # type: ignore
            print(f"Adding {to_add}" + "\n")
            current_pokedex.add(to_add)
        except ValueError as e:
            # "I've listed this in phase 2 beacuse something that is now possible is for a Pokemon to be placed in the tree, then removed, then added again."
            print("No duplicates allowed. Skipping\n")

    def _print_preorder(self) -> None:
        current_pokedex: Pokedex = self._select_pokedex()
        for i in current_pokedex.preorder():
            print(i)

    def _print_inorder(self) -> None:
        current_pokedex: Pokedex = self._select_pokedex()
        for i in current_pokedex.inorder():
            print(i)

    def _print_postorder(self) -> None:
        current_pokedex: Pokedex = self._select_pokedex()
        for i in current_pokedex.postorder():
            print(i)

    def _print_prompt(self) -> None:
        self._prompt_for_command(self.PRINT_COMMANDS, loop=False)

    def _quit(self) -> None:
        sys.exit(0)

    def _copy(self) -> None:
        if self._copy_pokedex is None:
            print("Copying pokedex...\n")
            self._copy_pokedex = self._pokedex.copy()
        else:
            print("There is already a copied pokedex... Skipping...\n")

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

    def _remove(self) -> None:
        current_pokedex: Pokedex = self._select_pokedex()
        i: int
        try:
            i = int(input("Pokemon id to remove?: "))
        except Exception as e:
            print(f"An error occured: f{e}, please try again")
        print(f"Removed pokemon: {current_pokedex.search(i).value}" + "\n")  # type: ignore
        current_pokedex.remove(i)  # type: ignore
