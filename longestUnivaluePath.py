# https://www.youtube.com/watch?v=yX1hVhcHcH8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0

        def helper(root, ans):
            if not root:
                return 0
            left = helper(root.left, ans)
            right = helper(root.right, ans)
            pathL = 0
            pathR = 0
            if root.left and root.val == root.left.val:
                pathL = left + 1
            if root.right and root.val == root.right.val:
                pathR = right + 1
            self.ans = max(ans, pathL + pathR)
            return max(pathL, pathR)

        helper(root, 0)
        return self.ans