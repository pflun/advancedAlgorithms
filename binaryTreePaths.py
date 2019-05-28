# Definition for a binary tree node.
from sortedArrayToBST import Solution

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        if not root:
            return None
        ls += str(root.val)
        if not root.left and not root.right:
            res.append(ls)
        if root.left:
            self.dfs(root.left, ls + "->", res)
        if root.right:
            self.dfs(root.right, ls + "->", res)

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.binaryTreePaths(head_node)

#    4
#  2   6
# 1 3 5 7

# in-place
# still preorder
#
#         left = root.left;
#         right = root.right;
#
#         root.left = None;
#         root.right = left;
#         whileroot.right != None:
#             root = root.right;