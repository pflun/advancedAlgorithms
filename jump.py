# -*- coding: utf-8 -*-
# Greedy algorithm (another solution: DP)

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, nums):
        # P is the min steps to reach each position
        p = [0]
        for i in range(len(nums) - 1):
            print i, p
            # as long as not exceed the jumpability, append curr steps (which is also the min steps). Below is a very tricky way to write.
            # 位置0能跳两步，就把位置1和2设成 0 ＋ 1， 0 ＋ 1
            while i + nums[i] >= len(p) and len(p) < len(nums):
                p.append(p[i] + 1)
        return p[-1]

test = Solution()
print test.jump([2,3,1,1,4])