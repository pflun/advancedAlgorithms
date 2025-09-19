# -*- coding: utf-8 -*-
# 先对每块独立的island计算面积，赋予一个ID存入dic {2: 7}，ID从2开始并且把ID写入grid对应island
# 对于每个0，看上下左右的ID，从dic里拿ID取面积，最后加上1（flip） 切勿重复计算
class Solution(object):
    def largestIsland(self, grid):
        index = 2
        dic = {0: 0}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.size = 0
                    self.dfs(grid, i, j, set(), index)
                    dic[index] = self.size
                    index += 1
        res = max(dic.values())
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    tmp = 1
                    possible = set()
                    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for d in dir:
                        currx = i + d[0]
                        curry = j + d[1]
                        if currx < 0 or currx >= len(grid) or curry < 0 or curry >= len(grid[0]):
                            continue
                        possible.add(grid[currx][curry])
                    for p in possible:
                        tmp += dic[p]
                    res = max(res, tmp)
        return res

    def dfs(self, grid, i, j, visited, index):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited or grid[i][j] != 1:
            return

        self.size += 1
        visited.add((i, j))
        grid[i][j] = index
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for d in dir:
            currx = i + d[0]
            curry = j + d[1]
            self.dfs(grid, currx, curry, visited, index)

test = Solution()
print test.largestIsland([[1,0],[0,1]])
print test.largestIsland([[1,1],[1,0]])
print test.largestIsland([[1,1],[1,1]])