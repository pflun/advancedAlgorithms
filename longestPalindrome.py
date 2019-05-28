class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0

        dic = {}
        res = 0
        odd = 0

        for char in s:
            dic[char] = dic.get(char, 0) + 1

        for key, val in dic.items():
            if val % 2 == 0:
                res += val
            else:
                odd = max(odd, val)

        return res + odd

test = Solution()
print test.longestPalindrome("abccccdd")