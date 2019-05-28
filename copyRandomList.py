# -*- coding: utf-8 -*-
# dict key：原node， val：新node
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        dic = {}
        # 最后缺个None，这里补上
        dic[None] = None
        curr = head
        # copy node
        while curr:
            dic[curr] = RandomListNode(curr.label)
            curr = curr.next

        curr = head
        # copy pointers
        while curr:
            dic[curr].next = dic[curr.next]
            dic[curr].random = dic[curr.random]
            curr = curr.next

        return dic[head]