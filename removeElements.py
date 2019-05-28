# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        # if first node need to delete
        if head.val == val:
            tmp = head.next
            head.next = None
            head = tmp
        dummy = ListNode(0)
        dummy.next = head
        prev = None
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next
            if slow.val == val:
                prev.next = fast
                slow = fast
                fast = fast.next
        # if last node need to delete
        last = dummy.next
        while last.next.next != None:
            last = last.next
        if last.next.val == val:
            last.next = None

        return dummy.next

    def removeElements2(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        next = dummy

        while next != None and next.next != None:
            if next.next.val == val:
                next.next = next.next.next
            else:
                next = next.next

        traverse = dummy.next
        while traverse != None:
            print traverse.val
            traverse = traverse.next

        return dummy.next


head = ListNode(1)
p1 = ListNode(6)
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
print test.removeElements(head, 1).val