class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + [0] * (n - 1)
        for i in range(m):
            for j in range(n):
                # if obstacle, mark as 0 as no path
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[n - 1]

test = Solution()
print test.uniquePathsWithObstacles(
    [[0,0,0],
    [0,1,0],
    [0,0,0]])
# print test.uniquePathsWithObstacles([[0,0],[1,1],[0,0]])