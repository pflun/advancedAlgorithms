# Similar: https://codeforces.com/blog/entry/59579
class Solution(object):
    # TLE
    def countPairs(self, nums, low, high):
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if low <= nums[i] ^ nums[j] <= high:
                    res += 1
        return res

test = Solution()
print test.countPairs([1,4,2,7], 2, 6)
print test.countPairs([9,8,4,2,1], 5, 14)