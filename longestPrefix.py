class Solution(object):
    def longestPrefix(self, s):
        s1 = 0
        e1 = len(s) - 1
        s2 = 1
        e2 = len(s)
        while s1 <= e1 and s2 <= e2:
            if s[s1:e1] == s[s2:e2]:
                return s[s1:e1]
            else:
                e1 -= 1
                s2 += 1
        return ''

test = Solution()
print test.longestPrefix("level")
print test.longestPrefix("ababab")
print test.longestPrefix("leetcodeleet")
print test.longestPrefix("a")