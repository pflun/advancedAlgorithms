# -*- coding: utf-8 -*-
class Solution(object):
    # Brutal force
    def countSubstrings(self, s):
        res = 0
        for i in range(0, len(s)):
            for j in range(i + 1, len(s) + 1):
                if self.isValid(s[i:j]):
                    res += 1

        return res

    def isValid(self, string):
        i = 0
        j = len(string) - 1
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True

    # 中心扩展法
    def countSubstrings2(self, s):
        self.res = 0
        for i in range(len(s)):
            # 奇数向外扩展
            self.helper(s, i, i)
            # 偶数向外扩展
            self.helper(s, i, i + 1)

        return self.res

    def helper(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                self.res += 1
                left -= 1
                right += 1
            # 有不对称就没必要继续找下去，break
            else:
                break

test = Solution()
print test.countSubstrings2('abcba')