class Solution(object):
    def subarraySum(self, nums, k):
        if len(nums) == 0 or not k:
            return 0

        res = 0
        tmp = 0
        left = 0
        right = 0

        while right < len(nums):
            if tmp == k:
                res += 1
                tmp -= nums[left]
                left += 1
            elif tmp < k:
                tmp += nums[right]
                right += 1
            else:
                tmp -= nums[left]
                left += 1

        if tmp == k:
            res += 1

        return res