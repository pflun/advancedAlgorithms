class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        res = 0
        for i in range(len(points) - 1):
            res += self.getDistance(points[i], points[i + 1])
        return res

    def getDistance(self, a, b):
        if a[0] == b[0]:
            return abs(a[1] - b[1])
        elif a[1] == b[1]:
            return abs(a[0] - b[0])
        else:
            return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

test = Solution()
print test.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
print test.minTimeToVisitAllPoints([[3,2],[-2,2]])