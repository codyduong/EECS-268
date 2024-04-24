import copy
from .LinkedList import LinkedList
from .LinkedQueue import LinkedQueue
from .Stack import Stack
from .Timer import Timer
from .Heap import MaxHeap

def generate_stack():
    """
    Because of the way the references are setup internally within stack, it'll reference the same instance
    so we have to create a new list of stacks for each test (ie. default copy does not work)
    """
    STACK_BASE = Stack()
    STACKS = []
    for i in range(100):
        prev_stack = None
        try:
            prev_stack = STACKS[i - 1]
        except IndexError:
            pass
        # clone the previous stack
        fixed_stack = copy.copy(prev_stack) if prev_stack else copy.copy(STACK_BASE)
        for j in range(1000):
            fixed_stack.push(j)
        STACKS.append(fixed_stack)
    return STACKS

def generate_queue():
    QUEUE_BASE = LinkedQueue()
    QUEUES = []
    for i in range(1000, 100001, 1000):
        QUEUES.append(copy.copy(QUEUE_BASE).arbitrary_fill(i))
    return QUEUES

def generate_list():
    LINKED_LIST_BASE = LinkedList()
    LINKED_LISTS = []
    for i in range(100):
        prev_list = None
        try:
            prev_list = LINKED_LISTS[i - 1]
        except IndexError:
            pass
        # clone the previous stack
        fixed_list = copy.copy(prev_list) if prev_list else copy.copy(LINKED_LIST_BASE)
        for j in range(1000):
            fixed_list.append(j)
        LINKED_LISTS.append(fixed_list)
    return LINKED_LISTS

def generate_heap():
    HEAP_BASE = MaxHeap()
    HEAPS = []
    for i in range(1000, 100001, 1000):
        prev_heap = None
        try:
            prev_heap = HEAPS[i - 1]
        except IndexError:
            pass
        # clone the previous stack
        fixed_heap = copy.copy(prev_heap) if prev_heap else copy.copy(HEAP_BASE)
        for j in range(1000):
            fixed_heap.insert(j)
        HEAPS.append(fixed_heap)
    return HEAPS

def measure_stack_pop():
    """Popping a single item from a stack"""
    timer = Timer()
    times = []
    for stack in generate_stack():
        stack_len = len(stack)
        timer.reset().start()
        stack.pop()
        timer.end()
        # print(f"{stack_len} {timer.get_time()}")
        times.append((stack_len, timer.get_time()))
    return times

def measure_all_pop():
    """Popping all items from a stack"""
    timer = Timer()
    times = []
    for stack in generate_stack():
        stack_len = len(stack)
        timer.reset().start()
        for _ in range(stack_len):
            stack.pop()
        timer.end()
        # print(f"{stack_len} {timer.get_time()}")
        times.append((stack_len, timer.get_time()))
    return times

def measure_all_enqueue():
    """Queue's enqueue"""
    timer = Timer()
    times = []
    for queue in generate_queue():
        queue_len = len(queue)
        timer.reset().start()
        queue.enqueue("foo")
        timer.end()
        times.append((queue_len, timer.get_time()))
    return times

def measure_linked_list_get_entry_at_0():
    """Linked List get_entry at specifically index 0"""
    timer = Timer()
    times = []
    for list in generate_list():
        list_len = len(list)
        timer.reset().start()
        list.get_entry(0)
        timer.end()
        times.append((list_len, timer.get_time()))
    return times

def measure_linked_list_get_entry_at_last():
    """Linked List get_entry at specifically the last index"""
    timer = Timer()
    times = []
    for list in generate_list():
        list_len = len(list)
        timer.reset().start()
        list.get_entry(list_len - 1)
        timer.end()
        times.append((list_len, timer.get_time()))
    return times

def measure_linked_list_print_all():
    """Printing all elements in a LinkedList using get_entry"""
    timer = Timer()
    times = []
    for list in generate_list():
        list_len = len(list)
        timer.reset().start()
        for i in range(list_len):
            list.get_entry(i)
        timer.end()
        print(list_len, timer.get_time())
        times.append((list_len, timer.get_time()))
    return times

def measure_heap_add():
    """Measure adding to heap"""
    timer = Timer()
    times = []
    for heap in generate_heap():
        heap_len = len(heap)
        timer.reset().start()
        heap.insert(0)
        timer.end()
        times.append((heap_len, timer.get_time()))
    return times

def print_for_terminal(title, l):
    print("\n" + title)
    for n, time in l:
        # print(f"{n} {time}")
        print(f"{time}")
