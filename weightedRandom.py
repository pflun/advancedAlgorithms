# -*- coding: utf-8 -*-
# 若权重数组为 [1, 3, 2] 的话，那么累加和数组为 [1, 4, 6]，整个的权重和为6
# 随机到 0 则为第一个点，随机到 1，2，3 则为第二个点，随机到 4，5 则为第三个点
# 所以随机出一个数字x后, 用二分查找法可以找到第一个大于随机数x的数字的坐标, 如果不用binary search就用自带方法upper_bound
import random
class Solution(object):

    def __init__(self, w):
        self.candidates = []
        self.sum = 0
        for n in w:
            self.sum += n
            if len(self.candidates) == 0:
                self.candidates.append(n)
            else:
                self.candidates.append(n + self.candidates[-1])

    def pickIndex(self):
        r = random.randint(0, self.sum)
        return self.binarySearch(r)

    # find smallest element that larger than target
    def binarySearch(self, r):
        low = 0
        high = len(self.candidates) - 1
        while low < high:
            mid = (low + high) / 2
            if self.candidates[mid] <= r:
                low = mid + 1
            else:
                high = mid
        return low if self.candidates[low] > r else high


obj = Solution([1,3,2])
print obj.pickIndex()