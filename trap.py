# -*- coding: utf-8 -*-
# 对任意位置上的积水，不包括i本身, 由左右两边最高的bar决定
class Solution(object):
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
print test.trap([0,1,0,2,1,0,1,3,2,1,2,1])