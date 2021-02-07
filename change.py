# -*- coding: utf-8 -*-
# https://leetcode.com/problems/coin-change-2/discuss/176706/Beginner-Mistake%3A-Why-an-inner-loop-for-coins-doensn't-work-Java-Soln
# 2D: dp[i][j]="number of ways to get sum 'j' using 'first i' coins"
# 1D: dp存每个amount（对于前n个硬币）的comb数，那么每新加一个coin就累加之前计算过的comb数
# 之所以1D两个loop顺序不能变是dp定义的问题，2D就可以变
class Solution(object):
    def change(self, amount, coins):
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for c in coins:
            for i in range(1, len(dp)):
                if i - c >= 0:
                    dp[i] += dp[i - c]
        return dp[-1]

test = Solution()
print test.change(5, [1, 2, 5])
print test.change(3, [2])
print test.change(10, [10])