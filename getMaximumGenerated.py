class Solution(object):
    def getMaximumGenerated(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        res = [0, 1]
        for i in range(2, n + 1):
            if i % 2 == 0:
                res.append(res[i / 2])
            else:
                res.append(res[i / 2] + res[i / 2 + 1])
        return max(res)

test = Solution()
print test.getMaximumGenerated(7)
print test.getMaximumGenerated(2)
print test.getMaximumGenerated(3)
print test.getMaximumGenerated(15)