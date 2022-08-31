
"""
Author: Cody Duong
KUID: 3050266
Date: 2022-08-31
Lab: lab02
Last modified: 2022-08-31
Purpose: Schedules processes
"""


from typing import TypeVar
from .process import Process
from .linkedqueue import LinkedQueue
Self = TypeVar("Self", bound="CPUScheduler")


class CPUScheduler:
    _linkedqueue: LinkedQueue = None

    def __init__(self: Self) -> Self:
        self._linkedqueue = LinkedQueue()

    def run(self: Self, s: str) -> None:
        print('')
        for row in s.split('\n'):
            command_tuple = row.split(' ')
            if command_tuple[0] == "START":
                self._linkedqueue.enqueue(Process(command_tuple[1]))
                print(f"{command_tuple[1]} added to queue")
            elif command_tuple[0] == "CALL":
                # adds a command then immediately calls it
                self._linkedqueue.peek_front().add(command_tuple[1])
                self._linkedqueue.peek_front().call()
                # have to move to end of queue now
                self._linkedqueue.enqueue(self._linkedqueue.dequeue())
            elif command_tuple[0] == 'RETURN':
                self._linkedqueue.dequeue().returns()
            else:
                print("Invalid Command")

        print("\nCPU has no more processes/functions scheduled")
