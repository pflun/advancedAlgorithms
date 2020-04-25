class Solution:
    # in-place
    def isPalindrome2(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].isalpha() and s[j].isalpha():
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                    continue
                else:
                    return False
            if not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
        return True

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
print test.isPalindrome2("A man, a plan, a canal: Panama")