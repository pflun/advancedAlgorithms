# -*- coding: utf-8 -*-
# 单调栈
# 维持站内高度单调递增，遇到下降高度（下一位比栈顶高）时，pop栈顶进行计算，以栈顶为height栈顶前一位为起始width
# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
# https://www.youtube.com/watch?v=XwUb7x6YDeA&ab_channel=LeetCode%E5%8A%9B%E6%89%A3
class Solution(object):
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in xrange(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans