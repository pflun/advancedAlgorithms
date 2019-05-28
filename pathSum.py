# Definition for a binary tree node.
from sortedArrayToBST import Solution

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def __init__(self):
        # Tip: instance variable unique to each instance (not really related to this problem)
        self.store = []

    def pathSum(self, root, sum):
        ls = []
        self.dfs(root, sum, ls)
        return self.store

    def dfs(self, root, target, ls):
        if root:

            if not root.left and not root.right:
                if root.val == target:
                    ls.append(root.val)
                    self.store.append(ls)

            # Tip: ls + [root.val] to pass tmp path
            if root.left:
                self.dfs(root.left, target - root.val, ls + [root.val])
            if root.right:
                self.dfs(root.right, target - root.val, ls + [root.val])

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.pathSum(head_node, 7)

#    4
#  2   6
# 1 3 5 7