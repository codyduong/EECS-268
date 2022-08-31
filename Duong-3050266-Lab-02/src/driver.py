
"""
Author: Cody Duong
KUID: 3050266
Date: 2022-08-31
Lab: lab02
Last modified: 2022-08-31
Purpose: Program entrypoint
"""

from typing import NoReturn
from .cpu_scheduler import CPUScheduler


def main() -> NoReturn:
    file_name = input(
        "Enter the name of the input file (default: entry.txt): ")
    cpu = CPUScheduler()
    with open(file_name  or "entry.txt", encoding="utf-8") as f:
        cpu.run(f.read())


if __name__ == "__main__":
    main()
