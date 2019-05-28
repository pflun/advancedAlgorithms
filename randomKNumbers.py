# -*- coding: utf-8 -*-
# 作弊：random.shuffle(list)
# 给一个数组，随机取出其中k个数，要求数组中每个数被取到的概率相等。一般会考你允许改动当前数组和不允许改变这两种

import random
class Solution(object):
    def randomKNumbers(self, nums, k):
        # 前i个元素里随机一个，然后和 i 交换，从而保证每一位都被随机换过
        for i in range(len(nums)):
            # 随即一个index
            index = random.randint(0, i)
            # swap with i
            nums[index], nums[i] = nums[i], nums[index]

        return nums[:k]



# Your Solution object will be instantiated and called as such:
obj = Solution()
print obj.randomKNumbers([10, 80, 30, 90, 40, 50, 70], 3)