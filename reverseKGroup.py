# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=pLx1VP-FnuY
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        if not head:
            return None

        stack = []
        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        rest = dummy.next

        while rest:
            # 每次扔k个进stack
            for _ in range(k):
                # 避免出现不能被k除尽的情况，最后剩余几个
                if rest:
                    stack.append(rest)
                    rest = rest.next
            # 最后剩余几个不用反转，直接返回dummy.next
            if len(stack) != k:
                return dummy.next
            # stack pop出来的顺序反转，用tail串起来
            while stack:
                tail.next = stack.pop()
                tail = tail.next

            # 把这一回合反转的最后一个node指向下一回合第一个node，就是rest
            tail.next = rest

        traverse = dummy.next
        while traverse:
            print traverse.val
            traverse = traverse.next

        return dummy.next


head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(4)
p4 = ListNode(5)
p5 = ListNode(6)
p6 = ListNode(7)
p7 = ListNode(8)
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7

test = Solution()
print test.reverseKGroup(head, 2).val
