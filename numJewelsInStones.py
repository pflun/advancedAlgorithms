class Solution(object):
    def numJewelsInStones(self, J, S):
        dic = {}
        res = 0
        for j in J:
            dic[j] = 0

        for s in S:
            if s in dic:
                dic[s] = dic.get(s, 0) + 1

        for key, val in dic.items():
            res += val

        return res

test = Solution()
print test.numJewelsInStones("aA", "aAAbbbb")