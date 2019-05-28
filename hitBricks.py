# -*- coding: utf-8 -*-
class Solution(object):
    def hitBricks(self, grid, hits):
        res = []
        for hit in hits:
            grid[hit[0]][hit[1]] = 0
            tmp = 0
            for y in range(1, len(grid)):
                for x in range(len(grid[0])):
                    # 是砖 == 1，False会掉
                    if grid[y][x] == 1 and self.bfs(grid, x, y) is False:
                        tmp += 1
            res.append(tmp)
        return res

    def bfs(self, grid, currx, curry):

        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        queue = [[currx, curry]]

        while queue:
            size = len(queue)
            for i in range(size):
                cell = queue.pop(0)
                mx = cell[0]
                my = cell[1]
                # 不连通
                if grid[my][mx] != 1:
                    break
                # 找到第一层
                if my == 0:
                    return True
                # 没找到就四个方向走
                for i in range(4):
                    x = mx + dir[i][0]
                    y = my + dir[i][1]

                    # 出界 or 障碍 or visited
                    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == 0 or (x, y) in visited:
                        continue
                    # Tip：往set里加要用tuple而不能用list，unhashable
                    visited.add((x, y))
                    # 加入queue
                    queue.append([x, y])

        # 走到这里证明没找到target
        return False

test1 = Solution()
print test1.hitBricks([
    [1, 0, 0, 0],
    [1, 1, 0, 0]
], [[1,1],[1,0]])