"""
Author: Cody Duong
KUID: 3050266
Date: 2022-10-23
Lab: lab03
Last modified: 2022-10-23
Purpose: Generate timings and print to stdout for easy copy and paste into excel

  * LinkedList
  * LinkedQueue
  * Stack

More specifically
  * Popping a single item from a stack
  * Popping all items from a stack
  * Queue's enqueue
  * Linked List get_entry at specifically index 0
  * Linked List get_entry at specifically the last index
  * Printing all elements in a LinkedList using get_entry

"""

from typing import Any, List, Tuple, Union
from .LinkedList import LinkedList
from .LinkedListOptimized import LinkedListOptimized
from .LinkedQueue import LinkedQueue
from .Stack import Stack
from .Timer import Timer
import copy

TIMES_TYPE = List[Tuple[int, int]]


def generate_stack() -> List[Stack]:
    """
    Because of the way the references are setup internally within stack, it'll reference the same instance
    so we have to create a new list of stacks for each test (ie. default copy does not work)
    """
    STACK_BASE: Stack = Stack()
    STACKS: List[Stack] = []
    for i in range(100):
        prev_stack: Union[Stack, None] = None
        try:
            prev_stack = STACKS[i - 1]
        except IndexError:
            pass
        # clone the previous stack
        fixed_stack: Stack = (
            copy.copy(prev_stack) if prev_stack else copy.copy(STACK_BASE)
        )
        for j in range(1000):
            fixed_stack.push(j)
        STACKS.append(fixed_stack)
    return STACKS


def generate_queue() -> List[LinkedQueue]:
    """
    Because of the way the references are setup internally within queue, it'll reference the same instance
    so we have to create a new list of queues for each test (ie. default copy does not work)
    """
    QUEUE_BASE: LinkedQueue = LinkedQueue()
    QUEUES: List[LinkedQueue] = []
    for i in range(1000, 100001, 1000):
        QUEUES.append(copy.copy(QUEUE_BASE).arbitrary_fill(i))
    return QUEUES


def generate_list() -> List[LinkedList[Any]]:
    """
    Because of the way the references are setup internally within LinkedList, it'll reference the same instance
    so we have to create a new list of LinkedLists for each test (ie. default copy does not work)
    """
    LINKED_LIST_BASE: LinkedList[Any] = LinkedList()
    LINKED_LISTS: List[LinkedList[Any]] = []
    for i in range(100):
        prev_list: Union[LinkedList[Any], None] = None
        try:
            prev_list = LINKED_LISTS[i - 1]
        except IndexError:
            pass
        # clone the previous stack
        fixed_list: LinkedList[Any] = (
            copy.copy(prev_list) if prev_list else copy.copy(LINKED_LIST_BASE)
        )
        for j in range(1000):
            fixed_list.append(j)
        LINKED_LISTS.append(fixed_list)
    return LINKED_LISTS


def generate_optimized_list() -> List[LinkedListOptimized[Any]]:
    LINKED_LIST_BASE: LinkedListOptimized[Any] = LinkedListOptimized()
    LINKED_LISTS: List[LinkedListOptimized[Any]] = []
    for i in range(100):
        prev_list: Union[LinkedListOptimized[Any], None] = None
        try:
            prev_list = LINKED_LISTS[i - 1]
        except IndexError:
            pass
        # clone the previous stack
        fixed_list: LinkedListOptimized[Any] = (
            copy.copy(prev_list) if prev_list else copy.copy(LINKED_LIST_BASE)
        )
        for j in range(1000):
            fixed_list.append(j)
        LINKED_LISTS.append(fixed_list)
    return LINKED_LISTS


def measure_stack_pop() -> TIMES_TYPE:
    """Popping a single item from a stack"""
    timer: Timer = Timer()
    times: TIMES_TYPE = []
    for stack in generate_stack():
        stack_len: int = len(stack)
        timer.reset().start()
        stack.pop()
        timer.end()
        times.append((stack_len, timer.get_time()))
    return times


def measure_all_pop() -> TIMES_TYPE:
    """Popping all items from a stack"""
    timer: Timer = Timer()
    times: TIMES_TYPE = []
    for stack in generate_stack():
        stack_len: int = len(stack)
        timer.reset().start()
        for _ in range(stack_len):
            stack.pop()
        timer.end()
        times.append((stack_len, timer.get_time()))
    return times


def measure_all_enqueue() -> TIMES_TYPE:
    """Queue's enqueue"""
    timer: Timer = Timer()
    times: TIMES_TYPE = []
    for queue in generate_queue():
        queue_len: int = len(queue)
        timer.reset().start()
        queue.enqueue("foo")
        timer.end()
        times.append((queue_len, timer.get_time()))
    return times


def measure_linked_list_get_entry_at_0() -> TIMES_TYPE:
    """Linked List get_entry at specifically index 0"""
    timer: Timer = Timer()
    times: TIMES_TYPE = []
    for list in generate_list():
        list_len: int = len(list)
        timer.reset().start()
        list.get_entry(0)
        timer.end()
        times.append((list_len, timer.get_time()))
    return times


def measure_linked_list_get_entry_at_last() -> TIMES_TYPE:
    """Linked List get_entry at specifically the last index

    I imagine there's some optimization that could be done on the implementation side,
    IE. iterate from the end closer to the index, so head/tail accessing should be O(1),
    instead of O(1) and O(n) respectively...
    """
    timer: Timer = Timer()
    times: TIMES_TYPE = []
    for list in generate_list():
        list_len: int = len(list)
        timer.reset().start()
        list.get_entry(list_len - 1)
        timer.end()
        times.append((list_len, timer.get_time()))
    return times


def measure_linked_list_get_entry_at_last_optimized() -> TIMES_TYPE:
    timer: Timer = Timer()
    times: TIMES_TYPE = []
    for list in generate_optimized_list():
        list_len: int = len(list)
        timer.reset().start()
        list.get_entry(list_len - 1)
        timer.end()
        times.append((list_len, timer.get_time()))
    return times


def measure_linked_list_print_all() -> TIMES_TYPE:
    """Printing all elements in a LinkedList using get_entry"""
    timer: Timer = Timer()
    times: TIMES_TYPE = []
    for list in generate_optimized_list():
        list_len: int = len(list)
        timer.reset().start()
        for i in range(list_len):
            """
            The print statement would actually generate significant overhead
            And I'm much too impatient, just time accessing all the values
            """
            list.get_entry(i)
        timer.end()
        print(list_len, timer.get_time())
        times.append((list_len, timer.get_time()))
    return times


def measure_linked_list_optimized_print_all() -> TIMES_TYPE:
    """Printing all elements in a LinkedList using get_entry"""
    timer: Timer = Timer()
    times: TIMES_TYPE = []
    for list in generate_optimized_list():
        list_len: int = len(list)
        timer.reset().start()
        for i in range(list_len):
            """
            The print statement would actually generate significant overhead
            And I'm much too impatient, just time accessing all the values
            """
            list.get_entry(i)
        timer.end()
        print(list_len, timer.get_time())
        times.append((list_len, timer.get_time()))
    return times


def print_for_terminal(title: str, l: List[Tuple[int, int]]) -> None:
    print("\n" + title)
    for n, time in l:
        print(f"{time}")
