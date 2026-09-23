# -*- coding: utf-8 -*-
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        curr = head
        while curr:
            if curr.child:
                child = curr.child
                next_node = curr.next      # 1. 保存原来的 next

                curr.next = child          # 2. 把 child 接到 curr.next
                child.prev = curr
                curr.child = None

                tail = child               # 3. 找子链表的尾部
                while tail.next:
                    tail = tail.next

                tail.next = next_node      # 4. 尾部接回原来的 next
                if next_node:
                    next_node.prev = tail

            curr = curr.next
        return head