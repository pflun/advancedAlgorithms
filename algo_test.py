# -*- coding: utf-8 -*-
# 450. Delete Node in a BST
# deleteBST.py
# 我这个没置换，只是把值改了
from sortedArrayToBST import Solution
class Solution1(object):
    def deleteNode(self, root, key):
        while root:
            if root.val == key:
                if root.right:
                    tmp = self.findMin(root.right)
                    root.val = tmp.val
                    return root
                if root.left:
                    tmp = self.findMax(root.left)
                    root.val = tmp.val
                    return root
                root.val = None
            if key < root.val:
                root = root.left
            elif key > root.val:
                root = root.right

        return root

    def findMin(self, root):
        while root.left:
            root = root.left
        return root

    def findMax(self, root):
        while root.right:
            root = root.right
        return root

test = Solution()
head_node = test.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.deleteNode(head_node, 4).right.right.val

#     4
#   2   6
#  1 3 5 7
# 0