class Solution(object):
    def numWays(self, steps, arrLen):
        dp = [[None for _ in range(arrLen + 1)] for _ in range(steps + 1)]
        dp[0][0] = 1

        for i in range(1, steps + 1):
            for j in range(arrLen + 1):
                if j == 0:
                    left = 0
                    if dp[i - 1][j + 1]:
                        right = dp[i - 1][j + 1]
                    else:
                        right = 0
                    if dp[i - 1][j]:
                        middle = dp[i - 1][j]
                    else:
                        middle = 0
                elif j == arrLen:
                    right = 0
                    if dp[i - 1][j - 1]:
                        left = dp[i - 1][j - 1]
                    else:
                        left = 0
                    if dp[i - 1][j]:
                        middle = dp[i - 1][j]
                    else:
                        middle = 0
                else:
                    if dp[i - 1][j - 1]:
                        left = dp[i - 1][j - 1]
                    else:
                        left = 0
                    if dp[i - 1][j + 1]:
                        right = dp[i - 1][j + 1]
                    else:
                        right = 0
                    if dp[i - 1][j]:
                        middle = dp[i - 1][j]
                    else:
                        middle = 0
                dp[i][j] = left + middle + right

        print dp
        return dp[-1][0] if dp[-1][0] else -1

test = Solution()
print test.numWays(3, 2)
print test.numWays(2, 4)
print test.numWays(4, 2)