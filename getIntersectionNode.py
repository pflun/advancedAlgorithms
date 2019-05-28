# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA == None or headA.next == None or headB.next == None or headB.next == None:
            return None

        dummyA = ListNode(float("-inf"))
        dummyA.next = headA
        dummyB = ListNode(float("inf"))
        dummyB.next = headB

        while headA.next != None and headB.next != None:
            headA = headA.next
            headB = headB.next
        if headA.next == None and headB.next == None:
            headA = dummyA.next
            headB = dummyB.next
            while headA.next != None and headB.next != None:
                if headA == headB:
                    return headA.val
                headA = headA.next
                headB = headB.next
        elif headA.next == None:
            headA = dummyB.next
            headB = headB.next
        else:
            headB = dummyA.next
            headA = headA.next

        while headA.next != None and headB.next != None:
            headA = headA.next
            headB = headB.next
        if headA.next == None:
            headA = dummyB.next
            headB = headB.next
        else:
            headB = dummyA.next
            headA = headA.next

        while headA.next != None and headB.next != None:
            if headA == headB:
                return headA.val
            headA = headA.next
            headB = headB.next

        return None

    # better solution
    def getIntersectionNode2(self, headA, headB):
        lenA = 0
        lenB = 0
        ptrA = headA
        ptrB = headB

        # get both length
        while ptrA != None:
            ptrA = ptrA.next
            lenA += 1

        while ptrB != None:
            ptrB = ptrB.next
            lenB += 1

        ptrA = headA
        ptrB = headB

        # move A or B to same position of their length
        if lenA > lenB:
            for _ in range(lenA - lenB):
                ptrA = ptrA.next
        else:
            for _ in range(lenB - lenA):
                ptrB = ptrB.next

        # find intersection
        while ptrA != ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next

        return ptrA

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(4)
p4 = ListNode(5)
p5 = ListNode(6)
p6 = ListNode(7)
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6

head2 = ListNode(10)
h1 = ListNode(11)
head2.next = h1
h1.next = p3

test = Solution()
print test.getIntersectionNode(head, head2)

# A:       1 → 2 → 3
#                    ↘
#                      4 → 5 → 6 → 7
#                    ↗
# B:          10 → 11