"""
Author: Cody Duong
KUID: 3050266
Date: 2022-09-22
Lab: lab03
Last modified: 2022-09-22
Purpose: Typing extension, safely import typing modules and fail without blowing up runtime if python version isn't 3.11^ IIRC
"""

Self = None
TypeGuard = None

try:
    from typing import Self  # pyright: ignore
except ImportError:
    pass

try:
    from typing import TypeGuard  # pyright: ignore
except ImportError:
    pass
