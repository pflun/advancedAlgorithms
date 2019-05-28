# -*- coding: utf-8 -*-
# 任取两点当对角线做矩形，存在set里。若已有set存在则因为另外一个对角线存在，更新面积
# 没写完，parallel那种好写一点，比较容易根据对角线求两外两点
class Solution:
    def minAreaFreeRect(self, points):
        self.combine = []
        self.used = [False] * (len(points) + 1)
        self.exist = set((p[0], p[1]) for p in points)
        self.res = float('inf')

        def dfs(n, tmp, prev):
            if len(tmp) == 2:
                # shallow copy
                self.combine.append(tmp[:])

            for i in range(prev, n):
                if self.used[i]:
                    continue
                self.used[i] = True
                tmp.append(points[i])
                dfs(n, tmp, i)
                # backtracking:
                self.used[i] = False
                tmp.pop()

        dfs(len(points), [], 0)

        def getArea(c):
            return abs(c[1][0] - c[0][0]) * abs(c[1][1] - c[0][1])

        # 这个求的是parallel，因为容易写，汗
        for c in self.combine:
            A = (c[0][0], c[1][1])
            B = (c[1][0], c[0][1])
            if A in self.exist and B in self.exist:
                currArea = getArea(c)
                self.res = min(self.res, currArea)

        return self.res

test = Solution()
print test.minAreaFreeRect([[1,1],[1,3],[3,1],[3,3],[2,2]])