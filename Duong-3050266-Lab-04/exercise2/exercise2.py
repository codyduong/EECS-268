"""
Author: Cody Duong
KUID: 3050266
Date: 2022-02-09
Lab: lab04
Last modified: 2022-09-25
Purpose: "Outbreak!"

This is a modified version of the original lab in 168, which I already used a recursive function for.
"""

import functools


@functools.cache
def get_sick_number(day_num: int) -> int:
    """
    Get the number of sick people on a day

    :param day_num: day number
    :return: # of sick people
    """

    if not isinstance(day_num, int):
        raise TypeError(f"Invalid day type, expected: int, received: {type(day_num)}")
    if day_num <= 0:
        raise ValueError(f"Invalid day number, expected >= 0, received: {day_num}")
    if day_num == 1:
        return 6
    elif day_num == 2:
        return 20
    elif day_num == 3:
        return 75
    else:
        return (
            get_sick_number(day_num - 1)
            + get_sick_number(day_num - 2)
            + get_sick_number(day_num - 3)
        )


if __name__ == "__main__":
    day_num: int = int(
        input("OUTBREAK!\nWhat day do you want a sick count for?: ").strip()
    )
    infected: int = get_sick_number(day_num)
    # print([get_sick_number(d) for d in range(1, day_num)])
    print(f"Total people with flu: {infected}")
