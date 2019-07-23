
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

# Did we have to use a Node class for this?


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        # should add an item to the back of the queue.
        self.size += 1
        self.storage.append(item)

    def dequeue(self):
        # should remove and return an item from the front of the queue.
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop(0)
        pass

    def len(self):
        # len returns the number of items in the queue.
        return self.size
