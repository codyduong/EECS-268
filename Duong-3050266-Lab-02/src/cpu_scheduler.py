from .process import Process
from .linkedqueue import LinkedQueue

class CPUScheduler:
    _linkedqueue = None

    def __init__(self):
        self._linkedqueue = LinkedQueue()

    def run(self, s):
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

        print('')