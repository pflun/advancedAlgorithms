class Solution(object):
    def checkPalindromeFormation(self, a, b):
        if self.isPalindrome(a):
            return True
        if self.isPalindrome(b):
            return True
        if self.helper(a, b[::-1]):
            return True
        if self.helper(a[::-1], b):
            return True
        return False

    def helper(self, a, b):
        i = 0
        while a[i] == b[i]:
            i += 1
        if i >= len(a):
            return True
        if self.isPalindrome(a[i:len(a) - i]):
            return True
        if self.isPalindrome(b[i:len(a) - i]):
            return True
        else:
            return False

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
# print test.checkPalindromeFormation("x", "y")
# print test.checkPalindromeFormation("abdef", "fecab")
# print test.checkPalindromeFormation("ulacfd", "jizalu")
# print test.checkPalindromeFormation("xbdef", "xecab")
print test.checkPalindromeFormation("pvhmupgqeltozftlmfjjde", "yjgpzbezspnnpszebzmhvp")