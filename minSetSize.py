class Solution(object):
    def minSetSize(self, arr):
        res = 0
        cnt = 0
        dic = {}
        for a in arr:
            dic[a] = dic.get(a, 0) + 1
        for i, j in sorted(dic.items(), key=lambda kv: kv[1], reverse=True):
            res += 1
            cnt += j
            if cnt >= len(arr) / 2:
                return res
        return res


test = Solution()
print test.minSetSize([3,3,3,3,5,5,5,2,2,7])
print test.minSetSize([7,7,7,7,7,7])
print test.minSetSize([1,9])
print test.minSetSize([1000,1000,3,7])
print test.minSetSize([1,2,3,4,5,6,7,8,9,10])