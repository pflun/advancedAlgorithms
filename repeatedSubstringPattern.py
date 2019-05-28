# -*- coding: utf-8 -*-
# 有点像rotated string，S="helloworld" T="lloworldhe"， T是S的rotated string 我们只需要在 T + T 中找 strStr S
#
# How do we apply that to this problem? We consider every rotation of string S such that it’s rotated by k units [k < len(S)] to the left.
# Specifically, we’re looking at strings "elloworldh", "lloworldhe", "loworldhel", etc...
# If we have a string that is periodic (i.e. is made up of strings that are the same and repeat R times),
# then we can check if the string is equal to some rotation of itself, and if it is, then we know that the string is periodic.
# Checking if S is a sub-string of (S+S)[1:-1] basically checks if the string is present in a rotation of itself for all values of R such that 0 < R < len(S).

class Solution(object):
    def repeatedSubstringPattern(self, s):

        s2 = s[1:] + s[:-1]

        for i in range(len(s) - 2):
            if s == s2[i:i + len(s)]:
                return True

        return False

test = Solution()
print test.repeatedSubstringPattern('abcabcabcabc')