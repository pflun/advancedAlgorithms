# -*- coding: utf-8 -*-
# https://leetcode.com/problems/maximum-number-of-visible-points/discuss/877822/Python-clean-sliding-window-solution-with-explanation
import math

class Solution(object):
    # sliding window
    def visiblePoints(self, points, angle, location):
        radians = []
        # 是否有多少个刚好在location的点
        includeLoc = 0
        for p in points:
            if p[1] == location[1] and p[0] == location[0]:
                includeLoc += 1
            else:
                curr = math.atan2(p[1] - location[1], p[0] - location[0])
                radians.append(curr)
        radians.sort()
        # circular array
        radians = radians + [x + 2.0 * math.pi for x in radians]
        angle = math.pi * angle / 180
        l = 0
        res = 0
        for r in range(len(radians)):
            while radians[r] - radians[l] > angle:
                l += 1
            res = max(res, r - l + 1)

        return res + includeLoc

    def visiblePoints2(self, points, angle, location):
        angles = []
        same_pos_count = 0
        pos_x, pos_y = location
        
        # 1. 过滤重合点，计算非重合点的角度
        for x, y in points:
            if x == pos_x and y == pos_y:
                same_pos_count += 1
            else:
                # math.atan2(y, x) 返回的是弧度，用 math.degrees 转换为角度
                radian = math.atan2(y - pos_y, x - pos_x)
                deg = math.degrees(radian)
                angles.append(deg)
                
        # 2. 从小到大排序
        angles.sort()
        
        # 3. 破环成链：把所有角度加 360 度拼接在后面
        angles = angles + [a + 360 for a in angles]
        
        # 4. 滑动窗口找最多能覆盖多少个点
        max_visible = 0
        left = 0
        
        for right in range(len(angles)):
            # 如果当前窗口里的最大角度差超出了视野 angle，左边界就往右缩
            while angles[right] - angles[left] > angle:
                left += 1
            
            # 记录窗口内能装下的最多点数
            max_visible = max(max_visible, right - left + 1)
            
        # 别忘了加上那些和你站在一起的 VIP 点
        return max_visible + same_pos_count
test = Solution()
print test.visiblePoints([[2,1],[2,2],[3,3]], 90, [1, 1])
print test.visiblePoints([[2,1],[2,2],[3,4],[1,1]], 90, [1, 1])
print test.visiblePoints([[1,0],[2,1]], 13, [1, 1])
print test.visiblePoints([[1,0],[0,1], [2, 1], [1, 2]], 13, [1, 1])