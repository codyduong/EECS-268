"""
Author: Cody Duong
KUID: 3050266
Date: 2022-10-30
Lab: lab07
Last modified: 2022-10-30
Purpose: Pokedex
"""


import os
from typing import Union

from src.BinarySearchTreeNode import BinarySearchTreeNode
from src.BinarySearchTree import BinarySearchTree
from src.Pokemon import Pokemon


class Pokedex(BinarySearchTree[Pokemon]):
    def __init__(
        self, pokedex: Union[BinarySearchTreeNode[Pokemon], None] = None
    ) -> None:
        super().__init__()

        self._root_node = pokedex or Pokedex.prompt_pokedex()

    @staticmethod
    def prompt_pokedex() -> BinarySearchTreeNode[Pokemon]:
        """
        Reads the input file
        """

        file_name: str = input("Enter the name of the pokedex file (pokedex.txt): ")
        if file_name == "":
            file_name = "pokedex.txt"
        while not os.path.isfile(file_name):
            # raise ValueError("Invalid file")
            file_name = input("File was not found, please try again (pokedex.txt): ")
            if file_name == "":
                file_name = "pokedex.txt"

        pokedex: BinarySearchTree[Pokemon] = BinarySearchTree()
        with open(file_name, encoding="utf-8") as f:
            for line in f.readlines():
                name_EN, i, name_JP = line.strip().split("\t")
                pokedex.add(Pokemon(i, name_EN, name_JP))

        return pokedex._root_node  # type: ignore

    def search(
        self,
        value: int,
        *_,
        current_node: Union[BinarySearchTreeNode[Pokemon], None] = None
    ) -> Union[BinarySearchTreeNode[Pokemon], None]:
        """
        Overload the base binary tree function
        """
        return super().search(value, "id", current_node=current_node)
