# -*- coding: utf-8 -*-
# [73, 74, 75, 71, 69, 72, 76, 73], 比如当前T[i]=71，stack里pop 69，因为71以前的数跟69无关，71已经比69大了
# stack里存index其实就行了，栈顶既然比T[i]大，那天数就用栈顶减去i
class Solution(object):
    def dailyTemperatures(self, T):
        res = [0] * len(T)
        stack = []
        for i in range(len(T) - 1, -1 , -1):
            while stack and stack[-1][0] < T[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1][1] - i
            stack.append([T[i], i])

        return res

test = Solution()
print test.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])