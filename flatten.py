from sortedArrayToBST import Solution

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

class Solution1(object):
    def flatten(self, root):
        if root is None:
            return []
        stack = [root]
        head = ListNode(root.val)
        dummy = ListNode(0)
        dummy.next = head

        # Preorder traversal, keep moving head to next
        while stack:
            node = stack.pop()
            tmp = ListNode(node.val)
            head.next = tmp
            head = head.next

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return dummy.next.next

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.flatten(head_node).next.next.next.val