# -*- coding: utf-8 -*-
# https://leetcode.com/problems/maximum-number-of-visible-points/discuss/877822/Python-clean-sliding-window-solution-with-explanation
import math

class Solution(object):
    # sliding window
    def visiblePoints(self, points, angle, location):
        radians = []
        # 是否有多少个刚好在location的点
        includeLoc = 0
        for p in points:
            if p[1] == location[1] and p[0] == location[0]:
                includeLoc += 1
            else:
                curr = math.atan2(p[1] - location[1], p[0] - location[0])
                radians.append(curr)
        radians.sort()
        # circular array
        radians = radians + [x + 2.0 * math.pi for x in radians]
        angle = math.pi * angle / 180
        l = 0
        res = 0
        for r in range(len(radians)):
            while radians[r] - radians[l] > angle:
                l += 1
            res = max(res, r - l + 1)

        return res + includeLoc

test = Solution()
print test.visiblePoints([[2,1],[2,2],[3,3]], 90, [1, 1])
print test.visiblePoints([[2,1],[2,2],[3,4],[1,1]], 90, [1, 1])
print test.visiblePoints([[1,0],[2,1]], 13, [1, 1])
print test.visiblePoints([[1,0],[0,1], [2, 1], [1, 2]], 13, [1, 1])