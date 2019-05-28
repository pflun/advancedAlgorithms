# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=HzlEkUt2TYs
# BFS, visted的key是 position_speed 拼成的
class Solution(object):
    def racecar(self, target):
        queue = []
        queue.append([0, 1])
        visited = set()
        visited.add("0_1")
        visited.add("0_-1")
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                pos, speed = queue.pop()
                # 加速
                posA = pos + speed
                speedA = speed * 2
                # found target
                if posA == target:
                    return step + 1
                # 剪枝，速度超过2倍target或位置超过2倍target就不考虑了
                if abs(speedA) < target * 2 and abs(posA) < target * 2:
                    queue.append([posA, speedA])
                # 减速
                if speed > 0:
                    speedR = -1
                else:
                    speedR = 1
                tmpKey = str(pos) + "_" + str(speedR)
                if tmpKey not in visited:
                    queue.append([pos, speedR])
                    visited.add(tmpKey)
            step += 1

        # not found
        return -1

test = Solution()
print test.racecar(6)