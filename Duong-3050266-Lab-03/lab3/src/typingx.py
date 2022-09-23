"""
Author: Cody Duong
KUID: 3050266
Date: 2022-09-22
Lab: lab03
Last modified: 2022-09-22
Purpose: Typing extension, safely import typing modules and fail without blowing up runtime
"""

Self = None
TypeGuard = None

try:
    from typing import Self
except ImportError:
    pass

try:
    from typing import TypeGuard
except ImportError:
    pass
