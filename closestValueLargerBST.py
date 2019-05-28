# -*- coding: utf-8 -*-
# 在BST中找下一个比给定target大的数。corner case: 比BST最大值还大？那res就等于root，额外处理下
from sortedArrayToBST import Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def closetValue(self, root, target):
        if not root:
            return None

        # global variable, will become more and more close to target
        self.res = root.val

        def dfs(root, target):
            if not root:
                return
            if root.val > target:
                self.res = root.val
            if target < root.val:
                dfs(root.left, target)
            else:
                dfs(root.right, target)

        dfs(root, target)
        return self.res

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 5, 6, 9, 20])
test1 = Solution1()
print test1.closetValue(head_node, 0)

#    5
#  2   9
# 1 3 6 20