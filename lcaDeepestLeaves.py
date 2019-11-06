# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lcaDeepestLeaves2(self, root):
        def helper(node, depth):
            if not node:
                return depth, node
            left = helper(node.left, depth + 1)
            right = helper(node.right, depth + 1)
            if left[0] == right[0]:
                return left[0], node
            elif left[0] > right[0]:
                return left[0], left[1]
            else:
                return right[0], right[1]

        return helper(root, 0)[1]

    def lcaDeepestLeaves(self, root):
        self.deepest = 0
        self.res = None
        self.helper(root, 0)
        return self.res

    def helper(self, node, depth):
        self.deepest = max(self.deepest, depth)
        if not node:
            return depth
        left = self.helper(node.left, depth + 1)
        right = self.helper(node.right, depth + 1)
        # 左右子树深度相等，当前node就是LCA，否则LCA在更深的那个子树里
        if left == self.deepest and right == self.deepest:
            self.res = node
        return max(left, right)

head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(5)
n3 = TreeNode(2)
n4 = TreeNode(4)
# n5 = TreeNode(3)
# n6 = TreeNode(6)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
# n3.left = n5
# n5.right = n6

test = Solution()
print test.lcaDeepestLeaves(head_node).val

#     0
#   1   5
#  2 4
# 3
#  6