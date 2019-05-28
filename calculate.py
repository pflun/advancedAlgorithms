# -*- coding: utf-8 -*-
# 比如：
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
# https://www.youtube.com/watch?v=ijyUwyt5vkU
# 用stack存之前若干层没计算完的结果，也就是没遇到')'
class Solution(object):
    def calculate(self, s):
        stack = []
        res = 0
        sign = 1
        for i in range(len(s)):
            if s[i].isdigit():
                num = int(s[i])
                # 识别比如123
                while i + 1 < len(s) and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
                # 1 - 2 = 1 + (-2)
                res += num * sign
            elif s[i] == '+':
                sign = 1
            # 1 - 2 = 1 + (-2)
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                # 用stack存之前若干层没计算完的结果，也就是没遇到')'
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif s[i] == ')':
                # 当前res乘以最近pop出来的（也就是sign），再加上第二次pop出来的（也就是上一层的value）
                res = res * stack.pop() + stack.pop()

        return res

test = Solution()
print test.calculate('(1+(4+5+2 + (1 + 1))-3)+(6+8 + 1)')