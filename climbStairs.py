# -*- coding: utf-8 -*-

class Solution:
    # def climbStairs(self, n):
    #     if n == 0:
    #         return 1
    #     elif n == 1:
    #         return 1
    #     a = 1
    #     b = 2
    #     for i in range(2, n):
    #         tmp = b
    #         b = a + b
    #         a = tmp
    #     return b
    # 最后一步无非是1或2 递归一步步到最后一步 像fibonacci
    # Recursion
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # DP
    def climbStairs2(self, n):
        # write your code here
        if n == 0:
            return 1
        if n <= 2:
            return n
        result = [1, 2]
        for i in range(n - 2):
            result.append(result[-2] + result[-1])
        return result[-1]

test = Solution()
print test.climbStairs2(3)