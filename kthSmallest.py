# -*- coding: utf-8 -*-
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        heap = [float('-inf')] * k
        heapq.heapify(heap)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < -heap[0]:
                    heapq.heapreplace(heap, self.negativify(matrix[i][j]))

        return -heap[0]



    def negativify(self, n):
        n = -n
        return n

    def kthSmallest2(self, matrix, k):
        n = len(matrix)
        # min
        left = matrix[0][0]
        # max
        right = matrix[n - 1][n - 1]

        while left + 1 < right:
            mid = (right - left) / 2 + left
            num = self.count(matrix, mid)
            # 比mid小的元素大于k个，从前半部分继续找
            if num >= k:
                right = mid
            else:
                left = mid

        if self.count(matrix, right) <= k - 1:
            return right
        else:
            return left

    # 数比target小的有多少个
    def count(self, matrix, target):
        n = len(matrix)
        res = 0
        # 从左下往右上找
        i = n - 1
        j = 0

        while i >= 0 and j < n:
            if matrix[i][j] < target:
                res += i + 1
                j += 1
            else:
                i -= 1
        return res

test = Solution()
# print test.kthSmallest2([
#     [1, 5, 9],
#     [10, 11, 13],
#     [12, 13, 15]
# ], 8)

print test.count([
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
], 13)