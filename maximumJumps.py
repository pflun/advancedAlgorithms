class Solution(object):
    def maximumJumps(self, nums, target):
        # maximum jump steps at dp[i]
        dp = [0] * len(nums)
        for j in range(1, len(nums)):
            tmp = 0
            for i in range(j):
                # -1 means cannot jump from this index, never reachable
                if dp[i] != -1 and -target <= nums[j] - nums[i] <= target:
                    tmp = max(tmp, dp[i] + 1)
            # set j to not reachable
            if tmp == 0:
                dp[j] = -1
            else:
                dp[j] = tmp
        return dp[-1]

test = Solution()
print test.maximumJumps([1,3,6,4,1,2], 2)
print test.maximumJumps([1,3,6,4,1,2], 3)
print test.maximumJumps([1,3,6,4,1,2], 0)
print test.maximumJumps([0,2,1,3], 1)