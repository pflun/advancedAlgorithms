# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def segregateEvenOddLinkedList(self, head):

        odd = ListNode(0)
        even = ListNode(0)

        dummy1 = ListNode(0)
        dummy2 = ListNode(0)

        dummy1.next = odd
        dummy2.next = even

        traverse = head
        while traverse:
            if traverse.val % 2 != 0:
                odd.next = traverse
                odd = odd.next
            else:
                even.next = traverse
                even = even.next
            traverse = traverse.next

        # while dummy1:
        #     print dummy1.val
        #     dummy1 = dummy1.next
        return dummy1.next.next, dummy2.next.next

head = ListNode(1)
p1 = ListNode(6)
p2 = ListNode(3)
p3 = ListNode(5)
p4 = ListNode(4)
p5 = ListNode(6)
p6 = ListNode(7)
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6

test = Solution()
print test.segregateEvenOddLinkedList(head)