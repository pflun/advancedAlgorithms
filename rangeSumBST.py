# -*- coding: utf-8 -*-
# BFS相对好写，DFS就是比如curr < L，就dfs(curr.right)因为curr.right could be possible
from sortedArrayToBST import Solution
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    # BFS
    def rangeSumBST(self, root, L, R):
        queue = [root]
        res = 0
        while queue:
            curr = queue.pop(0)
            if not curr:
                continue
            # left child could be possible
            if curr.val > L:
                queue.append(curr.left)
            # right child could be possible
            if curr.val < R:
                queue.append(curr.right)
            if curr.val >= L and curr.val <= R:
                res += curr.val
        return res

    def rangeSumBSTBrutalForce(self, root, L, R):
        self.res = 0

        def dfs(node, L, R):
            if not node:
                return
            if node.val >= L and node.val <= R:
                self.res += node.val
            dfs(node.left, L, R)
            dfs(node.right, L, R)

        dfs(root, L, R)
        return self.res

test = Solution()
head_node = test.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7])
test = Solution1()
print test.rangeSumBST(head_node, 3, 5)
#     4
#   2   6
#  1 3 5 7
# 0
