# -*- coding: utf-8 -*-
# 成对出现，至多可能中间有奇数个
class Solution(object):
    def canPermutePalindrome(self, s):
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1

        for key, val in dic.items():
            if val % 2 == 0:
                dic.pop(key)

        if len(dic) <= 1:
            return True

        return False

test = Solution()
print test.canPermutePalindrome("carerac")