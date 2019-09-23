class ListNode(object):
    def __init__(self, v):
        self.val = v
        self.prev = None
        self.next = None

class Solution(object):
    def __init__(self):
        self.dic = {}
        self.head = ListNode('head')
        self.tail = ListNode('tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, name):
        if name in self.dic and self.dic[name] is None:
            return
        elif name in self.dic:
            curr = self.dic[name]
            # delete node
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            del curr
            self.dic[name] = None
        else:
            newNode = ListNode(name)
            self.dic[name] = newNode
            self.insertNew(newNode)

    def insertNew(self, newNode):
        # insert new node into last position
        last = self.tail.prev
        last.next = newNode
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = last

    def getFirst(self):
        if self.head.next == self.tail:
            return None
        else:
            return self.head.next.val

test = Solution()
test.insert('a')
test.insert('b')
print test.getFirst()
test.insert('a')
print test.getFirst()
test.insert('c')
print test.getFirst()