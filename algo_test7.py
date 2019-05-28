# -*- coding: utf-8 -*-
# 先用end找包含短串的最右端，start再走找最左端, sum == 0 代表是否子串完全包含短串
import hashlib

a = "http://site.douban.com/chuan"
# 16 byte
print hashlib.md5(a).digest()
# 32 byte
print hashlib.md5(a).hexdigest()

# print '*'.isdigit()
# s1 = set([1, 2, 3])
# print s1.pop()
# s1.add(4)
# print s1.pop()
# print s1.pop()
# print s1.pop()
#
# def test(nums):
#     for i in xrange(len(nums) - 1, -1, -1):
#         print nums[i]
#     print nums[0:3]
#
# print test([5, 4, 3, 2, 1])


class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


# key => ListNode
class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.data = {}
        self.head = ListNode(None, 'head')
        self.tail = ListNode(None, 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key in self.data:
            node = self.data[key]
            self.delete(self.data[key])
            self.insert(node)
        else:
            return -1

        return node.val

    def insert(self, newNode):
        self.tail.prev.next = newNode
        newNode.prev = self.tail.prev
        self.tail.prev = newNode
        newNode.next = self.tail

    def delete(self, node):
        if node.val == 'head' or node.val == 'tail':
            return
        else:
            del self.data[node.key]
            node.prev.next = node.next
            node.next.prev = node.prev
            del node

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        if key in self.data:
            node = self.data[key]
            node.val = value
            self.delete(self.data[key])
            self.data[key] = node
            self.insert(node)
        else:
            if self.capacity > 0:
                self.capacity -= 1
                newNode = ListNode(key, value)
                self.data[key] = newNode
                self.insert(newNode)
            else:
                self.delete(self.head.next)
                newNode = ListNode(key, value)
                self.data[key] = newNode
                self.insert(newNode)


obj = LRUCache(3)
obj.set(1, 1)
obj.set(2, 2)
obj.set(3, 3)
print obj.get(1)
obj.set(4, 4)
print obj.get(2)
