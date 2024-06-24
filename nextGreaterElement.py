# -*- coding: utf-8 -*-
# Monotonic stack 单调栈模板
# 单调栈保持栈内递增 or 递减（这题是递减）
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        # dic store next great element for each one
        dic = {}
        res = []
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            dic[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        for i in range(len(nums1)):
            res.append(dic[nums1[i]])
        return res

test = Solution()
print test.nextGreaterElement([4,1,2], [1,3,4,2])
print test.nextGreaterElement([2,4], [1,2,3,4])