# -*- coding: utf-8 -*-
class Solution(object):
    def maxArea(self, height):
        if len(height) < 2:
            return 0
        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            curArea = min(height[left], height[right]) * width
            res = max(res, curArea)

            # 高位木板向里移动的所有位置，形成的 container 水量都小于原来位置。画图就看明白了。
            # 所以移低位木板水量才有可能变大
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res

test = Solution()
print test.maxArea([2,3,5,3,6,4])