# -*- coding: utf-8 -*-
# DP: if prev is positive, add to curr; otherwise abandon prev
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    # T: O(n); S: O(1)
    def maxSubArray(self, nums):
        tmp_max = nums[0]
        final_max = nums[0]
        for num in nums[1:]:
            tmp_max = max(num, tmp_max + num)
            final_max = max(final_max, tmp_max)
            # print num, tmp_max, final_max
        return final_max

    # T: O(n); S: O(n)
    def maxSubArray2(self, nums):
        # init
        tmp_max = [0] * len(nums)
        tmp_max[0] = nums[0]
        final_max = nums[0]

        # DP: if prev is positive, add to curr; otherwise abandon prev
        for i in range(1, len(nums)):
            if tmp_max[i - 1] <= 0:
                tmp_max[i] = nums[i]
            else:
                tmp_max[i] = tmp_max[i - 1] + nums[i]

        for j in tmp_max:
            final_max = max(final_max, j)

        return final_max

    # Follow-up output subarray
    def maxSubArray3(self, nums):
        tmp_max = [0] * len(nums)
        tmp_max[0] = nums[0]

        # DP: if prev is positive, add to curr; otherwise abandon prev
        for i in range(1, len(nums)):
            if tmp_max[i - 1] <= 0:
                tmp_max[i] = nums[i]
            else:
                tmp_max[i] = tmp_max[i - 1] + nums[i]

        # 右指针是DP数组最大值位置
        right = 0
        final_max = nums[0]
        for j in range(1, len(tmp_max)):
            if tmp_max[j] > final_max:
                final_max = tmp_max[j]
                right = j

        # 左指针从最大值位置往左走直到第一个DP数组负数出现
        left = right
        for k in range(right, -1, -1):
            if tmp_max[k] > 0:
                left -= 1
            else:
                break

        return nums[left + 1:right + 1]


test = Solution()
print test.maxSubArray3([-2,1,-3,4,-1,2,1,-5,4])