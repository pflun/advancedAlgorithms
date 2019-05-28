# -*- coding: utf-8 -*-
# 建立一个三维dp数组，其中dp[i][j][k]表示从开头遍历到数字nums[i][j]为止，
# 第k种情况的连续1的个数，k的值为0，1，2，3，分别对应水平，竖直，对角线和逆对角线这四种情况。
# 之后就是更新dp数组的过程了，如果如果数字为0的情况直接跳过，然后水平方向就加上前一个的dp值，竖直方向加上上面一个数字的dp值，
# 对角线方向就加上右上方数字的dp值，逆对角线就加上左上方数字的dp值，然后每个值都用来更新结果res
class Solution(object):
    def longestLine(self, M):
        res = 0
        dp = [[[-1 for _ in range(4)] for col in range(len(M[0]))] for row in range(len(M))]
        # initialize
        for i in range(len(M[0])):
            if M[0][i] == 1:
                dp[0][i][0] = 1
                dp[0][i][1] = 1
                dp[0][i][2] = 1
                dp[0][i][3] = 1
            elif M[0][i] == 0:
                dp[0][i][0] = 0
                dp[0][i][1] = 0
                dp[0][i][2] = 0
                dp[0][i][3] = 0
        for j in range(len(M)):
            if M[j][0] == 1:
                dp[j][0][0] = 1
                dp[j][0][1] = 1
                dp[j][0][2] = 1
                dp[j][0][3] = 1
            elif M[j][0] == 0:
                dp[j][0][0] = 0
                dp[j][0][1] = 0
                dp[j][0][2] = 0
                dp[j][0][3] = 0
        for i in range(1, len(M)):
            for j in range(1, len(M[0])):
                if M[i][j] == 1:
                    dp[i][j][0] = dp[i][j - 1][0] + 1
                    dp[i][j][1] = dp[i - 1][j][1] + 1
                    dp[i][j][2] = dp[i - 1][j - 1][2] + 1
                    if j == len(M[0]) - 1:
                        dp[i][j][3] = 1
                    else:
                        dp[i][j][3] = dp[i - 1][j + 1][3] + 1
                elif M[i][j] == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = 0
                    dp[i][j][2] = 0
                    dp[i][j][3] = 0
        # find longest in DP
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                res = max(res, max(dp[i][j]))
        return res

test = Solution()
print test.longestLine(
    [[0,1,1,0],
    [0,1,1,0],
    [0,0,0,1]])