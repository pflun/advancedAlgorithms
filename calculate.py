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
        i = 0
        while i < len(s):
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
            i += 1

        return res

    def calculate2(self, s):
        stack = []
        for c in s:
            if c == ")":
                curr = ""
                while stack and stack[-1] != "(":
                    curr = stack.pop() + curr
                # pop (
                stack.pop()
                value = self.getSubVal(curr)
                stack.append(value)
                continue
            if c != " ":
                stack.append(c)
        if len(stack) == 1:
            return int(stack[0])
        else:
            curr = ""
            while stack and stack[-1] != "(":
                curr = stack.pop() + curr
            return self.getSubVal(curr)

    def getSubVal(self, curr):
        res = 0
        i = 0
        currVal = ""
        currOp = 1
        while i < len(curr):
            if curr[i].isdigit():
                currVal += curr[i]
            else:
                res += int(currVal) * currOp
                currVal = ""
                if curr[i] == "-":
                    currOp = -1
                elif curr[i] == "+":
                    currOp = 1
            i += 1
        if len(currVal) != 0:
            res += int(currVal) * currOp
        return str(res)

test = Solution()
print test.calculate('(1+(4+5+2 + (1 + 1))-3)+(6+8 + 1)')
print test.calculate('(11+(4-3)+(6+8 + 11)')
print test.calculate2('(2+3) -4')