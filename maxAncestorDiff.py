# Optimization: top-down only pass max and min would work
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        self.res = 0
        def helper(node, prev):
            if not node:
                return
            if len(prev) != 0:
                for p in prev:
                    tmp = abs(p - node.val)
                    self.res = max(self.res, tmp)
            helper(node.left, prev + [node.val])
            helper(node.right, prev + [node.val])
        helper(root, [])
        return self.res