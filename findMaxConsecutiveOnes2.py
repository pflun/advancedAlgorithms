# -*- coding: utf-8 -*-
# Allow flip at most one 0，思想就是把prev上一个连续1个数存起来，每次prev + 1 + 当前1，再更新prev
class Solution(object):
    def findMaxConsecutiveOnes2(self, nums):
        res = 0
        curr = 0
        cnt = 0
        for n in nums:
            cnt += 1
            if n == 0:
                curr = cnt
                cnt = 0
            res = max(res, cnt + curr)
        return res

test = Solution()
print test.findMaxConsecutiveOnes2([1,0,1,1,0])