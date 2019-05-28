# -*- coding: utf-8 -*-
# 前车限制后车车速
class Solution(object):
    def carFleet(self, target, position, speed):
        # Sort list based on values from another list (position)
        speed = [x for _, x in sorted(zip(position, speed), reverse=True)]
        # Sort position
        position = sorted(position, reverse=True)

        while all(i <= target for i in position):
            for i in range(len(position)):
                position[i] += speed[i]
            for i in range(len(position) - 1):
                if position[i] < position[i + 1]:
                    position[i + 1] = position[i]
                    speed[i + 1] = speed[i]

        return len(set(position))

test1 = Solution()
print test1.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])
