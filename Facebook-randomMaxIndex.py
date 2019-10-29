# -*- coding: utf-8 -*-
# Generate random max index
# Given an array of integers, randomly return an index of the maximum value seen by far.
# e.g. Given [11,30,2,30,30,30,6,2,62, 62]
# Having iterated up to the at element index 5 (where the last 30 is), randomly give an index among [1, 3, 4, 5]
# which are indices of 30 - the max value by far. Each index should have a ¼ chance to get picked.
# Having iterated through the entire array, randomly give an index between 8 and 9 which are indices of the max value 62.
import random
class Solution(object):
    def __init__(self, arr):
        self.dic = {}
        curr = float('-inf')
        for i in range(len(arr)):
            if arr[i] < curr:
                self.dic[i] = self.dic[i - 1]
                continue
            elif arr[i] == curr:
                self.dic[i] = self.dic[i - 1] + [i]
            else:
                curr = arr[i]
                self.dic[i] = [i]

    def getRandom(self, index):
        candidates = self.dic[index]
        randNum = random.randint(0, len(candidates) - 1)
        return candidates[randNum]

test = Solution([11,30,2,30,30,30,6,2,62,62])
print test.getRandom(5)
print test.dic