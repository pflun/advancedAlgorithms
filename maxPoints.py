class Solution(object):
    # incorrect solution
    def maxPoints(self, points):
        slope = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[j][0] - points[i][0] != 0:
                    s = float(points[j][1] - points[i][1]) / float(points[j][0] - points[i][0])
                    tmp = slope.get(s, set())
                    tmp.add(i)
                    tmp.add(j)
                    slope[s] = tmp
        return slope

test = Solution()
print test.maxPoints([[1,1],[2,2],[3,3]])
print test.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])