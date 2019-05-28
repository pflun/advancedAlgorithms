# Reversed first half == Second half?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        dummy = ListNode(0)
        rev = None
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        while head != slow:
            rev = head
            tmp = head.next  # store tmp, for step 4 to move forward
            head.next = dummy.next  # reverse: 1.next -> null, 2nd while 2.next -> 1
            dummy.next = head  # dummy.next -> 1, 2nd while dummy.next -> 2
            head = tmp

        # slow is the mid point, 1 2 3 slow 3 2 1
        # odd/even
        if fast:
            slow = slow.next

        # traverse = rev
        # while traverse:
        #     print traverse.val
        #     traverse = traverse.next
        while rev != None and slow != None:
            if rev.val != slow.val:
                return False
            rev = rev.next
            slow = slow.next

        return True

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(3)
p4 = ListNode(2)
p5 = ListNode(1)
p6 = ListNode(1)
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
# p5.next = p6

test = Solution()
print test.isPalindrome(head)