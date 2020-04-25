class Solution(object):
    def minSubsequence(self, nums):
        sumVal = sum(nums)
        nums.sort()
        i = len(nums) - 1
        tmp = 0
        res = []
        while i >= 0:
            tmp += nums[i]
            res.append(nums[i])
            if tmp > sumVal - tmp:
                return res
            i -= 1

test = Solution()
print test.minSubsequence([4,3,10,9,8])
print test.minSubsequence([4,4,7,6,7])
print test.minSubsequence([6])