# -*- coding: utf-8 -*-
# https://www.hack2hire.com/companies/verkada/coding-questions/6a14d6957b0582b352787fa7/practice
# You are standing on a one-dimensional array nums at a starting position index. You also have an internal value called currentHeight,
# which is initialized to nums[index]. From there, you attempt to traverse the array by jumping between indices.
# For each jump:
# The first jump goes to the left. After every successful jump, the direction flips between left and right.
# In the current direction, you must land on the nearest index i such that nums[i] == currentHeight + 1.
# The current index itself is never a valid landing target.
# After a successful jump, update currentHeight = currentHeight + x. This update is based on the previous currentHeight, not on nums[i] at the landing position.
# If no valid landing index exists in the current direction, the traversal stops.
# Return the final index where the traversal stops. This may be the starting index if the first jump is not possible.
# Input: nums = [3, 5, 1, 4, 2, 5, 6], index = 4, x = 1
# Output: 6
# Explanation: Starting at index 4 with currentHeight = 2 and direction = left, the traversal jumps along the sequence 4 → 0 → 3 → 1 → 6,
# with currentHeight growing 2 → 3 → 4 → 5 → 6. After landing at index 6, the next required target is 7, which no index holds, so the traversal stops at index 6.

class Solution(object):
    def finalIndex(self, nums, index, x):
        # 预处理：记录每个数字出现的所有索引
        # 例如 nums = [3, 5, 1, 4, 2, 5, 6]
        # dic[5] = [1, 5]
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], []) + [i]
        curr_idx = index
        curr_height = nums[index]
        dir = 'left'

        while True:
            target_height = curr_height + 1
            if target_height not in dic:
                break
            candidate_idx = dic[target_height]
            next_idx = self.bisect(candidate_idx, curr_idx, dir)
            if next_idx == -1:
                break
            curr_idx = next_idx
            curr_height += x
            dir = 'right' if dir == 'left' else 'left'

        return curr_idx

    def bisect(self, indexes, target, dir):
        if dir == 'left':
            for idx in indexes[::-1]:
                if idx < target:
                    return idx
        else:
            for idx in indexes:
                if idx > target:
                    return idx
        return -1

test = Solution()
print test.finalIndex([3, 5, 1, 4, 2, 5, 6], 4, 1)