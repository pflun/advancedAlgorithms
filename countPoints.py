# -*- coding: utf-8 -*-
import bisect

class Solution(object):
    def countPoints(self, points, queries):
        res = []
        for q in queries:
            cnt = 0
            for p in points:
                if abs(p[0] - q[0]) ** 2 + abs(p[1] - q[1]) ** 2 <= q[2] ** 2:
                    cnt += 1
            res.append(cnt)
        return res

    # 如果有很多点很多圆，如何提高效率
    # 1. sort by x 坐标, bisect on x 2. 对于落在[cx - r, cx + r]内的点计算距离
    def countPoints2(self, points, queries):
        # 1. 按照 x 坐标对所有点进行升序排序
        points.sort(key=lambda p: p[0])
        
        # 单独把 x 坐标抽出来，为了能直接用 bisect 二分查找
        x_coords = [p[0] for p in points]
        
        res = []
        for cx, cy, r in queries:
            count = 0
            
            # 2. 找到圆在 X 轴上的最小和最大边界
            min_x = cx - r
            max_x = cx + r
            
            # 使用二分查找，瞬间锁定嫌疑点的范围 [left, right)
            left = bisect.bisect_left(x_coords, min_x)
            right = bisect.bisect_right(x_coords, max_x)
            
            # 3. 只遍历在这个 [left, right) 索引范围内的点
            for i in range(left, right):
                px, py = points[i]
                
                # 计算真实的欧氏距离的平方 (避免开根号带来的浮点数精度误差！)
                if (px - cx) ** 2 + (py - cy) ** 2 <= r ** 2:
                    count += 1
                    
            res.append(count)
            
        return res

test = Solution()
print test.countPoints([[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]])
print test.countPoints([[1,1],[2,2],[3,3],[4,4],[5,5]], [[1,2,2],[2,2,2],[4,3,2],[4,3,3]])