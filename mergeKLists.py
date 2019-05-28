# -*- coding: utf-8 -*-
import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]

        dummy = ListNode(0)
        tail = dummy
        heap = []
        heapq.heapify(heap)
        for node in lists:
            heapq.heappush(heap, [node.val, node])

        # lists里面只有一个有效node，其他都是none
        if len(heap) == 1:
            return heapq.heappop(heap)[1]

        while heap:
            curr = heapq.heappop(heap)[1]
            tail.next = curr
            if curr.next:
                heapq.heappush(heap, [curr.next.val, curr.next])
            tail = tail.next

        # traverse = dummy.next
        # while traverse:
        #     print traverse.val
        #     traverse = traverse.next

        return dummy.next


head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(4)
p4 = ListNode(5)
p5 = ListNode(6)
p6 = ListNode(7)
head.next = p2
p2.next = p4
p1.next = p3
p5.next = p6

test = Solution()
print test.mergeKLists([head, p1, p5]).val
