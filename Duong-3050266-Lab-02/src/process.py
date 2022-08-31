
"""
Author: Cody Duong
KUID: 3050266
Date: 2022-08-31
Lab: lab02
Last modified: 2022-08-31
Purpose: Handles executive functions of lab2
"""


from .stack import Stack
from typing import TypeVar
from .node import Node
Self = TypeVar("Self", bound="Process")


class Process:
    _callstack: Stack = None

    def __init__(self: Self, s: str) -> Self:
        """ Takes in a process name, ie. itunes"""
        self._processname = s
        self._callstack = Stack(Node("main"))
    
    @property
    def processname(self: Self) -> str:
        return self._processname

    @property
    def callstack(self: Self) -> Stack:
        return self._callstack

    def add(self: Self, s: str) -> None:
        self._callstack.push(s)

    def empty_check(self: Self) -> None:
        if (self._callstack.is_empty()):
            print(f"{self.processname} process has ended")
        

    def call(self: Self) -> None:
        print(f"{self.processname} calls {self._callstack.pop()}")
        self.empty_check()
        
    def returns(self: Self) -> None:
        print(f"{self.processname} returns from {self._callstack.pop()}")
        self.empty_check()