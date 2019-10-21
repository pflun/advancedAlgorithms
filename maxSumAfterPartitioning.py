# https://www.youtube.com/watch?v=3M8q-wB2tmw&t=829s
class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        dp = [0 for _ in range(len(A) + 1)]
        for i in range(len(A) + 1):
            tmp = float('-inf')
            for k in range(1, min(i + 1, K + 1)):
                tmp = max(tmp, A[i - k])
                dp[i] = max(dp[i], dp[i - k] + tmp * k)
        return dp[len(A)]

test = Solution()
print test.maxSumAfterPartitioning([1,15,7,9,2,5,10], 3)