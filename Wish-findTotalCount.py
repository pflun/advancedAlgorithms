# -*- coding: utf-8 -*-
# 就是有n个人比赛,问你有多少种比赛结果排名,每个人可以独自一人一组,
# 也可以和其他人组成团体,
# 比如n= 2, 两个人A,B,
# 可能的结果有3种
# A 第一,B 第二
# B 第一,A 第二
# A, B 团体第一
# 就是有n个人, 比赛, 问你有多少种比赛结果排名, 每个人可以独自一人一组,
# 也可以和其他人组成团体,
# 比如n = 2, 两个人 A,B,
# 可能的结果有3种
# A 第一, B 第二
# B 第一, A 第二
# A, B 团体第一
# n = 3, 有 13 种可能
# dp[0] = 1;
# dp[1] = 1;
# dp count with i persons

class Solution(object):
    def findTotalCount(self, n):
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for k in range(i):
                dp[i] += self.helper(i, i - k) * dp[k]
        return dp

    def helper(self, n, k):
        res = 1
        for i in range(n - k, n + 1):
            res *= i
        for i in range(1, k + 1):
            res /= i
        return res

test = Solution()
print test.findTotalCount(3)