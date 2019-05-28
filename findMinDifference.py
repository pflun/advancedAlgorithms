class Solution(object):
    def findMinDifference(self, timePoints):
        if len(timePoints) <= 1:
            return 0
        res = float('inf')
        timePoints.sort()
        for i in range(len(timePoints) - 1):
            t1 = timePoints[i].split(':')
            t2 = timePoints[i + 1].split(':')

            t1 = int(t1[0]) * 60 + int(t1[1])
            t2 = int(t2[0]) * 60 + int(t2[1])

            res = min(res, t2 - t1)

        t1 = timePoints[0].split(':')
        t2 = timePoints[-1].split(':')
        t1 = int(t1[0]) * 60 + int(t1[1])
        t2 = int(t2[0]) * 60 + int(t2[1])

        # 24 hrs = 1440 min
        tmp = min(t2 - t1, t1 + 1440 - t2)
        res = min(res, tmp)

        return res

test = Solution()
print test.findMinDifference(["23:59","00:00","00:05"])