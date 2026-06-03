# -*- coding: utf-8 -*-
class Solution(object):
    # [73, 74, 75, 71, 69, 72, 76, 73], 比如当前T[i]=71，stack里pop 69，因为71以前的数跟69无关，71已经比69大了
    # stack里存index其实就行了，栈顶既然比T[i]大，那天数就用栈顶减去i
    # decreasing stack, idx右 -> idx左，每次把更靠stack右的替换掉，这样最右边留下的就是当前最近的warmer temp
    # 先while pop，再res，最后append当前value
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

    # 单调栈：维护递减栈的index
    def dailyTemperatures2(self, temperatures):
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            # 当前数字大于栈顶index对应的数字时
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped_idx = stack.pop()
                res[popped_idx] = i - popped_idx # 和warmer day相差的天数

            stack.append(i) # 当前的index进栈，等待它自己的“下一个更大值”

        return res

test = Solution()
print test.dailyTemperatures2([73, 74, 75, 71, 69, 72, 76, 73])