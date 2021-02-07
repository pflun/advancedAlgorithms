# -*- coding: utf-8 -*-
# 单调栈
# 维持站内高度单调递增，遇到下降高度（下一位比栈顶高）时，pop栈顶进行计算，以栈顶为height栈顶前一位为起始width
# 当遇到下降高度（比height[i]更低的高度）时，之前以那些height[i]为高度向右扩散出的矩形面积就确定了
# PS：暴力解法是，对于每一个固定高度，尝试向左右两边扩散
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