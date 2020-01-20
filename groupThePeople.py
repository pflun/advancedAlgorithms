class Solution(object):
    def groupThePeople(self, groupSizes):
        if len(groupSizes) == 0:
            return []
        dic = {}
        for i in range(len(groupSizes)):
            dic[groupSizes[i]] = dic.get(groupSizes[i], []) + [i]
        res = []
        for k, v in dic.items():
            while k in dic:
                tmp = dic[k][:k]
                res.append(tmp)
                if k == len(dic[k]):
                    del dic[k]
                else:
                    dic[k] = dic[k][k:]
        return res

test = Solution()
print test.groupThePeople([3,3,3,3,3,1,3])
print test.groupThePeople([2,1,3,3,3,2])