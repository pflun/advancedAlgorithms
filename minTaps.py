# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=G88X89Eo2C0
# Jump Game 2
class Solution(object):
    def minTaps(self, n, ranges):
        nums = [float('inf') for _ in range(n + 1)]
        for i in range(n + 1):
            # 防止左边越界
            s = max(0, i - ranges[i])
            # 只要更新 nums[s] 而无需更新 nums[i] 因为s更靠左更早起跳，你都能从s跳到最右端目标了就不必从i跳
            nums[s] = i + ranges[i]


        res = 0
        # 上次能够跳到的index
        l = 0
        # 下次能够跳到的最大index，i > e表示中间有gap没能跳到 return false
        e = 0
        for i in range(n + 1):
            if i > e:
                return -1
            # 要再跳一次了
            if i > l:
                res += 1
                l = e
            e = max(e, nums[i])

        return res

test = Solution()
print test.minTaps(5, [3,4,1,1,0,0])
print test.minTaps(3, [0,0,0,0])
print test.minTaps(7, [1,2,1,0,2,1,0,1])
print test.minTaps(8, [4,0,0,0,0,0,0,0,4])
print test.minTaps(8, [4,0,0,0,4,0,0,0,4])