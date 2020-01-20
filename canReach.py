# -*- coding: utf-8 -*-
# 这不是微软OTS原题么，20191209
class Solution(object):
    def canReach(self, arr, start):
        if arr[start] == 0:
            return True
        else:
            return self.helper(arr, start, {})

    def helper(self, nums, idx, dic):
        # out of boundary
        if idx < 0 or idx >= len(nums):
            return False
        steps = nums[idx]
        # found 0
        if steps == 0:
            return True
        # found in cache
        if idx in dic:
            return dic[idx]
        dic[idx] = False
        # search in left
        leftIdx = idx - steps
        rightIdx = idx + steps
        if leftIdx >= 0:
            if self.helper(nums, leftIdx, dic):
                return True
        # search in right
        if rightIdx < len(nums):
            if self.helper(nums, rightIdx, dic):
                return True
        return False

test = Solution()
print test.canReach([4,2,3,0,3,1,2], 5)
print test.canReach([4,2,3,0,3,1,2], 0)
print test.canReach([3,0,2,1,2], 2)