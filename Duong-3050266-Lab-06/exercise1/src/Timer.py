"""
Author: Cody Duong
KUID: 3050266
Date: 2022-10-23
Lab: lab03
Last modified: 2022-10-23
Purpose: Helper timer class
"""


import time
from typing import TypeVar
from .typingx import Self  # type: ignore
Self = TypeVar("Self", bound="Timer")

class Timer:
  def __init__(self) -> None:
    self.start_time: int | None = None
    self.end_time: int | None = None

  def start(self: Self) -> Self:
    if (self.start_time):
      raise ValueError("This timer instance has already started")
    self.start_time = time.process_time_ns()
    return self

  def end(self: Self) -> Self:
    if (self.end_time):
      raise ValueError("This timer instance has already ended")
    self.end_time = time.process_time_ns()
    return self

  def get_time(self) -> int:
    if (self.end_time and self.start_time):
      return self.end_time - self.start_time
    else:
      raise ValueError(f"This timer instance has not {'started' if not self.start_time else 'ended'}")

  def reset(self: Self) -> Self:
    self.start_time = None
    self.end_time = None
    return self
    