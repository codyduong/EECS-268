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
"""Use a better implementation for O(n) accessing"""
print_for_terminal("LinkedList (optimized) - @ End", measure_linked_list_get_entry_at_last_optimized())

# This prints as it goes since it so slow
# measure_linked_list_print_all()

# Use the optimized list data structure whose implementation should change from O(n^2) to O(n)
measure_linked_list_optimized_print_all()
