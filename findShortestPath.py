# -*- coding: utf-8 -*-
# 先dfs把可以走的坐标画出来，就是visited set s
# bfs找最短距离
class Solution(object):
    def findShortestPath(self, master):
        self.target = None
        def dfs(i, j):
            if master.isTarget():
                self.target = (i, j)
            for dir, ndir, a, b in dirs:
                x, y = i + a, j + b
                if master.canMove(dir) and (x, y) not in s:
                    # visited set s later use for empty cell (可走的坐标集合)
                    s.add((x, y))
                    master.move(dir)
                    dfs(x, y)
                    master.move(ndir)

        self.target = None
        s = set()
        dirs = [
            ['U', 'D', -1, 0],
            ['D', 'U', 1, 0],
            ['L', 'R', 0, -1],
            ['R', 'L', 0, 1],
        ]
        dfs(0, 0)
        if self.target is None:
            return -1
        s.remove((0, 0))
        q = deque([(0, 0)])
        ans = -1
        while q:
            ans += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                if (i, j) == self.target:
                    return ans
                for _, _, a, b in dirs:
                    x, y = i + a, j + b
                    # 如果可以继续走
                    if (x, y) in s:
                        s.remove((x, y))
                        q.append((x, y))
        return -1