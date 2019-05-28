class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return None
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                res += nums[i]
        return res

test = Solution()
print test.arrayPairSum([1,4,3,2,5,6])