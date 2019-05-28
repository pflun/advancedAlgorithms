# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow = head
        pre = slow

        size = 0
        traverse = head
        while traverse:
            size += 1
            traverse = traverse.next

        if size < n:
            return head
        elif size == 1 and n == 1:
            return []

        for _ in range(size - n):
            pre = slow
            slow = slow.next

        tmp = slow.next
        slow.next = None
        pre.next = tmp

        # traverse = head
        # while traverse:
        #     print traverse.val
        #     traverse = traverse.next

        return head

    def removeNthFromEnd2(self, head, n):
        # i.e. 1~5 n=2, fast goto 3, then slow goto 3 and fast goto 5, slow.next skip 4 point to 5
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        # traverse = dummy.next
        # while traverse:
        #     print traverse.val
        #     traverse = traverse.next

        return dummy.next

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
print test.removeNthFromEnd2(head, 2).val