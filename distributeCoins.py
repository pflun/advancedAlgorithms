# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=zQqku1AXVF8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distributeCoins(self, root):
        self.res = 0
        self.balance(root)
        return self.res

    # @return 金币数量与节点数量的差值diff
    def balance(self, root):
        if not root:
            return 0
        l = self.balance(root.left)
        r = self.balance(root.right)
        # flow = 左边缺的或多出来的 + 右边缺的或多出来的
        self.res += abs(l) + abs(r)
        # 返回左右flow抵消的 + 根节点剩余的（根节点自己用掉一个）
        return l + r + root.val - 1

# [1,0,2] => 2
h1 = TreeNode(1)
h2 = TreeNode(0)
h3 = TreeNode(2)
h1.left = h2
h1.right = h3
test = Solution()
print test.distributeCoins(h1)