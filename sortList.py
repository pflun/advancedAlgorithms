# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        if head == None or head.next == None:
            return head

        mid = self.findMiddle(head)

        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)

        return self.merge(left, right)

    def findMiddle(self, head):
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy

        # Tip to merge two linked list
        while head1 != None and head2 != None:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        # If any leftover
        if head1 != None:
            tail.next = head1
        else:
            tail.next = head2

        return dummy.next


head = ListNode(2)
p1 = ListNode(6)
p2 = ListNode(4)
p3 = ListNode(8)
head.next = p1
p1.next = p2
p2.next = p3

test = Solution()
print test.sortList(head).next.next.next.val
