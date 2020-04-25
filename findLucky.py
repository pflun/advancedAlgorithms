class Solution(object):
    def findLucky(self, arr):
        dic = {}
        for a in arr:
            dic[a] = dic.get(a, 0) + 1
        res = -1
        for k, v in dic.items():
            if k == v:
                res = max(res, k)
        return res

test = Solution()
print test.findLucky([2,2,3,4])
print test.findLucky([1,2,2,3,3,3])
print test.findLucky([2,2,2,3,3])
print test.findLucky([5])
print test.findLucky([7,7,7,7,7,7,7])