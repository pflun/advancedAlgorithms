class Solution(object):
    def findLengthOfLCIS(self, nums):
        if len(nums) == 0:
            return 0
        subRes = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                subRes += 1
            else:
                res = max(res, subRes)
                subRes = 1
        res = max(res, subRes)

        return res

test = Solution()
print test.findLengthOfLCIS([1,3,5,7,2])