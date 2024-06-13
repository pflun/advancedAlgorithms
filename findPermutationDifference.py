class Solution(object):
    def findPermutationDifference(self, s, t):
        dicS = {}
        dicT = {}
        for i in range(len(s)):
            dicS[s[i]] = i
        for i in range(len(t)):
            dicT[t[i]] = i
        res = 0
        for k, v in dicS.items():
            res += abs(v - dicT[k])
        return res