# -*- coding: utf-8 -*-
# list1 = input('input1: ')
# list2 = input('input2: ')
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    # def __init__(self, y):
    #     self.val = y

    def addLists(self, l1, l2):
        carry = 0
        dummy = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            # a除以b，然后返回商与余数的元组
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next

        # Print result
        # traverse = dummy.next
        # while traverse:
        #     print traverse.val
        #     traverse = traverse.next
        return dummy.next

head = ListNode(2)
p1 = ListNode(4)
p2 = ListNode(6)
p3 = ListNode(8)
head.next = p1
p1.next = p2
p2.next = p3

test = Solution()
print test.addLists(head, head)