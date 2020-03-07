# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=gxYV8eZY0eQ
# 有个小bug，base case不应该看input长度为1，比如两位数就不成立。应该检查len(ans)是否为0空
class Solution(object):
    def diffWaysToCompute(self, input):
        if len(input) == 1:
            return input
        ans = []
        for i in range(len(input)):
            op = input[i]
            if op == '+' or op == '-' or op == '*':
                left = input[:i]
                right = input[i + 1:]
                l = self.diffWaysToCompute(left)
                r = self.diffWaysToCompute(right)

                for a in l:
                    for b in r:
                        ans.append(self.operation(a, b, op))

        return ans


    def operation(self, a, b, op):
        a = int(a)
        b = int(b)
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b


test = Solution()
print test.diffWaysToCompute("2*3-4*5")
print test.diffWaysToCompute("2*3")