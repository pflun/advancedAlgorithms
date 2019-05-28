# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        if head is None:
            return head
        # Fast slow pointer find middle
        dummy1 = ListNode(0)
        dummy1.next = head
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None

        # Reverse second half
        dummy2 = ListNode(0)
        while fast:
            tmp = fast.next  # store tmp, for step 4 to move forward
            fast.next = dummy2.next  # reverse: 1.next -> null, 2nd while 2.next -> 1
            dummy2.next = fast  # dummy.next -> 1, 2nd while dummy.next -> 2
            fast = tmp  # head forward

        tail = dummy1
        head1 = dummy1.next
        head2 = dummy2.next

        # Merge two linked list
        while head2 != None:
            tail.next = head1
            head1 = head1.next
            tail = tail.next
            tail.next = head2
            head2 = head2.next
            tail = tail.next

        # any leftover from first half
        if head1 != None:
            tail.next = head1

        # traverse = dummy1.next
        # while traverse:
        #     print traverse.val
        #     traverse = traverse.next

        return dummy1.next

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
# p5.next = p6

test = Solution()
test.reorderList(head)