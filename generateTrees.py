# https://www.youtube.com/watch?v=GZ0qvkTAjmw
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# solution different than youtube above
class Solution(object):
    def generateTrees(self, n):
        # corner case
        if n == 0:
            return []
        return self.cal([i for i in xrange(1, n + 1)])

    def cal(self, lst):
        if not lst: return [None]
        res = []
        for i in xrange(len(lst)):
            for left in self.cal(lst[:i]):
                for right in self.cal(lst[i + 1:]):
                    node, node.left, node.right = TreeNode(lst[i]), left, right
                    res += [node]
        return res