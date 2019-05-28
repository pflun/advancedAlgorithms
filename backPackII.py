# -*- coding: utf-8 -*-
# 典型 01 背包问题
class Solution:
    """
    @param: m: An integer m denotes the size of a backpack
    @param: A: Given n items with size A[i]
    @param: V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # dp[i][j] 包里有 j 的空间，可以取前 i 个元素时，所能获得的最大收益。
        # dp[i][j] within first i elements with space j, maximum profit gain
        dp = [[0 for _ in range(m + 1)] for _ in range(len(A) + 1)]

        for i in range(1, len(A) + 1):
            for j in range(1, m + 1):
                if j - A[i - 1] >= 0:
                    # max(不放i, 放i则需减去i所占的空间)
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + V[i - 1])
                else:
                    # 不取
                    dp[i][j] = dp[i - 1][j]

        print dp
        return dp[len(A)][m]


test = Solution()
print test.backPackII(10, [2, 3, 5, 7], [1, 5, 2, 4])