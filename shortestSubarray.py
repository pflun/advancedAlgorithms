# -*- coding: utf-8 -*-
# 应该可以按照负数分段，每一段套用只有正数的sliding window解, 记得刷题网有原题的，带负数的
class Solution(object):
    def shortestSubarray(self, A, K):
        res = float('inf')
        left = 0
        right = 0
        currSum = 0
        while right <= len(A) - 1:
            currSum += A[right]
            while currSum >= K:
                res = min(res, right - left + 1)
                currSum -= A[left]
                left += 1
            else:
                right += 1
        return -1 if res == float('inf') else res

test = Solution()
print test.shortestSubarray([2,-1,2], 3)