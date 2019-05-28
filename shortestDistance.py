# -*- coding: utf-8 -*-
import heapq
class Solution(object):
    def shortestDistance(self, grid):
        # 预处理得到building/1的坐标
        building = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    building.append([x, y])

        # 对每个空地/0求到每个building/1的距离之和，加入heap，堆顶为最小距离之和
        heap = []
        heapq.heapify(heap)
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 0:
                    tmp = 0
                    for b in building:
                        bx = b[0]
                        by = b[1]
                        tmp += self.bfs(grid, x, y, bx, by)
                    heapq.heappush(heap, [tmp, y, x])

        return [heap[0][1], heap[0][2]]

    def bfs(self, grid, currx, curry, nx, ny):

        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        queue = [[currx, curry]]

        steps = 0
        # bfs 一层一层遍历，每层steps++
        while queue:
            size = len(queue)
            for _ in range(size):
                cell = queue.pop(0)
                mx = cell[0]
                my = cell[1]
                # 2, obstacle
                if grid[my][mx] == 2:
                    continue
                # 找到1, building
                elif mx == nx and my == ny:
                    return steps
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

            steps += 1

        # 走到这里证明没找到target
        return float('inf')

test1 = Solution()
print test1.shortestDistance([
    [1, 0, 2, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
])
test2 = Solution()
print test2.bfs([
    [1, 0, 2, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
], 2, 1, 0, 0)