# -*- coding: utf-8 -*-
# https://www.geeksforgeeks.org/quickselect-algorithm/
# Find k smallest
class Solution(object):
    def quickSelect(self, arr, l, r, k):
        if k > 0 and k <= r - l + 1:
            index = self.partition(arr, l, r)
            if index - l == k - 1:
                return arr[index]
            elif index - l > k - 1:
                return self.quickSelect(arr, l, index - 1, k)
            elif index - l < k - 1:
                return self.quickSelect(arr, index + 1, r, k - index + l - 1)

    def partition(self, arr, low, high):
        # pivot (Element to be placed at right position)
        pivot = arr[high]

        # Index of smaller element
        i = low

        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            # 这个双指针就像moveZeros, 小于pivot挪前面，大的挪后面
            if arr[j] <= pivot:
                i += 1
                # swap
                arr[i], arr[j] = arr[j], arr[i]

        # pivot挪到小于组的下一个（和大于组第一个交换）
        arr[i], arr[high] = arr[high], arr[i]

        # 返回pivot位置，下次partition就这个分（pi - 1组 和 pi + 1组）
        return i

test = Solution()
print test.quickSelect([10, 4, 5, 8, 6, 11, 26], 0, 6, 3)