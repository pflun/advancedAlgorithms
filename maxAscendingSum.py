class Solution(object):
    def maxAscendingSum(self, nums):
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp.append(dp[-1] + nums[i])
            else:
                dp.append(nums[i])
        return max(dp)

test = Solution()
print test.maxAscendingSum([10,20,30,5,10,50])
print test.maxAscendingSum([10,20,30,40,50])
print test.maxAscendingSum([12,17,15,13,10,11,12])
print test.maxAscendingSum([100,10,1])