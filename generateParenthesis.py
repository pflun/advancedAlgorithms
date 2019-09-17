# -*- coding: utf-8 -*-
# 回溯法 backtracking, helper param: curr_str, res, 正括号已经用的数量, 反括号已经用的数量
# 想想tree
class Solution(object):
    def generateParenthesis(self, n):
        res = []
        self.helper('', res, n, 0, 0)
        return res

    def helper(self, curr, res, n, left, right):
        # 反括号已用完
        if right == n:
            res.append(curr)

        if left < n:
            self.helper(curr + "(", res, n, left + 1, right)

        if right < left:
            self.helper(curr + ")", res, n, left, right + 1)

    def generateParenthesis2(self, n):
        self.res = []

        def dfs(left, right, tmp, n):
            if len(tmp) == 2 * n:
                self.res.append(tmp[:])
            if left < right:
                if left == 0:
                    tmp += ')'
                    dfs(left, right - 1, tmp, n)
                else:
                    tmp += '('
                    dfs(left - 1, right, tmp, n)
                    tmp = tmp[:-1]
                    tmp += ')'
                    dfs(left, right - 1, tmp, n)
            elif left == right and left != 0:
                tmp += '('
                dfs(left - 1, right, tmp, n)

        dfs(n, n, '', n)
        return self.res

test = Solution()
print test.generateParenthesis(3)