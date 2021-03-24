#
class Solution:
    # @param {string} s a string
    # @param {string} t a string
    # @return {boolean} true if the characters in s
    # can be replaced to get t or false
    def isIsomorphic(self, s, t):
        pattern1 = {}
        pattern2 = {}

        i = 0
        while i < len(s):
            if s[i] not in pattern1:
                pattern1[s[i]] = t[i]

            if t[i] not in pattern2:
                pattern2[t[i]] = s[i]

            if s[i] in pattern1:
                currMatch = pattern1[s[i]]
                if currMatch != t[i]:
                    return False

            if t[i] in pattern2:
                currMatch = pattern2[t[i]]
                if currMatch != s[i]:
                    return False

            i += 1

        return True

test = Solution()
print test.isIsomorphic("egg", "add")
print test.isIsomorphic("foo", "bar")
print test.isIsomorphic("paper", "title")