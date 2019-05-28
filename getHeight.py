# -*- coding: utf-8 -*-
# 想找 "从当前元素向某一方向的第一个 (大于 / 小于) 自己的元素"，就要靠单调栈来维护单调性，对应的是 (递减 / 递增)。
# 有N个人，顺次排列，他们的身高分别为H[i]，每个人向自己后方看，他能看到的人是在他后面离他最近的且比他高的人。
# 请依次输出每个人能看到的人的编号Next[i]，如果他后面不存在比他高的人，则输出-1

class Solution(object):
    def getHeight(self, heights):
        n = len(heights)
        res = [0] * n

        # Stack stores index of people
        stack = []
        for i in range(n):
            # 若i更高，所有之前小于heights[i]看到的都是i
            while stack and heights[stack[-1]] <= heights[i]:
                res[stack.pop()] = i
            # 新的i压入stack
            stack.append(i)

        while stack:
            res[stack.pop()] = -1

        return res

test = Solution()
print test.getHeight([3,2,5,6,1,2])