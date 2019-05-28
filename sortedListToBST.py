# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None
        pre_mid, mid = self.sortedListToBSTHelper(head)

        root = TreeNode(mid.val)
        if pre_mid != None:
            pre_mid.next = None
        else:
            head = None

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root


    def sortedListToBSTHelper(self, head):
        prev = None
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev, slow


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
print test.sortedListToBST(head).val
