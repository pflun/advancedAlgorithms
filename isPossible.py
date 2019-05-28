# -*- coding: utf-8 -*-
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106493/C%2B%2B-O(n)-solution-two-pass
# below code bug
class Solution(object):
    def isPossible(self, nums):
        freq = {}
        tails = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for n in nums:
            if n not in freq:
                continue
            freq[n] -= 1
            if tails[n - 1] > 0:
                tails[n - 1] -= 1
                tails[n] += 1
            elif freq[n + 1] and freq[n + 2]:
                freq[n + 1] -= 1
                ferq[n + 2] -= 1
                tails[n + 2] += 1
            else:
                return False
        return True

# https://www.youtube.com/watch?v=GzEek52CyW8&t=467s
# 小Q这个状态机的解法似乎更好，贪心法优先给能接上的，不能接上重新开序列，
# 1和2还没接好（状态机里不为0就是还存在没接好，为0就是接好了进位给3）再重开序列就返回false
# 当前 len = 1的集合 1 0 0 1 0 0 0 0
#      len = 2      0 1 0 0 1 1 1 0
#      len >= 3     0 0 1 1 1 1 1 2
# [1,2,3,3,4,4,5,5] 1 2 3 3 4 4 5 5

test = Solution()
print test.isPossible([1,2,3,3,4,4,5,5])