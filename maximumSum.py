class Solution(object):
    def maximumSum(self, nums):
        dic = {}
        res = float('-inf')
        for n in nums:
            key = sum([int(x) for x in str(n)])
            dic[key] = dic.get(key, []) + [n]
        for v in dic.values():
            if len(v) >= 2:
                v.sort()
                res = max(res, v[-1] + v[-2])
        return -1 if res == float('-inf') else res

test = Solution()
print test.maximumSum([18,43,36,13,7])
print test.maximumSum([10,12,19,14])
