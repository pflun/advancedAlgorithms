# -*- coding: utf-8 -*-
# 标准单调栈模板 concatenate or i % n 都行
class Solution(object):
    def nextGreaterElements(self, nums):
        stack = []
        nums = nums + nums
        res = [None for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(nums[i])
        return res[:len(nums) / 2]

test = Solution()
print test.nextGreaterElements([1,2,1])
print test.nextGreaterElements([1,2,3,4,3])