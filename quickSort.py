# -*- coding: utf-8 -*-
# low  --> Starting index,  high  --> Ending index
class Solution(object):
    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)

            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

        return arr

    def partition(self, arr, low, high):
        # pivot (Element to be placed at right position)
        pivot = arr[high]

        # Index of smaller element
        i = low - 1

        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            # 这个双指针就像moveZeros, 小于pivot挪前面，大的挪后面
            if arr[j] <= pivot:
                i += 1
                # swap
                arr[i], arr[j] = arr[j], arr[i]

        # pivot挪到小于组的下一个（和大于组第一个交换）
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        # 返回pivot位置，下次partition就这个分（pi - 1组 和 pi + 1组）
        return i + 1

test = Solution()
print test.quickSort([10, 80, 30, 90, 40, 50, 70], 0, 6)