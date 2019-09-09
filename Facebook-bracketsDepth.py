# -*- coding: utf-8 -*-
# 给一个str包含左右小括号和小写字母，求括号的最大“深度”，比如“))((())())()”的最大“深度”就是3。该str的括号可能不合法。
class Solution(object):
    def bracketsDepth(self, str):
        res = 0
        depth = 0
        for c in str:
            if c == '(':
                depth += 1
                res = max(res, depth)
            elif c == ')' and depth > 0:
                depth -= 1
        return res

test = Solution()
print test.bracketsDepth("))((())())()")