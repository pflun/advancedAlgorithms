# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=ABMLLVzf4ZQ
# 思路就是把 2 * 3 + 4 * 5 变成 6 ＋ 20
class Solution(object):
    def calculate(self, s):
        if not s or len(s) == 0:
            return 0

        stack = []
        res = 0
        sign = '+'
        num = 0

        for i in range(len(s)):
            if s[i].isdigit():
                num = int(s[i])
                # 识别比如123
                while i + 1 < len(s) and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1

            # if operator OR at last position (so you need to calculate whatsoever)
            if not s[i].isdigit() and not s[i] == ' ' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                # pop prev element and multiply curr num
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(stack.pop() / num)
                # 更新 sign，sign永远是滞后的，因为 3 ＊ 4 － 2 你遇到 '－' 才去计算 3 ＊ 4，3在stack最顶 4就是num
                sign = s[i]
                num = 0

        for x in stack:
            res += x

        return res

    def calculate2(self, s):
        res = 0
        stack = []
        currNum = 0
        sign = '+'
        i = 0
        while i < len(s):
            if s[i].isdigit():
                currNum = int(s[i])
                while i + 1 < len(s) and s[i + 1].isdigit():
                    currNum = currNum * 10 + int(s[i + 1])
                    i += 1
            if not s[i].isdigit() and not s[i] == ' ' or i == len(s) - 1:
                if sign == '+':
                    stack.append(int(currNum))
                elif sign == '-':
                    stack.append(-int(currNum))
                elif sign == '*':
                    stack[-1] *= int(currNum)
                elif sign == '/':
                    stack[-1] /= int(currNum)
                sign = s[i]
                currNum = 0
            i += 1

        for n in stack:
            res += n
        return res

test = Solution()
print test.calculate(' 3+5 * 2')
# expect: 13, python 2 bug, -3/2 = -2 but 3/2 = 1
print test.calculate2("14-3/2")
print test.calculate2("3+2*2")
