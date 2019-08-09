# -*- coding: utf-8 -*-
# 任意两个不在同行或同列的 1 作为对角线，那么另外两点坐标也得出。记得结果除以4因为重复计算（要优化）
class Solution(object):
    def countCornerRectangles(self, grid):
        cnt = 0
        ones = []
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] == 1:
                    ones.append([j, i])

        for k in range(len(ones)):
            for l in range(len(ones)):
                if k != l:
                    if self.isCornerRectangle(grid, ones[k], ones[l]):
                        cnt += 1

        return cnt / 4

    def isCornerRectangle(self, grid, p1, p2):
        if p1[0] == p2[0] or p1[1] == p2[1]:
            return False
        if grid[p1[0]][p2[1]] == 1 and grid[p2[0]][p1[1]] == 1:
            return True
        else:
            return False

test = Solution()
print test.countCornerRectangles([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]])
print test.countCornerRectangles([
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1]])