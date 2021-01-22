# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=g5wLHFTodm0
class Solution(object):
    # Without memory
    def PredictTheWinner(self, nums):
        return True if self.getScore(nums, 0, len(nums) - 1) >= 0 else False

    # Max diff my_score - your_score
    def getScore(self, nums, l, r):
        if l == r:
            return nums[l]
        return max(nums[l] - self.getScore(nums, l + 1, r), nums[r] - self.getScore(nums, l, r - 1))

    # With memory, 用hashmap存 剩下的nums => max_diff，
    # 这样每次先从hashmap里找，如果当前求解还不如hashmap中就剪枝
    def PredictTheWinner2(self, nums):
        self.cache = {}
        return True if self.getScore2(nums, 0, len(nums) - 1) >= 0 else False

    # Max diff my_score - your_score
    def getScore2(self, nums, l, r):
        if l == r:
            return nums[l]
        key = str(l) + '_' + str(r)
        if key in self.cache:
            return self.cache[key]
        self.cache[key] = max(nums[l] - self.getScore2(nums, l + 1, r), nums[r] - self.getScore2(nums, l, r - 1))
        return self.cache[key]

test = Solution()
print test.PredictTheWinner2([1, 5, 233, 7])