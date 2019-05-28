# -*- coding: utf-8 -*-
# 我用三指针写了一下，但是看参考答案是DP
# LeetCode 727. Minimum Window Subsequence
# Input:
# S = "abcdebdde", T = "bde"
# Output: "bcde"
# Explanation:
# "bcde" is the answer because it occurs before "bdde" which has the same length.
# "deb" is not a smaller window because the elements of T in the window must occur in order.

class Solution(object):

    # DP
    def minWindowSubsequence(self, S, T):
        res = ''
        ls, lt = len(S), len(T)
        dp = [-1] * lt
        for x in range(ls):
            for y in range(lt - 1, -1, -1):
                if T[y] == S[x]:
                    dp[y] = dp[y - 1] if y else x
                    if y == lt - 1 and dp[-1] > -1:
                        nlen = x - dp[-1] + 1
                        if not res or nlen < len(res):
                            res = S[dp[-1]: x + 1]
        return res

    def minWindow(self, s, t):
        if len(t) == 0:
            return ''
        if len(s) == 0:
            return None

        res = ''
        for left in range(len(s)):
            if s[left] == t[0]:
                break
        right = left + len(t) - 1
        # 左右指针走到后面
        while right < len(s) or left < len(s) - len(t):
            # 找到则左指针走
            if self.isSubsequence(s, t, left, right):
                if len(res) == 0:
                    res = s[left:right + 1]
                else:
                    if len(res) > len(s[left:right + 1]):
                        res = s[left:right + 1]
                left += 1
            # 找不到右指针走继续找
            else:
                right += 1
        return res

    def isSubsequence(self, s, t, start, end):
        p = 0
        for char in s[start:end + 1]:
            if char == t[p]:
                p += 1
            if p == len(t):
                return True
        return False

test = Solution()
print test.minWindow("abcdebdde", "bde")