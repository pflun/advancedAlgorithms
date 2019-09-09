# -*- coding: utf-8 -*-
# Sn = a1(1 - q ** n) / (1 - q)
from sortedArrayToBST import Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def countNodes(self, root):
        if not root:
            return 0

        dic = {}
        level = 0
        self.inorder(root, dic, level)

        # tip: last key -- dic.keys()[-1], last value -- dic.values()[-1]
        # perfect tree
        if len(dic.values()[-1]) == 2 ** dic.keys()[-1]:
            # 等比通项公式，比如3层 1 + 2 + 4
            return (1 - 2 ** dic.keys()[-1]) / (1 - 2)
        # not perfect tree
        else:
            # 求最后一行余出来几个node，加上除最后一行以外的perfect tree nodes, (1 + 2 + 4) + 1
            counter = 0
            for i in dic.values()[-2]:
                if i != '#':
                    counter += 1
            return ((1 - 2 ** dic.keys()[-2]) / (1 - 2)) + counter

    def inorder(self, root, dic, level):
        if root == None:
            if level in dic:
                dic[level].append('#')
            else:
                dic[level] = ['#']
            return None

        self.inorder(root.left, dic, level + 1)
        if level in dic:
            dic[level].append(root.val)
        else:
            dic[level] = [root.val]
        self.inorder(root.right, dic, level + 1)

    def countNodes2(self, root):
        def getRightDepth(node, depth):
            if not node.left and not node.right:
                return depth
            getRightDepth(node.right, depth + 1)

        def getLeftDepth(node, depth):
            if not node.left and not node.right:
                return depth
            getLeftDepth(node.left, depth + 1)

        right = getRightDepth(root, 1)
        left = getLeftDepth(root, 1)

        res = 0
        curr = 1
        if left == right:
            for _ in range(left):
                res += curr
                curr *= 2
            return res
        else:
            return 1 + self.countNodes2(root) + self.countNodes2(root)


test = Solution()
head_node = test.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.countNodes(head_node)

#     4
#   2   6
#  1 3 5 7
# 0