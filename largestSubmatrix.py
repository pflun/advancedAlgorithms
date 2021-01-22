# -*- coding: utf-8 -*-
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/discuss/1020710/C%2B%2B-Clean-and-Clear-With-intuitive-pictures-O
# similar: https://leetcode.com/problems/largest-submatrix-with-rearrangements/discuss/1020576/C%2B%2B-Solution-or-Easy-Implementation
# 柱状图找最大矩形高级版，对于每一行要找的柱状图就是这行往上的所有区域，input matrix里0的点造成断开的柱，只有连续1形成的才是valid柱
# rearrange其实按柱高度sort就行，sort完就能不浪费尽可能产生更大的矩形（更高的柱相邻在一起而不被低柱中间打断），就变成了LC84
class Solution(object):
    def largestSubmatrix(self, matrix):
        res = 0
        pillars = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        pillars[0] = matrix[0]
        # 生成柱状图
        for j in range(len(matrix[0])):
            for i in range(1, len(matrix)):
                if matrix[i][j] == 1:
                    pillars[i][j] = pillars[i - 1][j] + 1
        # 对于每一行，rearrange找最大矩形
        for i in range(len(matrix)):
            k = float('inf')
            pillars[i].sort(reverse=True)
            for j in range(len(matrix[0])):
                # 逆排序，越前柱越高，越往后只能变低所以min，面积是宽(j+1) * 高，随着宽度增加才有可能获得更大面积
                k = min(k, pillars[i][j])
                res = max(res, k * (j + 1))
        return res

test = Solution()
print test.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]])
print test.largestSubmatrix([[1,0,1,0,1]])