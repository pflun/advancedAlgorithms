# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=DguJN47_mSg
# 这题很明显Greedy，但是居然是按end时间点排序的
class Solution(object):
    def findMinArrowShots(self, points):
        if len(points) == 0:
            return 0
        points.sort(key=lambda x: x[1])
        res = 0
        curr = points[0]
        for p in points[1:]:
            s = max(curr[0], p[0])
            e = min(curr[1], p[1])
            if s <= e:
                curr = [s, e]
            else:
                res += 1
                curr = p
        return res + 1

test = Solution()
print test.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]])
print test.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]])