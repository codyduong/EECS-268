"""
Author: Cody Duong
KUID: 3050266
Date: 2022-10-23
Lab: lab06
Last modified: 2022-10-23
Purpose: Entry file, runs lab6

Disable/Enable lines as needed
"""

from exercise1.src.Generate import *

print_for_terminal("Stack - Pop", measure_stack_pop())
print_for_terminal("Stack - All Pop", measure_all_pop())
print_for_terminal("Queue - Enqueue", measure_all_enqueue())

print_for_terminal("LinkedList - @ 0", measure_linked_list_get_entry_at_0())
print_for_terminal("LinkedList - @ End", measure_linked_list_get_entry_at_last())
print_for_terminal("LinkedList - all", measure_linked_list_print_all())

print_for_terminal("MaxHeap", measure_heap_add())