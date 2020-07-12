class Solution(object):
    def numIdenticalPairs(self, nums):
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    res += 1
        return res


test = Solution()
print test.numIdenticalPairs([1,2,3,1,1,3])
print test.numIdenticalPairs([1,1,1,1])
print test.numIdenticalPairs([1,2,3])
print test.numIdenticalPairs([1])