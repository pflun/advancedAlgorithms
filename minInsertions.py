# -*- coding: utf-8 -*-
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
class Solution(object):
    # 超时，必须用lru-cache
    def minInsertions(self, s):
        def dp(i, j):
            # base case, 如果1个字符 or 没字符了
            if i >= j:
                return 0
            # 极左 = 极右，就求中间段最少插入几个
            if s[i] == s[j]:
                return dp(i + 1, j - 1)
            # 极左 != 极右，就或右边插(i + 1, j) 或左边插(i, j - 1)
            else:
                return min(dp(i + 1, j), dp(i, j - 1)) + 1
        return dp(0, len(s) - 1)

    def minInsertions2(self, s):
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for l in range(2, len(s) + 1):
            i = 0
            j = l - 1
            while j < len(s):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
                i += 1
                j += 1
        return dp[0][len(s) - 1], dp

test = Solution()
print test.minInsertions2("mbadm")