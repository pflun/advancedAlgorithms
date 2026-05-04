# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # inorder traversal iteration
    def kthSmallest(self, root, k):
        if not root:
            return []
        stack = [root]
        while root.left:
            stack.append(root.left)
            root = root.left
        while stack:
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            if curr.right:
                stack.append(curr.right)
                curr = curr.right
                while curr.left:
                    stack.append(curr.left)
                    curr = curr.left
        return -1