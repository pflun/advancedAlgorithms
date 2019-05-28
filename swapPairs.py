# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        if not head:
            return None
        elif head.next == None:
            return head

        dummy = ListNode(0)
        dummy.next = head.next
        slow = dummy
        fast = head
        # init Position (not val): (0, 1), (2, 3)...
        while fast and fast.next:
            # store 3
            tmp = fast.next.next
            # dummy -> 2
            slow.next = fast.next
            # 2 -> 1, fast still 1 after this operation
            fast.next.next = fast
            # 1 -> 3
            fast.next = tmp
            # s = f = 1
            slow = fast
            # f = 3
            fast = fast.next

        return dummy.next