# Amazon-findAnagrams.py
class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        res = []
        dicS = {}
        dicP = {}
        for c in p:
            dicP[c] = dicP.get(c, 0) + 1
        for i in range(len(p)):
            dicS[s[i]] = dicS.get(s[i], 0) + 1
        if dicS == dicP:
            res.append(0)
        for i in range(len(s) - len(p)):
            j = i + len(p)
            dicS[s[j]] = dicS.get(s[j], 0) + 1
            dicS[s[i]] = dicS.get(s[i], 0) - 1
            if dicS[s[i]] == 0:
                del dicS[s[i]]
            if dicS == dicP:
                res.append(i + 1) # i is the one getting removed, i + 1 is start of substring
        return res

test = Solution()
print test.findAnagrams("cbaebabacd", "abc")
print test.findAnagrams("abab", "ab")