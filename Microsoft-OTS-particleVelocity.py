# -*- coding: utf-8 -*-
# stable: at least continuely 3 positions that velocity are same
# 1, 3, 5, 7, 9, velocity is 2
# [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0] => 5, because (0,2) (2,4) (6,9) (6,8) (7,9) note that the last two periods are contained by (6,9)
class Solution(object):
    def particleVelocity(self, arr):
        res = 0
        i = 0
        while i < len(arr):
            tmp = 0
            while i < len(arr) - 2 and arr[i + 2] - arr[i + 1] == arr[i + 1] - arr[i]:
                tmp += 1
                res += tmp
                i += 1
            i += 1
        if res < 1000000000:
            return res
        else:
            return -1

test = Solution()
print test.particleVelocity([-1, 1, 3, 3, 3, 2, 3, 2, 1, 0])
print test.particleVelocity([1,3,5,7,9])
print test.particleVelocity([0,1])
print test.particleVelocity([1,1,2,5,7])