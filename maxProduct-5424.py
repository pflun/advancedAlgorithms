class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)

test = Solution()
print test.maxProduct([3,4,5,2])
print test.maxProduct([1,5,4,5])
print test.maxProduct([3,7])