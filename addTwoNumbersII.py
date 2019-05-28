# Solution 1: Reverse l1, l2, implement add-two-list-numbers.py, reverse result linked list
# Solution 2: Not in-place, convert into integer then add them

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        c1, c2 = '', ''
        while l1:
            c1 += str(l1.val)
            l1 = l1.next
        while l2:
            c2 += str(l2.val)
            l2 = l2.next
        num = str(int(c1) + int(c2))
        dummy = ListNode(0)
        c = dummy
        for i in range(len(num)):
            c.next = ListNode(num[i])
            c = c.next

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
print test.addTwoNumbers(head, head).next.val