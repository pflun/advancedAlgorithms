# -*- coding: utf-8 -*-
# https://leetcode.com/problems/longest-string-chain/discuss/294890/C%2B%2BJavaPython-DP-Solution
# 按length排序
# 对于每一个字符串，取走一个字母，看剩下的在不在cache里，如果在当前长度就是cache[取走剩下的] + 1，找所有取走可能性里能达到最长的长度并存进cache
class Solution(object):
    def longestStrChain(self, words):
        words = sorted(words, key=len)
        dp = {}
        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                tmp = w[:i] + w[i + 1:]
                if tmp in dp:
                    dp[w] = max(dp[w], dp[tmp] + 1)
        res = 0
        for v in dp.values():
            res = max(res, v)
        return res

test = Solution()
print test.longestStrChain(["a","b","ba","bca","bda","bdca"])