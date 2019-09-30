# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        self.res = 0
        self.helper(root, root)
        return self.res

    def helper(self, node, parent):
        if not node:
            return [0, 0]
        left = self.helper(node.left, node)
        right = self.helper(node.right, node)
        # 左increase + 右decrease + 当前，左边递增右边递减才形成任意的拐弯
        self.res = max(self.res, left[0] + right[1] + 1)
        self.res = max(self.res, left[1] + right[0] + 1)
        increase, decrease = 0, 0
        if node.val == parent.val + 1:
            # 左和右increase的最大值返回
            increase = max(left[0], right[0]) + 1
        elif node.val == parent.val - 1:
            decrease = max(left[1], right[1]) + 1
        return [increase, decrease]

head_node = TreeNode(2)
n1 = TreeNode(3)
n2 = TreeNode(1)
n3 = TreeNode(4)
n4 = TreeNode(0)
n5 = TreeNode(5)
n6 = TreeNode(6)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n3.left = n5
n5.right = n6

test = Solution()
print test.longestConsecutive(head_node)

#     2
#   3   1
#  4 0
# 5
#  6