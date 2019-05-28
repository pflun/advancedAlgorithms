# -*- coding: utf-8 -*-
# 利用 postorder，若子树不是BST，则直接返回False，不必计算parents
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        self.largest = 0

        def postorder(root):
            if root is None:
                return None
            left = postorder(root.left)
            right = postorder(root.right)

            # if this subtree is not validBST, its parents are definitely not valid
            if left is False or right is False:
                return False
            else:
                flag, size = self.isValid(root)

            if flag:
                self.largest = max(self.largest, size)
                return True
            else:
                return False

        postorder(root)

        return self.largest


    def isValid(self, root):

        def inorder(root, res):
            if not root:
                return None

            if root.left:
                inorder(root.left, res)

            res.append(root.val)

            if root.right:
                inorder(root.right, res)

            return res

        arr = inorder(root, [])

        for i in range(len(arr) - 1):
            if arr[i + 1] <= arr[i]:
                return False, len(arr)

        return True, len(arr)

head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n3.left = n6
n6.left = n5
n6.right = n7

test1 = Solution()
print test1.largestBSTSubtree(head_node)

#     0
#   1   2
#  3 4
# 6
#5 7