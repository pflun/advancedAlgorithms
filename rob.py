class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        res = [0] * len(nums)
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            res[i] = max(nums[i] + res[i - 2], res[i - 1])

        return res[-1]

test = Solution()
print test.rob([2, 1, 1, 3, 2])