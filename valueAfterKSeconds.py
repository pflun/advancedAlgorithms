class Solution(object):
    def valueAfterKSeconds(self, n, k):
        dp = [[1 for _ in range(n)]]
        for i in range(1, k + 1):
            dp.append([1])
            for j in range(1, n):
                dp[i].append(dp[i][-1] + dp[i - 1][j])
        return dp[-1][-1] % (10 ** 9 + 7)

test = Solution()
print test.valueAfterKSeconds(4, 5)
print test.valueAfterKSeconds(5, 3)