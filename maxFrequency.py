class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        res = 1
        l = 0
        r = 0
        cnt = 0
        while r < len(nums) - 1:
            cnt += (nums[r + 1] - nums[r]) * (r - l + 1)
            if cnt > k:
                while cnt > k:
                    cnt -= nums[r + 1] - nums[l]
                    l += 1
            res = max(res, r - l + 2)
            r += 1
        return res

test = Solution()
print test.maxFrequency([1,2,4], 5)
print test.maxFrequency([1,4,8,13], 5)
print test.maxFrequency([3,9,6], 2)
print test.maxFrequency([100000], 100000)