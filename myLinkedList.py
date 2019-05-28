class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.size or index < 0 or self.head is None:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        curr = Node(val)
        curr.next = self.head
        self.head = curr
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        tmp = Node(val)
        if self.head is None:
            self.head = tmp
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = tmp
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index > self.size:
            return
        tmp = Node(val)
        curr = self.head
        for _ in range(index):
            curr = curr.next
        after = curr.next
        curr.next = tmp
        tmp.next = after
        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index > self.size:
            return
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1

obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(2)
obj.addAtIndex(1, 2)
print obj.get(1)
obj.deleteAtIndex(1)
print obj.get(1)