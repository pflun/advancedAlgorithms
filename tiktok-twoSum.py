# -*- coding: utf-8 -*-
# 数组里是否有2个数相加得到k，数组支持增加/删除，查询时间要求O(1)
class Solution(object):
    def __init__(self, nums, k):
        self.dic = {}
        self.k = k
        for i in range(len(nums)):
            self.dic[k - nums[i]] = self.dic.get(k - nums[i], 0) + 1

    def add(self, num):
        # query, 不知道原题是在一起还是单独query method
        if num in self.dic:
            res = True
        else:
            res = False
        self.dic[self.k - num] = self.dic.get(self.k - num, 0) + 1
        return res

    def delete(self, num):
        if self.k - num not in self.dic:
            return False
        self.dic[self.k - num] = self.dic.get(self.k - num, 0) - 1
        if self.dic[self.k - num] == 0:
            del self.dic[self.k - num]
        return True