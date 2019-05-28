# -*- coding: utf-8 -*-
# dp: 当前的钱数 ==> 需要最小多少枚
class Solution(object):
    def coinChange(self, coins, amount):

        dp = [amount + 1 for _ in range(amount + 1)]
        # init
        dp[0] = 0
        for i in xrange(1, amount + 1):
            for c in coins:
                # 当前的钱数必须大于coin面值
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        # amount + 1 表示取不到
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]

    def findMinCoins(self, coins, target):
        self.res = float('inf')

        def dfs(coins, target, i,  sum, number):
            if sum > target or i == len(coins):
                return
            elif sum == target:
                self.res = min(self.res, number)
            else:
                dfs(coins, target, i, sum + coins[i], number + 1)
                if i < len(coins) - 1:
                    dfs(coins, target, i + 1, sum + coins[i + 1], number + 1)

        for i in range(len(coins)):
            dfs(coins, target, i, coins[i], 1)

        return self.res

test = Solution()
print test.coinChange([1, 2, 5], 11)
