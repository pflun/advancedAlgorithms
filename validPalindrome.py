# you may delete at most one character. Judge whether you can make it a palindrome
class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                skip_left = self.helper(s[left + 1: right + 1])
                skip_right = self.helper(s[left: right])
                if skip_left or skip_right:
                    return True
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

test = Solution()
print test.validPalindrome("aba")
print test.validPalindrome("acba")
print test.validPalindrome("aazzzzz")