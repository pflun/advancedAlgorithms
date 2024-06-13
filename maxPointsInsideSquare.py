# -*- coding: utf-8 -*-
# 不是按照到0点距离排序，而是最大边到0点距离排序，这样才能被square包围
# sorted dic 找每次扩展square能否包围新的points
class Solution(object):
    def maxPointsInsideSquare(self, points, s):
        dic = {}
        for i in range(len(points)):
            maxSide = max(abs(points[i][0]), abs(points[i][1]))
            distance = maxSide * maxSide + maxSide * maxSide
            dic[distance] = dic.get(distance, []) + [s[i]]

        res = 0
        visited = set()
        for k, v in sorted(dic.items()):
            for c in v:
                if c in visited:
                    return res
                else:
                    visited.add(c)
            res += len(v)
        return res

test = Solution()
print test.maxPointsInsideSquare([[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], "abdca")
print test.maxPointsInsideSquare([[1,1],[-2,-2],[-2,2]], "abb")
print test.maxPointsInsideSquare([[1,1],[-1,-1],[2,-2]], "ccd")
print test.maxPointsInsideSquare([[1,-1]], "a")