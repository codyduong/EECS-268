"""
Author: Cody Duong
KUID: 3050266
Date: 2022-08-30
Lab: lab01
Last modified: 2022-08-30
Purpose: Program entrypoint
"""

from typing import NoReturn
from executive import Executive


def main() -> NoReturn:
    file_name = input("Enter the name of the input file: ")
    my_exec = Executive(file_name or "gibbons_collection.tsv")
    my_exec.run()


if __name__ == "__main__":
    main()
