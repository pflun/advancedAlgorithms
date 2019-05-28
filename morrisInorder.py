# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=wGXB9OWhPTg
from sortedArrayToBST import Solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def morrisInorder(self, root):
        res = []
        current = root
        while current:
            if not current.left:
                res.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                # 找到左子树中最大的那个
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                # 指回current
                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                # already visited, 删掉辅助指针
                else:
                    predecessor.right = None
                    res.append(current.val)
                    current = current.right
        return res

test = Solution()
head_node = test.sortedArrayToBST([0, 1, 2, 4, 5, 3, 6, 7])
test1 = Solution1()
print test1.morrisInorder(head_node)

#     5
#   2   6
#  1 4 3 7
# 0