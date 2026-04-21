# Java LinkedHashSet also work
from collections import OrderedDict

class FirstUnique:
    def __init__(self, nums):
        self.unique = OrderedDict()
        self.freq = {}
        for n in nums:
            self.freq[n] = self.freq.get(n, 0) + 1
        for k, v in self.freq.items():
            if v == 1:
                self.unique[k] = 1

    def showFirstUnique(self):
        if not self.unique:
            return -1
        return next(iter(self.unique.keys()))

    def add(self, value):
        self.freq[value] = self.freq.get(value, 0) + 1
        if self.freq[value] == 1:
            self.unique[value] = 1
        else:
            self.unique.pop(value)

test = FirstUnique([2,3,5])
print test.showFirstUnique()
print test.add(5)
print test.showFirstUnique()
print test.add(2)
print test.showFirstUnique()
print test.add(3)
print test.showFirstUnique()

# Doubly linked list
class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class FirstUniqueDoublyLinkedList:
    def __init__(self, nums):
        # 1. Initialize Doubly Linked List with Dummy Head and Tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        # 2. Hash Map: val -> Node (if unique) OR False (if duplicate)
        self.dic = {}

        # 3. Process initial numbers
        for num in nums:
            self.add(num)

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append_node(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def showFirstUnique(self):
        # If the list is empty, head.next points to tail
        if self.head.next == self.tail:
            return -1
        # The first unique number is always right after the dummy head
        return self.head.next.val

    def add(self, value):
        if value not in self.dic:
            # State 1: Brand new number. It is unique.
            new_node = Node(value)
            self._append_node(new_node)
            self.dic[value] = new_node

        elif self.dic[value] is not False:
            # State 2: Seen exactly once before. It is now a duplicate.
            # Remove it from the DLL and mark it dead in the dictionary.
            node_to_remove = self.dic[value]
            self._remove_node(node_to_remove)
            self.dic[value] = False

        # State 3: self.dic[value] is False.
        # It's already a known duplicate, do absolutely nothing.
