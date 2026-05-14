# -*- coding: utf-8 -*-
# https://www.cnblogs.com/grandyang/p/5628836.html
class Solution(object):
    def canMeasureWater(self, x, y, z):
        # need a bunch of if to take care corner cases
        if z % self.gcd(x, y) == 0:
            return True
        else:
            return False

    # greatest common divisor
    def gcd(self, x, y):
        if x % y == 0:
            return y
        else:
            return self.gcd(y, x % y)

    # https://leetcode.com/problems/water-and-jug-problem/description/
    # 365. Water and Jug Problem
    # 总水量只会因为两种行为而发生改变：
    #    1. 从水龙头接水进系统（增加总水量）
    #    2. 把水倒进下水道（减少总水量）
    #   而在杯子之间互相倒水（比如 1 倒给 2），系统里的总水量是没有任何变化的。
    #   在最优策略中，绝对不会出现“把半杯水倒进下水道”或者“把半杯水用水龙头接满”的操作。
    #   因为一旦你对未知的“半杯水”进行了清空或加满，你之前所有精确倒水累积下来的“刻度”就全部清零作废了
    def canMeasureWater2(self, x, y, target):
        queue = [0]
        visited = set()
        # Four potential operations: +jug1Capacity , -jug1Capacity , +jug2Capacity , -jug2Capacity
        ops = [x, -x, y, -y]
        while queue:
            curr = queue.pop(0)
            for o in ops:
                after = curr + o
                if after == target:
                    return True
                if after not in visited and 0 <= after <= x + y:
                    visited.add(after)
                    queue.append(after)
        return False

test = Solution()
print test.canMeasureWater(2, 6, 5)
print test.gcd(3, 5)
print test.canMeasureWater2(3, 5, 4)
print test.canMeasureWater2(2, 6, 5)
