class Solution(object):
    def maximalNetworkRank(self, n, roads):
        dic = {}
        for r in roads:
            if r[0] not in dic:
                dic[r[0]] = set()
            dic[r[0]].add(r[1])
            if r[1] not in dic:
                dic[r[1]] = set()
            dic[r[1]].add(r[0])
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                r1 = dic.get(i, [])
                r2 = dic.get(j, [])
                if j in dic and i in dic[j]:
                    tmp = len(r1) + len(r2) - 1
                else:
                    tmp = len(r1) + len(r2)
                res = max(res, tmp)
        return res

test = Solution()
print test.maximalNetworkRank(4, [[0,1],[0,3],[1,2],[1,3]])
print test.maximalNetworkRank(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]])
print test.maximalNetworkRank(8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]])
print test.maximalNetworkRank(2, [])