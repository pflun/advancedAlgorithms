# -*- coding: utf-8 -*-
# http://www.cnblogs.com/grandyang/p/6793904.html
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Need debug
class Solution:
    def str2tree(self, s):
        if len(s) == 0:
            return None

        start = s.find('(')
        if start == -1:
            return TreeNode(int(s))

        root = TreeNode(int(s[:start]))
        #
        count = 0
        for i in range(start, len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
            # print count, s[i]
            if count == 0:
                print i, s
                root.left = self.str2tree(s[start + 1:i])
                if i + 1 < len(s):
                    root.right = self.str2tree(s[i + 2:-1])

        return root

test = Solution()
print test.str2tree('4(2(3)(1))(6(5))').right.val
