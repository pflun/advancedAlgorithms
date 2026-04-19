# -*- coding: utf-8 -*-
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        if p1 == p2 == p3 == p4:
            return False

        def helper(a, b):
            return (b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1])

        distances = [helper(p1, p2), helper(p1, p3), helper(p1, p4), helper(p2, p3), helper(p2, p4), helper(p3, p4)]
        distances.sort()
        return True if distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5] else False

    # Follow-up: given n points, how many valid square exist?
    def countSquares(self, points):
        point_set = set(tuple(p) for p in points)
        count = 0

        # 遍历所有点对 (A, B)
        for A in points:
            for B in points:
                if A == B:
                    continue

                x1, y1 = A
                x2, y2 = B

                # 计算向量 AB
                dx, dy = x2 - x1, y2 - y1

                # 逆时针旋转 90 度，推算另外两个点 C 和 D
                C = (x2 - dy, y2 + dx)
                D = (x1 - dy, y1 + dx)

                # 如果 C 和 D 都在我们给定的点集里，说明构成了一个正方形
                if C in point_set and D in point_set:
                    count += 1

        # 每个正方形由 4 条有向边组成，因此被计算了 4 次
        return count // 4
