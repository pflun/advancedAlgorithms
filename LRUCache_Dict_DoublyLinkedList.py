# -*- coding: utf-8 -*-
# self.data: key => LinkedNode
class LinkedNode(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

class LRUCache2(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = {}
        self.head = LinkedNode(None, 'head')
        self.tail = LinkedNode(None, 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    # ==========================================
    # 以下两个函数【绝对不碰字典】，只管纯粹的指针断连
    # ==========================================
    def remove(self, node):
        """把一个节点从当前位置摘除"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        """把节点挂到 tail 的前面（代表最近使用）"""
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    # ==========================================
    # 核心业务逻辑：就像调 API 一样无脑拼装
    # ==========================================
    def get(self, key):
        if key not in self.data:
            return -1

        node = self.data[key]
        # 刷新活跃度：先摘下来，再挂到最新
        self.remove(node)
        self.add(node)

        return node.value

    def put(self, key, value):
        # 1. 如果已经存在，先把旧的从链表里摘除
        if key in self.data:
            self.remove(self.data[key])

        # 2. 创建新节点，挂到最新，并记录在字典里
        newNode = LinkedNode(key, value)
        self.add(newNode)
        self.data[key] = newNode

        # 3. 检查超载：淘汰最老的（head.next）
        if len(self.data) > self.capacity:
            oldest = self.head.next
            self.remove(oldest)           # 链表里摘除
            del self.data[oldest.key]     # 字典里删除

# Outdated
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = LinkedNode(None, 'head')
        self.tail = LinkedNode(None, 'tail')
        self.head.next = self.tail  # head.next being oldest
        self.tail.prev = self.head  # tail.prev being most recent
        self.data = {}

    def deleteNode(self, node):
        if node.value == 'head' or node.value == 'tail':
            return
        else:
            del self.data[node.key]
            node.prev.next = node.next
            node.next.prev = node.prev
            del node

    def get(self, key):
        if key not in self.data:
            return -1
        node = self.data[key]
        # take the node out
        node.prev.next = node.next
        node.next.prev = node.prev
        # insert into most recent position
        self.insertNew(node)
        return node.value

    def put(self, key, value):
        # remove old value if present
        if key in self.data:
            self.deleteNode(self.data[key])

        # create new node
        newNode = LinkedNode(key, value)
        self.data[key] = newNode

        # if over limit, delete oldest node
        if len(self.data) > self.capacity:
            self.deleteNode(self.head.next)

        self.insertNew(newNode)

    def insertNew(self, newNode):
        # insert new node into last position
        last = self.tail.prev
        last.next = newNode
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = last

obj = LRUCache(3)
obj.put(1, 1)
obj.put(2, 2)
obj.put(3, 3)
print obj.get(1)
obj.put(4, 4)
print obj.get(2)