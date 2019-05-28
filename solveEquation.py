# -*- coding: utf-8 -*-
# 参考下面这个答案
# https://leetcode.com/problems/solve-the-equation/discuss/105310/Python-via-helper-function
class Solution(object):
    def solveEquation(self, equation):
        def helper(s):
            sign, n = 1, len(s)
            # i, coef, const stand for current index, and accumulative 'x' coefficient and constant
            i = coef = const = 0
            while i < n:
                if s[i] == '+':
                    sign = 1
                elif s[i] == '-':
                    sign = -1
                elif s[i].isdigit():
                    j = i
                    while j < n and s[j].isdigit():
                        j += 1
                    tmp = int(s[i:j])
                    if j < n and s[j] == 'x':
                        coef += tmp * sign
                        j += 1
                    else:
                        const += tmp * sign
                    i = j - 1
                else:
                    coef += 1 * sign
                i += 1
            return coef, const

        left, right = equation.split('=')
        k1, b1 = helper(left)
        k2, b2 = helper(right)
        # k1x + b1 = k2x + b2
        ans = 'x=' + str((b2 - b1) / (k1 - k2)) if k1 != k2 and b1 != b2 \
            else "Infinite solutions" if k1 == k2 and b1 == b2 \
            else "No solution" if b2 != b1 else 'x=0'
        return ans

test = Solution()
print test.solveEquation("x+5-3+x=6+x-2")