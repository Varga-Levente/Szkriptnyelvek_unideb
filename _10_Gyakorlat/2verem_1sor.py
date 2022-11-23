#!/usr/bin/env python3

# Create MyQueue class one row 2 stacks
class MyQueue(object):
    """
    MyQueue class one row 2 stacks
    Can use append, popleft, popright, is_empty methods

    append - add element to queue
    popleft - get first element from queue and remove it
    popright - get last element from queue and remove it
    is_empty - check if queue is empty
    size - return size of queue
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def popleft(self):
        return self.stack1.pop(0)

    def popright(self):
        return self.stack1.pop(-1)

    def append(self, value):
        self.stack1.append(value)

    def is_empty(self):
        return len(self.stack1) == 0

    def size(self):
        return len(self.stack1)


def main():
    # Create queue
    queue = MyQueue()

    # Add elements to queue
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)

    # Print queue size
    print("Queue size: "+str(queue.size()))

    # Print queue
    print("Queue: "+str(queue.stack1))

    # Print queue popleft
    print("Popleft: "+str(queue.popleft()))

    # Print queue popright
    print("Popright: "+str(queue.popright()))

    # Print queue
    print("Queue: "+str(queue.stack1))

    # Print queue size
    print("Queue size: " + str(queue.size()))

    # Print queue is_empty
    print("Is empty: "+str(queue.is_empty()))

    # Pop remaining elements with loop
    while not queue.is_empty():
        print("Pop: "+str(queue.popleft()))

    # Print queue
    print("Queue: "+str(queue.stack1))

    # Print queue size
    print("Is empty: "+str(queue.is_empty()))


##############################################################################

if __name__ == "__main__":
    main()