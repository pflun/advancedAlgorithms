class Solution(object):
    def processQueries(self, queries, m):
        res = []
        p = [x for x in range(1, m + 1)]
        for q in queries:
            idx = p.index(q)
            res.append(idx)
            p = [p[idx]] + p[:idx] + p[idx + 1:]
        return res

test = Solution()
print test.processQueries([3,1,2,1], 5)
print test.processQueries([4,1,2,2], 4)
print test.processQueries([7,5,5,8,3], 8)