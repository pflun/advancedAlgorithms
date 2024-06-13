class Solution(object):
    def findMatrix(self, nums):
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        res = []
        while dic:
            tmp = []
            for k, v in sorted(dic.items(), key=lambda x: x[1]):
                tmp.append(k)
                dic[k] -= 1
                if dic[k] == 0:
                    del dic[k]
            res.append(tmp)
        return res