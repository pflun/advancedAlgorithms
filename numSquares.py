# -*- coding: utf-8 -*-
class Solution(object):
    def numSquares(self, n):
        dp = [float("inf") for x in xrange(n + 1)]
        dp[0] = 0
        i = 0
        while i <= n:
            j = 1
            while j * j <= i:
                # dp[i]: integer i can be consist of least number of square
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                # print i, j, dp[i - j * j], dp[i]
                j += 1
            i += 1
        return dp[n]

    # Recursion, traverse all squares that less than n, call function for (n - square)
    def numSquares2(self, n):
        res = n
        # num = 1 is meaningless (res = n)
        num = 2
        while num * num <= n:
            a = n / (num * num)
            b = n % (num * num)
            res = min(res, a + self.numSquares2(b))
            # print num, a, b, res
            num += 1
        return res

    # Recursion, num从1开始每次不加或加一，当前余下的数减去(num * num)继续传入递归函数
    def numSquares3(self, n):
        self.res = n

        def helper(curr, num, remain):
            square = num * num

            # Exit: if remain not enough
            if remain < square:
                return
            if remain - square == 0:
                self.res = min(self.res, curr + 1)
                return
            else:
                tmp = remain - square

            helper(curr + 1, num, tmp)
            helper(curr + 1, num + 1, tmp)

        for i in range(1, n):
            helper(0, i, n)

        return self.res

test = Solution()
print test.numSquares3(12)