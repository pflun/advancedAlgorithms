# -*- coding: utf-8 -*-
# isPalindrome 函数去判断一个 substring 是不是 palindrome
# 然后从给定的 string 左面开始一直往右扫，去找到从最左边字符开始，最长的 palindrome
# 然后把剩下的右边部分复制一份，翻转，接到原来的 string 上
class Solution(object):
    def shortestPalindrome(self, s):
        maxIndex = 0
        for i in range(1, len(s)):
            if self.isPalindrome(s[:i + 1]):
                maxIndex = max(maxIndex, i)

        mid = s[:maxIndex + 1]
        last = s[maxIndex + 1:]
        # reverse last part
        first = last[::-1]

        return first + mid + last


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
print test.shortestPalindrome("aaacecaaa")