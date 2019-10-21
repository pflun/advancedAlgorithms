# -*- coding: utf-8 -*-
# https://leetcode.com/problems/replace-the-substring-for-balanced-string/discuss/408978/JavaC%2B%2BPython-Sliding-Window
class Solution(object):
    def balancedString(self, s):
        count = collections.Counter(s)
        res = n = len(s)
        i = 0
        for j, c in enumerate(s):
            count[c] -= 1
            while i < n and all(n / 4 >= count[c] for c in 'QWER'):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res

    # 注意这题是substring不是character，contest时理解错了
    def forgetthis(self, s):
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        res = 0
        for v in dic.values():
            if v > len(s) / 4:
                res += v - len(s) / 4
        return res, dic, len(s)

test = Solution()
print test.balancedString("QWER")
print test.balancedString("QQWE")
print test.balancedString("QQQW")
print test.balancedString("QQQQ")
print test.balancedString("WWEQERQWQWWRWWERQWEQ")