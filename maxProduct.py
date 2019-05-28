# -*- coding: utf-8 -*-
# 这道题是maximum subarray sum 的变体
# 已然用动归 DP来解决 每个dp数组保存的都是以当前元素结尾的乘积最大值
# 但是要注意因为是相乘 负负得正 所以还要保存最小值 因为最小值碰到个负数很可能就会变成最大值

class Solution(object):
    def maxProduct(self, nums):
        if len(nums) == 0:
            return None
        # init: tmp_max[curr][0] is curr max, tmp_max[curr][1] is curr min
        tmp_max = [[0 for x in range(2)] for y in range(len(nums))]
        tmp_max[0][0] = tmp_max[0][1] = nums[0]
        final_max = nums[0]

        # DP: curr_max is max among prev_max * curr, prev_min * curr, curr
        #     curr_min is min among prev_max * curr, prev_min * curr, curr
        for i in range(1, len(nums)):
            tmp_max[i][0] = max(max(tmp_max[i - 1][0] * nums[i], tmp_max[i - 1][1] * nums[i]), nums[i])
            tmp_max[i][1] = min(min(tmp_max[i - 1][0] * nums[i], tmp_max[i - 1][1] * nums[i]), nums[i])

        for j in tmp_max:
            final_max = max(final_max, j[0])

        return final_max

test = Solution()
print test.maxProduct([2])