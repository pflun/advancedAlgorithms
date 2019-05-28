# -*- coding: utf-8 -*-
# 原题是definitely a mountain，我还多写了检查单调递增和单调递减
class Solution(object):
    def peakIndexInMountainArray(self, A):
        idx = 0
        flag = 1

        for i in range(len(A) - 1):
            if A[i] < A[i + 1] and flag == 1:
                idx = i + 1
            elif A[i] >= A[i + 1] and flag == 1:
                flag = 0
            elif flag == 0:
                if A[i] <= A[i + 1]:
                    return False

        return idx

test = Solution()
print test.peakIndexInMountainArray([0,2,1,0])