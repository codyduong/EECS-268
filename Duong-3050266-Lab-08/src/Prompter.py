import sys
from distutils.util import strtobool
from src.Pokedex import Pokedex
from src.Pokemon import Pokemon


class Prompter:
    """
    Prompts and handle commands for pokedex lab
    """

    def __init__(
        self,
        pokedex = None,
    ):
        self._pokedex: Pokedex = pokedex or Pokedex()
        self._copy_pokedex: Pokedex | None = None

    def _select_pokedex(self):
        if self._copy_pokedex:
            use_other: Literal[0, 1] = strtobool(
                input("Use the copied pokedex? (y/N): ") or "n".lower()
            )
            if use_other == 1:
                return self._copy_pokedex
        return self._pokedex

    def _search(self):
        current_pokedex: Pokedex = self._select_pokedex()
        search_id = int(input("Id to search for?: "))
        try:
            print(f"{current_pokedex.search(search_id).value}" + "\n")  
        except AttributeError:
            print(f"Could not find id: {search_id}" + "\n")
            return
        except Exception as e:
            print(f"Error: {e}, try again!")
            return

    def _add(self):
        current_pokedex: Pokedex = self._select_pokedex()
        i = None
        name_EN = None
        name_JP = None
        try:
            i = int(input("Pokemon id?: "))
            name_EN = input("Pokemon EN Name?: ")
            name_JP = input("Pokemon JP Name?: ")
        except Exception as e:
            print(f"An error occured: f{e}, please try again")
        try:
            to_add: Pokemon = Pokemon(i, name_EN, name_JP)  
            print(f"Adding {to_add}" + "\n")
            current_pokedex.add(to_add)
        except ValueError as e:
            # "I've listed this in phase 2 beacuse something that is now possible is for a Pokemon to be placed in the tree, then removed, then added again."
            print("No duplicates allowed. Skipping\n")

    def _print_preorder(self):
        current_pokedex: Pokedex = self._select_pokedex()
        for i in current_pokedex.preorder():
            print(i)

    def _print_inorder(self):
        current_pokedex: Pokedex = self._select_pokedex()
        for i in current_pokedex.inorder():
            print(i)

    def _print_postorder(self):
        current_pokedex: Pokedex = self._select_pokedex()
        for i in current_pokedex.postorder():
            print(i)

    def _print_prompt(self):
        print("Choose print order:\n1) Pre-order\n2) In-order\n3) Post-order")
        command = input("What would you like to do?: ").strip().lower()
        if command == "pre-order" or command == "1":
            self._print_preorder()
        elif command == "in-order" or command == "2":
            self._print_inorder()
        elif command == "post-order" or command == "3":
            self._print_postorder()
        else:
            print("Invalid print command.")

    def _quit(self):
        sys.exit(0)

    def _copy(self):
        if self._copy_pokedex is None:
            print("Copying pokedex...\n")
            self._copy_pokedex = self._pokedex.copy()
        else:
            print("There is already a copied pokedex... Skipping...\n")

    def _prompt_for_command(
        self, loop = True
    ):
        while True:
            print("Commands available:\n1) Add\n2) Search\n3) Print\n4) Remove\n5) Copy\n6) Quit")
            command = input("What would you like to do?: ").strip().lower()
            if command == "add" or command == "1":
                self._add()
            elif command == "search" or command == "2":
                self._search()
            elif command == "print" or command == "3":
                self._print_prompt()
            elif command == "remove" or command == "4":
                self._remove()
            elif command == "copy" or command == "5":
                self._copy()
            elif command == "quit" or command == "6":
                self._quit()
            else:
                print("Not an available command! Try again.")

            if not loop:
                break


    def run(self):
        self._prompt_for_command()

    def _remove(self):
        current_pokedex: Pokedex = self._select_pokedex()
        i = None
        try:
            i = int(input("Pokemon id to remove?: "))
        except Exception as e:
            print(f"An error occured: f{e}, please try again")
        print(f"Removed pokemon: {current_pokedex.search(i).value}" + "\n")  
        current_pokedex.remove(i)  
