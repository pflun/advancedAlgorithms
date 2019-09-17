# Brutal force, bug
# Add cache, from i to i + k => sum value of interval
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        self.res = 0
        self.starts = []

        def dfs(remain, tmp, val, idx):
            if idx + remain * k > len(nums):
                return
            if remain == 0:
                if val > self.res:
                    self.starts = tmp[:]
            for i in range(idx, len(nums) - k + 1):
                tmp.append(i)
                for j in range(i, i + k):
                    val += nums[j]
                dfs(remain - 1, tmp, val, i + k)
                tmp.pop()
                for j in range(i, i + k):
                    val += nums[j]

        dfs(3, [], 0, 0)
        return self.starts

test = Solution()
print test.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)