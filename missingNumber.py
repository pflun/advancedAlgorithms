class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total_n = (n + 1) * n /2
        total_nums = sum(nums)
        return total_n - total_nums

test = Solution()
print test.missingNumber([0, 1, 3])