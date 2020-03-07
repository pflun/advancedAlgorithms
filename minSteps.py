class Solution(object):
    def minSteps(self, s, t):
        dic1 = {}
        dic2 = {}
        for c in s:
            dic1[c] = dic1.get(c, 0) + 1
        for c in t:
            dic2[c] = dic2.get(c, 0) + 1

        for k, v1 in dic1.items():
            if k in dic2:
                v2 = dic2[k]
                dic1[k] = max(0, v1 - v2)
        res = 0
        for v in dic1.values():
            res += v
        return res

test = Solution()
print test.minSteps("bab", "aba")
print test.minSteps("leetcode", "practice")
print test.minSteps("anagram", "mangaar")
print test.minSteps("xxyyzz", "xxyyzz")
print test.minSteps("friend", "family")