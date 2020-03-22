class Solution(object):
    def createTargetArray(self, nums, index):
        res = [nums[0]]
        for i in range(1, len(nums)):
            val = nums[i]
            idx = index[i]
            res = res[:idx] + [val] + res[idx:]
        return res

test = Solution()
print test.createTargetArray([0,1,2,3,4], [0,1,2,2,1])
print test.createTargetArray([1,2,3,4,0], [0,1,2,3,0])
print test.createTargetArray([1], [0])