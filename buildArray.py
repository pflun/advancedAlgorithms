class Solution(object):
    def buildArray(self, target, n):
        res = []
        i = 0
        cnt = 1
        while cnt <= max(target):
            if cnt == target[i]:
                res.append('Push')
                cnt += 1
                i += 1
            elif cnt < target[i]:
                res.append('Push')
                res.append('Pop')
                cnt += 1
        return res

test = Solution()
print test.buildArray([1,3], 3)
print test.buildArray([1,2,3], 3)
print test.buildArray([1,2], 4)
print test.buildArray([2,3,4], 4)