# -*- coding: utf-8 -*-
# 作弊：random.shuffle(list)

import random
class Solution(object):
    def __init__(self, nums):
        self.default = nums

    def reset(self):
        return self.default

    def shuffle(self):
        clone = self.default
        # 前i个元素里随机一个，然后和 i 交换，从而保证每一位都被随机换过
        for i in range(len(clone)):
            # 随即一个index
            index = random.randint(0, i)
            # swap with i
            clone[index], clone[i] = clone[i], clone[index]

        return clone



# Your Solution object will be instantiated and called as such:
obj = Solution([10, 80, 30, 90, 40, 50, 70])
print obj.reset()
print obj.shuffle()