# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0 or len(preorder) != len(inorder):
            return []
        res = self.buildTreeHelper(preorder, inorder, 0, 0, len(preorder) - 1)
        return res

    def buildTreeHelper(self, preorder, inorder, pre_st, in_st, in_end):
        if pre_st > len(preorder) or in_st > in_end:
            return None

        # first node in preorder is root
        root = TreeNode(preorder[pre_st])
        i = in_st

        # find root in inorder, root is the first element in preorder
        while(i <= in_end):
            if inorder[i] == preorder[pre_st]:
                break
            i += 1

        # left: pre start is the next element in preorder, i is curr root in inorder so in_end is at the left position of i
        root.left = self.buildTreeHelper(preorder, inorder, pre_st + 1, in_st, i - 1)
        # right: pre start is curr root (pre_st) + len(left child in inorder) + 1 (画图可见)
        root.right = self.buildTreeHelper(preorder, inorder, pre_st + (i - in_st + 1), i + 1, in_end)

        return root