# https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/
# input is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100)
class Solution(object):
    def maxSumIS(self, arr):
        dp = [0 for _ in range(len(arr))]
        dp[0] = arr[0]
        res = 0
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + arr[i])
        for v in dp:
            res = max(res, v)
        return res, dp

test = Solution()
print test.maxSumIS([1, 101, 2, 3, 100, 4, 5])