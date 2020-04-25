# -*- coding: utf-8 -*-
# https://leetcode.com/problems/stone-game-iii/discuss/564419/Python3-Easy-Minimax-solution-(Top-Down-Approach)
class Solution:
    def stoneGameIII(self, stoneValue):
        memo = {}

        def dfs(start):
            if start >= len(stoneValue):
                return 0

            if start in memo:
                return memo[start]

            memo[start] = float('-inf')
            score = 0

            # 从当前index依次往后取三个值，尝试本次能获得最大分，minmax问题所以是当前score - 对方能获得最大分dfs()
            for i in range(start, min(len(stoneValue), start + 3)):
                score += stoneValue[i]
                memo[start] = max(memo[start], score - dfs(i + 1))

            return memo[start]

        score = dfs(0)
        return 'Tie' if score == 0 else 'Alice' if score > 0 else 'Bob'

test = Solution()
print test.stoneGameIII([1,2,3,7])
print test.stoneGameIII([1,2,3,-9])
print test.stoneGameIII([1,2,3,6])