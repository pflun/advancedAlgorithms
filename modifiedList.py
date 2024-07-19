# -*- coding: utf-8 -*-
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        deletes = set(nums)
        # 若要删第一个node，就得dummy.next = head然后走dummy
        # 走dummy就还需要res = dummy
        dummy = ListNode('inf')
        dummy.next = head
        res = dummy
        while dummy and dummy.next:
            if dummy.next.val in deletes:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return res.next

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(4)
p4 = ListNode(5)
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4

test = Solution()
print test.modifiedList([1,2,3], head).val
print test.modifiedList([6], head).val