# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        slow = head
        fast = head
        post = head
        for _ in range(m - 1):
            pre = slow
            slow = slow.next
        for _ in range(n - 1):
            fast = fast.next

        rest = fast.next
        fast.next = None

        dummy = ListNode(0)
        # Use 2 or more nodes as example
        # Test case: 1, 2 then return 2 (meanwhile if print (p.next).val you will get 1)
        while slow:
            tmp = slow.next  # store tmp, for step 4 to move forward
            slow.next = dummy.next  # reverse: 1.next -> null, 2nd while 2.next -> 1
            dummy.next = slow  # dummy.next -> 1, 2nd while dummy.next -> 2
            slow = tmp  # head forward

        # 1 -> 4
        pre.next = dummy.next

        # 2 -> 5
        for _ in range(n - 1):
            post = post.next
        post.next = rest

        # traverse = head
        # while traverse:
        #     print traverse.val
        #     traverse = traverse.next

        return head

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
print test.reverseBetween(head, 2, 4)