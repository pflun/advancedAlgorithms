# Minimum number of squares whose sum equals to given number n
# https://www.geeksforgeeks.org/minimum-number-of-squares-whose-sum-equals-to-given-number-n/
from math import sqrt
class Solution(object):
    def getMinSquares(self, n):
        # 1 1+1 1+1+1, until 4 = 2*2
        dp = [0, 1, 2, 3]

        for i in range(4, n + 1):
            # worst case all 1s
            dp.append(i)
            for j in range(1, int(sqrt(i)) + 1):
                tmp = j * j
                if tmp > i:
                    break
                dp[i] = min(dp[i], 1 + dp[i - tmp])
        return dp[-1]

test = Solution()
print test.getMinSquares(4)
print test.getMinSquares(8)