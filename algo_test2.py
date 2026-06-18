# -*- coding: utf-8 -*-
#         _______1______
#       /              \
#     ___2__          ___5__
#   /      \        /      \
#   3       4       6       7

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorder(root):
    global res
    res = ''
    def helper(node):
        global res
        res += str(node.val)
        if node.left:
            helper(node.left)
        if node.right:
            helper(node.right)
    helper(root)
    return res

from sortedArrayToBST import Solution
test = Solution()
head_node = test.sortedArrayToBST([3, 2, 4, 1, 6, 5, 7])
print preorder(head_node)

#    1
#  2   5
# 3 4 6 7