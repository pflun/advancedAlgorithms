# -*- coding: utf-8 -*-
# 一个矩阵，要求奇数偶数跳着走，前提矩阵一定是valid的，要求从（0,0）走到（n-1, m-1），方向也一定是向下或者向右，问有没有此路径
class Solution(object):
    def hasOddEvenPaths(self, matrix):
        # dp[0] 矩阵为走到此点有没有路径 && 当前点为偶数，dp[1]有没有路径且当前点为奇数
        dp = [[[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))], [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]]
        # init
        if matrix[0][0] % 2 == 0:
            dp[0][0][0] = 1
        else:
            dp[1][0][0] = 1
        for i in range(1, len(matrix[0])):
            if matrix[0][i] % 2 != 0 and dp[0][0][i - 1] == 1:
                dp[1][0][i] = 1
            elif matrix[0][i] % 2 == 0 and dp[1][0][i - 1] == 1:
                dp[0][0][i] = 1
        for j in range(1, len(matrix)):
            if matrix[j][0] % 2 != 0 and dp[0][j - 1][0] == 1:
                dp[1][j][0] = 1
            elif matrix[j][0] % 2 == 0 and dp[1][j - 1][0] == 1:
                dp[0][j][0] = 1

        for i in range(1, len(matrix[0])):
            for j in range(1, len(matrix)):
                if matrix[j][i] % 2 == 0:
                    if dp[1][j - 1][i] == 1 or dp[1][j][i - 1] == 1:
                        dp[0][j][i] = 1
                elif matrix[j][i] % 2 != 0:
                    if dp[0][j - 1][i] == 1 or dp[0][j][i - 1] == 1:
                        dp[1][j][i] = 1

        return True if dp[0][-1][-1] == 1 or dp[1][-1][-1] == 1 else False

test = Solution()
print test.hasOddEvenPaths([
    [2, 1, 1],
    [1, 2, 2],
    [1, 1, 2]
])

