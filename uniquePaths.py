class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """
    def uniquePaths(self, m, n):
        # Exit
        if m == 1:
            return 1
        elif n == 1:
            return 1
        else:
            return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    def uniquePaths2(self, m, n):
        dp = [[1 for _ in range(m)] for _ in range(n)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]

test = Solution()
print test.uniquePaths2(3, 3)

# [[1,1,1],
#  [1,2,3],
#  [1,3,6]]

