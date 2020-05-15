# -*- coding: utf-8 -*-
# "Absolute difference between any two elements is less than or equal to limit" is basically => "Absolute difference between min and max elements of subarray"
# two pointer, maxQueue保持降序，minQueue保持升序
class Solution(object):
    def longestSubarray(self, nums, limit):
        res = 1
        maxQueue = []
        minQueue = []
        l = 0
        r = 0
        while r < len(nums):
            # update maxQueue
            while len(maxQueue) != 0 and maxQueue[-1] < nums[r]:
                maxQueue.pop()
            maxQueue.append(nums[r])

            # update minQueue
            while len(minQueue) != 0 and minQueue[-1] > nums[r]:
                minQueue.pop()
            minQueue.append(nums[r])

            # move left pointer
            while maxQueue[0] - minQueue[0] > limit:
                if maxQueue[0] == nums[l]:
                    maxQueue.pop(0)
                if minQueue[0] == nums[l]:
                    minQueue.pop(0)
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res


test = Solution()
print test.longestSubarray([8,2,4,7], 4)