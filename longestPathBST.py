# -*- coding: utf-8 -*-
# 路径可以拐弯
from sortedArrayToBST import Solution
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def longestPathBST(self, root):
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, left + right + 1)
            return max(left, right) + 1

        dfs(root)
        return self.res

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8])
test1 = Solution1()
print test1.longestPathBST(head_node)

#     5
#   3   7
#  2 4 6 8
# 1