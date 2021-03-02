# -*- coding: utf-8 -*-
# 由每个字符作为起点，往两边扫。
# DP: n乘n bool数组存从［i，j］是否为回文串，子问题是否是回文串是由"头尾两个char是否相等 ＋ 中间substring是否回文"决定的
class Solution(object):
    def longestPalindrome3(self, s):
        ans = ''
        max_len = 0
        n = len(s)
        DP = [[0] * n for _ in xrange(n)]
        for i in xrange(n):
            DP[i][i] = True
            max_len = 1
            ans = s[i]
        for i in xrange(n - 1):
            if s[i] == s[i + 1]:
                DP[i][i + 1] = True
                ans = s[i:i + 2]
                max_len = 2
        for j in xrange(n):
            for i in xrange(0, j - 1):
                if s[i] == s[j] and DP[i + 1][j - 1]:
                    DP[i][j] = True
                    if max_len < j - i + 1:
                        ans = s[i:j + 1]
                        max_len = j - i + 1
        return ans

    def longestPalindrome(self, s):
        if len(s) == 0:
            return ''

        res = ''

        for i in range(len(s)):
            left = i - 1
            right = i + 1
            tmpOdd = 1
            tmpEven = 0
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    tmpOdd += 2
                    left -= 1
                    right += 1
                else:
                    break

            start = i
            end = i + 1
            while start >= 0 and end <= len(s) - 1:
                if s[start] == s[end]:
                    tmpEven += 1
                    start -= 1
                    end += 1
                else:
                    break

            if tmpOdd > tmpEven:
                subRes = s[left + 1: right]
            else:
                subRes = s[start + 1: end]

            if len(subRes) > len(res):
                res = subRes

        return res

    # 有一点test case 没过，分奇偶两边扫
    def longestPalindrome2(self, s):
        # write your code here
        self.res = ''
        for i in range(len(s)):
            # odd
            offset = 1
            while i - offset >= 0 and i + offset < len(s):
                if self.isPalindrome(s[i - offset:i + offset + 1]):
                    if len(self.res) < len(s[i - offset:i + offset + 1]):
                        self.res = s[i - offset:i + offset + 1]
                offset += 1

            # even
            offset = 1
            while i - offset >= 0 and i + offset < len(s) + 1:
                if self.isPalindrome(s[i - offset:i + offset]):
                    if len(self.res) < len(s[i - offset:i + offset]):
                        self.res = s[i - offset:i + offset]
                offset += 1

        return self.res

    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

test = Solution()
print test.longestPalindrome2("aaaa")