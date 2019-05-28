# -*- coding: utf-8 -*-
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # dp[i][j] for the first i elements, can we make sum of j
        # Tip: create empty 2D array
        dp = [[0 for _ in range(m + 1)] for _ in range(len(A) + 1)]

        # init
        for i in range(len(A)):
            dp[i][0] = True

        for i in range(1, len(A) + 1):
            for j in range(1, m + 1):
                if j - A[i - 1] >= 0:
                    # dp[i][sum] = 前 i 个元素里我们能不能凑出来 sum.
                    # dp[i][sum] 要么取决于 dp[i - 1][sum] (不取当前元素),
                    # 要么取决于 dp[i - 1][sum - nums[i]] (取当前元素), 其中每一行 i 都只考虑前一行 i - 1 的值。
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
                else:
                    # 不取
                    dp[i][j] = dp[i - 1][j]

        for i in range(m, -1, -1):
            if dp[len(A)][i]:
                return i

        return -1

test = Solution()
print test.backPack(11, [2, 3, 5, 7])