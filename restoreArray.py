class Solution(object):
    def restoreArray(self, adjacentPairs):
        dic = {}
        for a in adjacentPairs:
            if a[0] in dic:
                dic.get(a[0]).append(a[1])
            else:
                dic[a[0]] = [a[1]]
            if a[1] in dic:
                dic.get(a[1]).append(a[0])
            else:
                dic[a[1]] = [a[0]]
        res = []
        for k, v in dic.items():
            if len(v) == 1:
                res.append(k)
                res.append(v[0])
                break
        while len(res) < len(adjacentPairs) + 1:
            next = res[-1]
            candidates = dic.get(next)
            if res[-2] == candidates[0]:
                res.append(candidates[1])
            elif res[-2] == candidates[1]:
                res.append(candidates[0])
        return res

test = Solution()
print test.restoreArray([[2,1],[3,4],[3,2]])
print test.restoreArray([[4,-2],[1,4],[-3,1]])
print test.restoreArray([[100000,-100000]])