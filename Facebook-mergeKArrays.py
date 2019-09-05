# Given k sorted arrays of possibly different sizes, find m-th smallest value in the merged array.
# Examples:
# Input: m = 5
# arr[][] = { {1, 3},
# {2, 4, 6},
# {0, 9, 10, 11}} ;
# Output: 4
# Explanation: The merged array would be {0 1 2 3 4 6 9 10 11}.
# The 5-th smallest element in this merged array is 4.
#
# Input: M = 2
# arr[][] = { {1, 3, 20},
# {2, 4, 6}} ;
# Output: 2
#
# Input: M = 6
# arr[][] = { {1, 3, 20},
# {2, 4, 6}} ;
# Output: 20
import heapq
class Solution(object):
    def mergeKArrays(self, lists, M):
        res = float('inf')
        heap = []
        heapq.heapify(heap)
        for i in range(len(lists)):
            # (value, which list, first index 0
            heapq.heappush(heap, (lists[i][0], i, 0))
        while heap and M > 0:
            currVal, currList, currIdx = heapq.heappop(heap)
            res = currVal
            M -= 1
            if currIdx + 1 < len(lists[currList]):
                heapq.heappush(heap, (lists[currList][currIdx + 1], currList, currIdx + 1))
        return res

test = Solution()
print test.mergeKArrays([[1,3], [2,4,6], [0,9,10,11]], 5)