# -*- coding: utf-8 -*-
class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0], nums[1], nums[2])

        resNotFirst = [0] * (len(nums) - 1)
        resNotLast = [0] * (len(nums) - 1)
        resNotBoth = [0] * (len(nums) - 2)

        # 不抢第一个
        resNotFirst[0] = nums[1]
        resNotFirst[1] = max(nums[1], nums[2])
        for i in range(2, len(nums) - 1):
            resNotFirst[i] = max(nums[i + 1] + resNotFirst[i - 2], resNotFirst[i - 1])

        # 不抢最后一个
        resNotLast[0] = nums[0]
        resNotLast[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            resNotLast[i] = max(nums[i] + resNotLast[i - 2], resNotLast[i - 1])

        # 不抢第一个和最后一个
        resNotBoth[0] = nums[1]
        resNotBoth[1] = max(nums[1], nums[2])
        for i in range(2, len(nums) - 2):
            resNotBoth[i] = max(nums[i + 1] + resNotBoth[i - 2], resNotBoth[i - 1])

        # print resNotFirst, resNotLast, resNotBoth
        return max(resNotFirst[-1], resNotLast[-1], resNotBoth[-1])

test = Solution()
print test.rob([2, 1, 1, 3])