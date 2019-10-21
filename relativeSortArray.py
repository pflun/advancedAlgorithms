class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        res = []
        dic = {}
        for a in arr1:
            dic[a] = dic.get(a, 0) + 1
        for a in arr2:
            for _ in range(dic[a]):
                res.append(a)
            del dic[a]
        for k in sorted(dic.keys()):
            for _ in range(dic[k]):
                res.append(k)
        return res

test = Solution()
print test.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])