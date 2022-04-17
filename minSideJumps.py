class Solution(object):
    def minSideJumps2(self, obstacles):
        memo = [[float('inf') for _ in range(len(obstacles))] for _ in range(3)]
        memo[1][0] = 0
        for j in range(len(obstacles)):
            for i in range(3):
                if obstacles[j] == i + 1:
                    continue
                if j > 0:
                    memo[i][j] = memo[i][j - 1]
            if obstacles[j] == 0:
                memo[0][j] = min(min(memo[0][j], memo[1][j] + 1), memo[2][j] + 1)
                memo[1][j] = min(min(memo[1][j], memo[0][j] + 1), memo[2][j] + 1)
                memo[2][j] = min(min(memo[2][j], memo[1][j] + 1), memo[0][j] + 1)
            elif obstacles[j] == 1:
                memo[1][j] = min(memo[1][j], memo[2][j] + 1)
                memo[2][j] = min(memo[2][j], memo[1][j] + 1)
            elif obstacles[j] == 3:
                memo[0][j] = min(memo[0][j], memo[1][j] + 1)
                memo[1][j] = min(memo[1][j], memo[0][j] + 1)
            elif obstacles[j] == 2:
                memo[0][j] = min(memo[0][j], memo[2][j] + 1)
                memo[2][j] = min(memo[2][j], memo[0][j] + 1)
            elif obstacles[j] != 0:
                memo[obstacles[j] - 1][j] = float('inf')
        return min(min(memo[0][len(obstacles) - 1], memo[1][len(obstacles) - 1]), memo[2][len(obstacles) - 1])

    # base: dp[0][0], dp[0][1], dp[0][2] = 1, 0, 1
    # dp[i][r] = min([dp[i-1][r], dp[i-1][(r+1)%3] + 1, dp[i-1][(r+2)%3] + 1]) for r = 0, 1, 2
    def minSideJumps(self, obstacles):
        n = len(obstacles) - 1
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = dp[0][2] = 1

        for i in range(1, n):
            for r in range(3):
                if obstacles[i] == r + 1 or obstacles[i + 1] == r + 1:
                    dp[i][r] = float('inf')
                else:
                    dp[i][r] = min([dp[i - 1][r],
                                    dp[i - 1][(r + 1) % 3] + 1,
                                    dp[i - 1][(r + 2) % 3] + 1])
        return min(dp[-1])

test = Solution()
print test.minSideJumps([0,1,2,3,0])
print test.minSideJumps([0,1,1,3,3,0])
print test.minSideJumps([0,2,1,0,3,0])
print test.minSideJumps([0,0,3,1,0,1,0,2,3,1,0])