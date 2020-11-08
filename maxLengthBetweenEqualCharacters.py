class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        res = -1
        for i in range(len(s) - 1):
            left = s[i]
            for j in range(i + 1, len(s)):
                if s[j] == left:
                    res = max(res, j - i - 1)
        return res

test = Solution()
print test.maxLengthBetweenEqualCharacters("cbzxy")
print test.maxLengthBetweenEqualCharacters("cabbac")