# dp[i][j] means the biggest number of stones you can get more than opponent picking piles in piles[i] ~ piles[j].
# You can first pick piles[i] or piles[j].
#
# If you pick piles[i], your result will be piles[i] - dp[i + 1][j]
# If you pick piles[j], your result will be piles[j] - dp[i][j - 1]
# So we get:
# dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
# We start from smaller subarray and then we use that to calculate bigger subarray.
def stoneGame(p):
    n = len(p)
    dp = [[0] * n for i in range(n)]
    for i in range(n): dp[i][i] = p[i]
    for d in range(1, n):
        for i in range(n - d):
            dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])
    return dp[0][-1] > 0