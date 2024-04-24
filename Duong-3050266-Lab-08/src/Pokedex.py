import os
from src.BinarySearchTree import BinarySearchTree, BinarySearchTreeNode
from src.Pokemon import Pokemon

class Pokedex(BinarySearchTree):
    def __init__(
        self, pokedex = None
    ) -> None:
        super().__init__()

        self._root_node = pokedex or Pokedex.prompt_pokedex()

    @staticmethod
    def prompt_pokedex():
        """
        Reads the input file
        """

        file_name = input("Enter the name of the pokedex file (pokedex.txt): ")
        if file_name == "":
            file_name = "pokedex.txt"
        while not os.path.isfile(file_name):
            # raise ValueError("Invalid file")
            file_name = input("File was not found, please try again (pokedex.txt): ")
            if file_name == "":
                file_name = "pokedex.txt"

        pokedex = BinarySearchTree()
        with open(file_name, encoding="utf-8") as f:
            for line in f.readlines():
                name_EN, i, name_JP = line.strip().split("\t")
                pokedex.add(Pokemon(i, name_EN, name_JP))

        return pokedex._root_node  

    def search(
        self,
        value,
        *_,
        current_node = None
    ):
        """
        Overload the base binary tree function
        """
        return super().search(value, "id", current_node=current_node)

    def remove(
        self,
        value,
        *_,
        current_node = None
    ):
        """
        Overload the base binary tree function
        """
        return super().remove(value, "id", current_node=current_node)

    def copy(
        self,
    ):
        return Pokedex(super().copy()._root_node)
