class Solution:
    """
    @param: s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # Rm punctuation, space and lowercase
        import string
        s = "".join(l for l in s if l not in string.punctuation).replace(" ", "").lower()
        # s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

test = Solution()
print test.isPalindrome("A man, a plan, a canal: Panama")