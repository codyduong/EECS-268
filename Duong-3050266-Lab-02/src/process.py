from .stack import Stack
from .node import Node

class Process:
    _callstack = None

    def __init__(self, s):
        """ Takes in a process name, ie. itunes"""
        self._processname = s
        self._callstack = Stack(Node("main"))
    
    @property
    def processname(self):
        return self._processname

    @property
    def callstack(self):
        return self._callstack

    def add(self, s):
        self._callstack.push(s)

    def empty_check(self):
        if self._callstack.is_empty():
            print(f"{self.processname} process has ended")
        
    def call(self):
        print(f"{self.processname} calls {self._callstack.pop()}")
        self.empty_check()
        
    def returns(self):
        print(f"{self.processname} returns from {self._callstack.pop()}")
        self.empty_check()