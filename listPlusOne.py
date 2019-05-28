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

    def listPlusOne(self, head):
        if not head:
            return None

        # Reverse to 3 2 1
        dummy = ListNode(0)
        while head:
            tmp = head.next  # store tmp, for step 4 to move forward
            head.next = dummy.next  # reverse: 1.next -> null, 2nd while 2.next -> 1
            dummy.next = head  # dummy.next -> 1, 2nd while dummy.next -> 2
            head = tmp  # head forward

        head = dummy.next
        carry = 0
        dummy = tail = ListNode(0)
        one = 1
        while head or carry:
            # if 999 + 1 = 1000, deal with additional node
            if carry and head == None:
                tail.next = ListNode(carry)
                break

            v1 = head.val
            head = head.next
            # a除以b，然后返回商与余数的元组
            carry, val = divmod(v1 + one + carry, 10)
            tail.next = ListNode(val)
            tail = tail.next
            one = 0

        # Reverse to 1 2 4
        head = dummy.next
        dummy.next = None
        while head:
            tmp = head.next
            head.next = dummy.next
            dummy.next = head
            head = tmp

        # Print result
        # traverse = dummy.next
        # while traverse:
        #     print traverse.val
        #     traverse = traverse.next
        return dummy.next

head = ListNode(9)
p1 = ListNode(9)
p2 = ListNode(9)
p3 = ListNode(9)
head.next = p1
p1.next = p2
p2.next = p3

test = Solution()
print test.listPlusOne(head)