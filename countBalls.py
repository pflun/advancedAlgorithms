class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        res = {}
        for i in range(lowLimit, highLimit + 1):
            tmp = 0
            for j in str(i):
                tmp += int(j)
            res[tmp] = res.get(tmp, 0) + 1
        rnt = 0
        for v in res.values():
            rnt = max(rnt, v)
        return rnt

test = Solution()
print test.countBalls(1, 10)
print test.countBalls(5, 15)
print test.countBalls(19, 28)