# Definition for a binary tree node.
from sortedArrayToBST import Solution

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def hasPathSum(self, root, sum):
        res = []
        self.dfs(root, sum, res)
        return any(res)

    def dfs(self, root, target, res):
        if root:
            if not root.left and not root.right:
                if root.val == target:
                    res.append(True)
            if root.left:
                self.dfs(root.left, target - root.val, res)
            if root.right:
                self.dfs(root.right, target - root.val, res)

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.hasPathSum(head_node, 7)

#    4
#  2   6
# 1 3 5 7