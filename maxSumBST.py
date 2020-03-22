# -*- coding: utf-8 -*-
from treeDesirializer import deserialize

# https://www.youtube.com/watch?v=wrsdqcG7lTE
# 我下面写的解法有个bug，没有判断左右子树是否为BST，所以return应该加上bool 子树是否BST
class Solution(object):
    def maxSumBST(self, root):
        self.res = 0
        def dfs(node):
            # exit
            if not node.left and not node.right:
                return node.val, node.val

            lv = False
            rv = False
            ls = 0
            rs = 0
            if node.left:
                lv, ls = dfs(node.left)
            if node.right:
                rv, rs = dfs(node.right)

            if not lv and rv > node.val:
                self.res = max(self.res, node.val + rs)
                return node.val, node.val + rs
            elif not rv and lv < node.val:
                self.res = max(self.res, ls + node.val)
                return node.val, ls + node.val
            elif lv < node.val and rv > node.val:
                self.res = max(self.res, ls + node.val + rs)
                return node.val, ls + node.val + rs
            return node.val, node.val

        dfs(root)
        return self.res

head = deserialize('[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]')
test = Solution()
print test.maxSumBST(head)