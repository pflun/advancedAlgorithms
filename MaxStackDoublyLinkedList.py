from sortedcontainers import SortedList
class LinkedNode(object):
    def __init__(self, v):
        self.val = v
        self.prev = None
        self.next = None

class MaxStack(object):
    def __init__(self):
        self.data = SortedList(key=lambda x: x.val)
        self.head = LinkedNode('head')
        self.tail = LinkedNode('tail')
        self.head.next = self.tail  # head.next being oldest
        self.tail.prev = self.head  # tail.prev being most recent

    def push(self, x):
        newNode = LinkedNode(x)
        # insert new node into last position
        last = self.tail.prev
        last.next = newNode
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = last
        self.data.add(newNode)

    def pop(self):
        last = self.tail.prev
        last.prev.next = last.next
        last.next.prev = last.prev
        self.data.remove(last)
        return last.val

    def top(self):
        last = self.tail.prev
        return last.val

    def peekMax(self):
        return self.data[-1].val

    def popMax(self):
        node = self.data.pop()
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.val

stack = MaxStack()
print stack.push(5)
print stack.push(1)
print stack.push(5)
print stack.top() # -> 5
print stack.popMax() # -> 5
print stack.top() # -> 1
print stack.peekMax() # -> 5
print stack.pop() # -> 1
print stack.top() # -> 5

print stack.push(2)
print stack.push(3)
print stack.push(4)
print stack.peekMax()
print stack.popMax()
print stack.peekMax()
print stack.pop()
print stack.top()