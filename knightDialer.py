# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=HTnIFivp0aw
class Solution(object):
    def knightDialer(self, N):
        dp = [[1 for _ in range(10)] for _ in range(N)]
        dp[0][4] = 0

        for k in range(1, N):
            # dp 0位置对应键盘上数字1，因为数字1可以从数字8和6跳过来，所以dp 1 = dp (7 + 5) 同理数字8对应dp7，数字6对应dp5
            dp[k][0] = dp[k - 1][7] + dp[k - 1][5]
            dp[k][1] = dp[k - 1][6] + dp[k - 1][8]
            dp[k][2] = dp[k - 1][3] + dp[k - 1][7]
            dp[k][3] = dp[k - 1][2] + dp[k - 1][8] + dp[k - 1][9]
            dp[k][4] = 0
            dp[k][5] = dp[k - 1][0] + dp[k - 1][6] + dp[k - 1][9]
            dp[k][6] = dp[k - 1][1] + dp[k - 1][5]
            dp[k][7] = dp[k - 1][0] + dp[k - 1][2]
            dp[k][8] = dp[k - 1][1] + dp[k - 1][3]
            dp[k][9] = dp[k - 1][3] + dp[k - 1][5]
        return sum(dp[-1]) % 1000000007

test = Solution()
print test.knightDialer(3)