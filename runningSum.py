class Solution(object):
    def runningSum(self, nums):
        if len(nums) == 1:
            return nums
        res = [nums[0]]
        for i in range(1, len(nums)):
            res.append(res[-1] + nums[i])
        return res

test = Solution()
print test.runningSum([1,2,3,4])
print test.runningSum([1,1,1,1,1])
print test.runningSum([3,1,2,10,1])