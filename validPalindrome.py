# you may delete at most one character. Judge whether you can make it a palindrome
class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1
        used = 0

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            elif used == 0:
                if self.helper(s[left + 1: right + 1]) or self.helper(s[left: right]):
                    return True
                else:
                    return False
            else:
                return False
        return True

    def helper(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

print False or True