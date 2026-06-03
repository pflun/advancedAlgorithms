# -*- coding: utf-8 -*-
# 对任意位置上的积水，不包括i本身, 由左右两边最高的bar决定
class Solution(object):
    # 单调栈：维护递减栈的index
    # 比较tricky：每次算一个矩形，而不是倒凸型。洼地是倒凸型的话，就会先出栈计算突出的尖部，然后再算剩下的矩形（所以逐次算两个矩形）
    def trap3(self, height):
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                # 1. 弹出洼地（底面）
                bottom_idx = stack.pop()
                if stack:
                    # 2. 获取新的栈顶作为左墙
                    left_idx = stack[-1]
                    # 3. 计算宽度
                    width = i - left_idx - 1
                    # 4. 计算被左右两堵墙夹住的水的高度
                    bounded_height = min(height[left_idx], height[i]) - height[bottom_idx]
                    # 5. 累加面积 (宽 * 高)
                    res += width * bounded_height

            stack.append(i)
        return res

    def trap2(self, height):
        if len(height) < 2:
            return 0
        res = 0
        l = 0
        r = len(height) - 1
        leftMax = height[0]
        rightMax = height[-1]
        while l < r:
            if leftMax <= rightMax:
                if l < len(height) and height[l] < leftMax:
                    res += leftMax - height[l]
                l += 1
                leftMax = max(leftMax, height[l])
            else:
                if r > 0 and height[r] < rightMax:
                    res += rightMax - height[r]
                r -= 1
                rightMax = max(rightMax, height[r])
        return res

    def trap(self, height):
        if len(height) < 2:
            return 0
        res = 0
        i = 0
        j = len(height) - 1
        leftMax = height[i]
        rightMax = height[j]

        while i < j:
            # 想象极端情况只有两边有柱中间全是水，矮的往高的方向移动
            if leftMax < rightMax:
                # 把以 leftMax 为高的当前缺口加进res
                if i + 1 < len(height) and height[i + 1] < leftMax:
                    res += leftMax - height[i + 1]
                i += 1
                # 更新leftMax，可能下一格盛更多水
                leftMax = max(leftMax, height[i])
            else:
                if j - 1 > 0 and height[j - 1] < rightMax:
                    res += rightMax - height[j - 1]
                j -= 1
                rightMax = max(rightMax, height[j])

        return res

test = Solution()
print test.trap3([0,1,0,2,1,0,1,3,2,1,2,1])