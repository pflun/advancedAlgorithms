# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=iZVBVCpmugI
# 这题关键在于证明快慢针第一次相遇点到cycle begin和head到cycle begin的距离一样，视频有证明过程
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow
        return None