# -*- coding: utf-8 -*-
# 给一个二叉树，找maximum size of level which has the largest number of siblings。
# 这里sibling的定义就是从这一层的左端点到右端点的所有存在或者不存在的node，也就是假设这中间的Parent都有左右孩子的情况下，从左端点到右端点总共有多少个。
from sortedArrayToBST import Solution
class Solution1(object):
    def maxSiblings(self, root):
        res = 0
        dic = {}

        def dfs(root, depth, offset):
            if not root:
                return
            dfs(root.left, depth + 1, offset - 1)
            if depth == 0:
                dic[depth] = [0, 0]
            else:
                curr = dic.get(depth, [0, 0])
                if offset > 0:
                    curr[1] = max(curr[1], offset)
                elif offset < 0:
                    curr[0] = min(curr[0], offset)
                dic[depth] = curr
            dfs(root.right, depth + 1, offset + 1)
        dfs(root, 0, 0)

        for v in dic.values():
            res = max(res, v[1] - v[0])

        return res


test = Solution()
head_node = test.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.maxSiblings(head_node)

#     4
#   2   6
#  1 3 5 7
# 0