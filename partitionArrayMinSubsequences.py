class Solution(object):
    def partitionArray(self, nums, k):
        res = 1
        nums.sort()
        minVal = nums[0]
        for n in nums[1:]:
            if n - minVal > k:
                res += 1
                minVal = n
        return res

test = Solution()
print test.partitionArray([3,6,1,2,5], 2)
print test.partitionArray([1,2,3], 1)
print test.partitionArray([2,2,4,5], 0)