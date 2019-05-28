# -*- coding: utf-8 -*-
from sortedArrayToBST import Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def findBottomLeftValue(self, root):
        if root is None:
            return []
        stack = [(root, 0)]
        dic = {}
        res = []

        while stack:
            node, level = stack.pop()
            if level not in dic:
                dic[level] = node.val

            if node.right:
                stack.append((node.right, level + 1))

            if node.left:
                stack.append((node.left, level + 1))

        for key, value in dic.items():
            res.append(value)

        return res[-1]

    # Accepted, 从右到左覆盖，如果当前level比maxlevel深或相等就更新res
    def findBottomLeftValue2(self, root):
        if root is None:
            return None

        self.res = 0
        self.maxlevel = 0

        def dfs(root, currlevel):
            if not root:
                return None
            if not root.left and not root.right:
                if currlevel >= self.maxlevel:
                    self.maxlevel = currlevel
                    self.res = root.val

            # 右子会被左子覆盖掉
            dfs(root.right, currlevel + 1)
            dfs(root.left, currlevel + 1)

        dfs(root, 0)
        return self.res

test = Solution()
head_node = test.sortedArrayToBST([None, 2, None, 4, 5, 6, 7])
test1 = Solution1()
print test1.findBottomLeftValue2(head_node)

#    4
#  2   6
# 1 N 5 7