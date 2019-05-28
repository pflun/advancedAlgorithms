class Solution(object):
    def findJudge(self, N, trust):
        dic = {}
        for i in range(1, N + 1):
            dic[i] = i

        for t in trust:
            dic[t[0]] = t[1]

        for k, v in dic.items():
            if k == v:
                return k
        return -1

test1 = Solution()
print test1.findJudge(3, [[1,3],[2,3]])