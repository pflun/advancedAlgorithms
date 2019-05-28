# Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):
        # 2 linked lists, below x goes to l1, above x goes to l2, finally link l1 and l2
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head != None:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next

head = ListNode(1)
p1 = ListNode(4)
p2 = ListNode(3)
p3 = ListNode(2)
p4 = ListNode(5)
p5 = ListNode(2)
p6 = ListNode(7)
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6

test = Solution()
print test.partition(head, 3).next.next.next.next.next.val

