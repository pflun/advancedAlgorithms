class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        l = 0
        r = 1
        res = 1
        used = False
        while r < len(s):
            if s[r] != s[r - 1]:
                res = max(res, r - l + 1)
                r += 1
            else:
                if not used:
                    used = True
                    res = max(res, r - l + 1)
                    r += 1
                else:
                    used = False
                    while s[l] != s[l + 1]:
                        l += 1
                    l += 1
        return res
