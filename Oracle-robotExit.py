# -*- coding: utf-8 -*-
# 一个robot，一些blocker，一个exit，robot可以走两种step，一种叫一小步move一个unit，一种叫一大步move两个unit。问走出去的最小step。
class Solution(object):
    def robotExit(self, matrix):
        queue = [[0, 0]]
        visited = set()
        step = 0
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0], [0, 2], [2, 0], [0, -2], [-2, 0]]
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop()
                for d in dir:
                    curry = curr[0] + d[0]
                    currx = curr[1] + d[1]
                    if curry < 0 or currx < 0 or curry > len(matrix) - 1 or currx > len(matrix[0]) - 1 or (curry, currx) in visited or matrix[curry][currx] == 1: # use 1 as blocker
                        continue
                    if matrix[curry][currx] == 2: # 2 as exit
                        return step + 1
                    queue.append([curry, currx])
                    visited.add((curry, currx))
            step += 1

        return False

test1 = Solution()
print test1.robotExit([
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 2]
])