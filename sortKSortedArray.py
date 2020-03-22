# https://www.techiedelight.com/sort-k-sorted-array/
# Given a k-sorted array that is almost sorted such that
# each of the N elements may be misplaced by no more than k positions from the correct sorted order.
# Find a space-and-time efficient algorithm to sort the array.
#
# Insert first k + 1 elements into the heap. Then we remove min from the heap and insert next element from the array into the heap and and continue the process
# till both array and heap is exhausted. Each pop operation from the heap should insert the corresponding top element in its correct position in the array.
import heapq
class Solution(object):
    def sortKSortedArray(self, arr, k):
        res = []
        heap = []
        heapq.heapify(heap)
        for i in range(k + 1):
            heapq.heappush(heap, arr[i])
        for j in range(k + 1, len(arr)):
            curr = heapq.heappop(heap)
            res.append(curr)
            heapq.heappush(heap, arr[j])
        while heap:
            curr = heapq.heappop(heap)
            res.append(curr)
        return res

test = Solution()
print test.sortKSortedArray([1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2)
