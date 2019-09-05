# -*- coding: utf-8 -*-
from sortedArrayToBST import Solution
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def rangeSumBST(self, root, L, R):
        self.res = 0

        def dfs(node, L, R):
            if not node:
                return
            if node.val >= L and node.val <= R:
                self.res += node.val
            dfs(node.left, L, R)
            dfs(node.right, L, R)

        dfs(root, L, R)
        return self.res

test = Solution()
head_node = test.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7])
test = Solution1()
print test.rangeSumBST(head_node, 3, 5)
#     4
#   2   6
#  1 3 5 7
# 0
