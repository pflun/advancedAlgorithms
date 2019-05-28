# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=OFkLC30OxXM
import heapq

# class Location(object):
#     def __init__(self, height, x, y):
#         self.height = height
#         self.x = x
#         self.y = y

class Solution(object):
    def golfMaze(self, forest):

        m = len(forest)
        n = len(forest[0])

        res = 0
        trees = []
        heapq.heapify(trees)

        # 按高度加入
        for y in range(m):
            for x in range(n):
                # Amazon OA gulf 和 LC675 区别：亚麻OA 1 是草地可以走，> 1 才是树
                if forest[y][x] > 1:
                    heapq.heappush(trees, [[forest[y][x]], x, y])

        # 亚麻OA 可以从四个角
        currx = 3
        curry = 1

        while trees:
            tmp = heapq.heappop(trees)

            nx = tmp[1]
            ny = tmp[2]
            steps = self.bfs(forest, currx, curry, nx, ny)

            # 处理高度相等，tmp 和 tmp2
            if trees and tmp[0] == trees[0][0]:
                tmp2 = heapq.heappop(trees)
                nx2 = tmp2[1]
                ny2 = tmp2[2]
                steps2 = self.bfs(forest, currx, curry, nx2, ny2)

                if steps < steps2:
                    heapq.heappush(trees, tmp2)
                # 两种可能都走不到
                elif steps == float('inf') and steps2 == float('inf'):
                    return -1
                # step2 离当前位置更近，把tmp放回heap，更新steps，tmp2的坐标赋给tmp然后赋给下一次curr的坐标
                else:
                    heapq.heappush(trees, tmp)
                    steps = min(steps, steps2)
                    nx = nx2
                    ny = ny2

            # 走不到
            if steps == float('inf'):
                return -1

            # Cut
            forest[ny][nx] = 1

            res += steps

            # 走得到就把当前位置挪到next坐标
            currx = nx
            curry = ny

        return res

    def bfs(self, forest, currx, curry, nx, ny):

        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        queue = [[currx, curry]]

        steps = 0
        # bfs 一层一层遍历，每层steps++
        while queue:
            size = len(queue)
            for i in range(size):
                cell = queue.pop(0)
                mx = cell[0]
                my = cell[1]
                # 找到target
                if mx == nx and my == ny:
                    return steps
                # 没找到就四个方向走
                for i in range(4):
                    x = mx + dir[i][0]
                    y = my + dir[i][1]

                    # 出界 or 障碍 or visited
                    if x < 0 or y < 0 or x >= len(forest[0]) or y >= len(forest) or forest[y][x] == 0 or (x, y) in visited:
                        continue
                    # Tip：往set里加要用tuple而不能用list，unhashable
                    visited.add((x, y))
                    # 加入queue
                    queue.append([x, y])

            steps += 1

        # 走到这里证明没找到target
        return float('inf')

test1 = Solution()
print test1.golfMaze([
    [1, 3, 0, 2],
    [1, 1, 3, 1]
])