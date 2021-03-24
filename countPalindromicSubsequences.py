class Solution:
    def countPalindromicSubsequences(self, S):
        m = len(S)
        dp = [[1 if j == i else 0 for i in range(m)] for j in range(m)]

        for k in range(1, m):
            for i in range(m - k):
                j = i + k
                if S[i] != S[j]:
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]
                else:
                    l, r = i + 1, j - 1
                    while l <= r and S[l] != S[i]: l += 1
                    while l <= r and S[r] != S[j]: r -= 1
                    dp[i][j] = 2 * dp[i + 1][j - 1]
                    if l == r:
                        dp[i][j] += 1
                    elif l > r:
                        dp[i][j] += 2
                    else:
                        dp[i][j] -= dp[l + 1][r - 1]

        return dp[0][m - 1] % (10 ** 9 + 7)