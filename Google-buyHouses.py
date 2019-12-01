# -*- coding: utf-8 -*-
# 热身题：输入一排房子的房价nums和我的预算budget，只能买连续的房子，输出最多能买多少幢。
# 给定m*n的房价矩阵matrix和预算budget，只能买成片的房子，输出能买的最大正方形边长。
# 我：枚举上边界top，枚举下边界down，枚举每一列col，过程中维护矩阵的prefix sum array。
# 这样将二维的prefix sum matrix降维成一维的prefix sum array。当前正方形边长为down-top+1，在枚举每一列的时候，
# 利用prefix sum array在O(1)的时间检查该正方形之和是不是小于等于budget。
# 给面试官解释为什么总复杂度是O(n^3)，他说O(n^3)非常好，我追问还有更好的做法么？他说应该能达到O(n^2)
class Solution(object):
    def buyHouses(self, matrix, budget):
        if len(matrix) == 0:
            return 0
        sum = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res = 0

        tmp = 0
        for j in range(len(matrix[0])):
            if matrix[0][j] < budget:
                res = 1
            tmp += matrix[0][j]
            sum[0][j] = tmp
        tmp = 0
        for i in range(len(matrix)):
            if matrix[i][0] < budget:
                res = 1
            tmp += matrix[i][0]
            sum[i][0] = tmp

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                sum[i][j] = matrix[i][j] + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                for k in range(1, min(len(matrix[0]) - j, len(matrix) - i)):
                    tmp = sum[i + k][j + k] - sum[i][j + k] - sum[i + k][j] + sum[i][j]
                    if tmp <= budget:
                        res = max(res, k)
        return res

test = Solution()
print test.buyHouses([
    [1, 3, 5, 7, 100, 8],
    [10, 11, 16, 20, 21, 20],
    [23, 30, 34, 50, 5, 19],
    [51, 53, 60, 70, 8, 7],
    [52, 54, 61, 71, 10, 2]
], 300)