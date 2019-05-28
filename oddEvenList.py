# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if head == None:
            return None

        dummyOdd = odd = head
        dummyEven = even = head.next

        while odd.next and even.next:
            odd.next = even.next
            even.next = odd.next.next
            odd = odd.next
            even = even.next

        odd.next = dummyEven

        return dummyOdd

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

test = Solution()
print test.oddEvenList(head).next.next.next.val