import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        uglyNumbers = [1]
        heap = [[2, 2], [3, 3], [5, 5]]
        idx2 = 0
        idx3 = 0
        idx5 = 0

        heapq.heapify(heap)

        i = 0
        while i < n:

            tmp = heapq.heappop(heap)
            uglyNumbers.append(tmp[0])
            print heap
            if tmp[1] == 2:
                idx2 += 1
                heapq.heappush(heap, [uglyNumbers[idx2] * 2, 2])
            elif tmp[1] == 3:
                idx3 += 1
                heapq.heappush(heap, [uglyNumbers[idx3] * 3, 3])
            elif tmp[1] == 5:
                idx5 += 1
                heapq.heappush(heap, [uglyNumbers[idx5] * 5, 5])

            i += 1
        return uglyNumbers

# Solution need debug
test = Solution()
print test.nthUglyNumber(10)