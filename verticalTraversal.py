# -*- coding: utf-8 -*-
from sortedArrayToBST import Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def verticalTraversal(self, root):
        res = []
        dic = {}
        offset = 0

        def preorder(root, offset, dic):
            if not root:
                return
            preorder(root.left, offset - 1, dic)
            if offset in dic:
                dic[offset].append(root.val)
            else:
                dic[offset] = [root.val]
            preorder(root.right, offset + 1, dic)

        preorder(root, offset, dic)

        for i in sorted(dic.keys()):
            res.append(dic[i])

        return res

test = Solution()
head_node = test.sortedArrayToBST([0, 1, 2, 4, 5, 3, 6, 7])
test1 = Solution1()
print test1.verticalTraversal(head_node)

#     5
#   2   6
#  1 4 3 7
# 0