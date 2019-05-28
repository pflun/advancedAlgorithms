class Solution(object):
    def findLHS(self, nums):
        dic = {}
        res = 1
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, val in dic.items():
            for key2, val2 in dic.items():
                if key != key2:
                    if abs(key - key2) == 1:
                        res = max(res, val + val2)

        # Sort by Key
        for key in sorted(dic.iterkeys()):
            print "%s: %s" % (key, dic[key])

        # Sort by Value
        for key, value in sorted(dic.iteritems(), key=lambda (k, v): (v, k)):
            print "%s: %s" % (key, value)

        return res

test = Solution()
print test.findLHS([1,3,2,2,5,2,3,7])