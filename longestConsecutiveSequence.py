# -*- coding: utf-8 -*-
# We can solve this problem in O(n) time using an Efficient Solution. The idea is to use Hashing.
# We first insert all elements in a Hash.
# Then check all the possible starts of consecutive subsequences
# 把nums扔哈希表里
# 查 num - 1 在不在哈希表里，不在就证明这个num是subsequence的起点
# 一直加一看看都在不在哈希表里，最后用count更新res

class Solution(object):
    def longestConsecutive(self, nums):
        hash = set(nums)
        res = 0
        count = 0

        for num in nums:
            if num - 1 not in hash:
                count = 1
                k = 1
                while num + k in hash:
                    count += 1
                    k += 1
                    # 记得从hash里删掉，下次就不用找了

            res = max(res, count)
        return res

test = Solution()
print test.longestConsecutive([100, 4, 200, 1, 3, 2])
