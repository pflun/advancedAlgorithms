# you may delete at most k character. Judge whether you can make it a palindrome
class Solution(object):
    def isValidPalindrome(self, s, k):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if k == 0:
                    return False
                else:
                    skip_left = self.isValidPalindrome(s[left + 1: right + 1], k - 1)
                    skip_right = self.isValidPalindrome(s[left: right], k - 1)
                    if skip_left or skip_right:
                        return True
                    else:
                        return False
        return True

test = Solution()
# True, Remove 'b' and 'e' characters.
print test.isValidPalindrome("abcdeca", 2)
# True
print test.isValidPalindrome("abbababa", 1)